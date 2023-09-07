from z3 import *

class SMT_Grouping():

    def print_answer(graph_out, edge_variables, model, number_nodes):
        print("output graph: ")
        for i in range(number_nodes):
            for j in range(number_nodes):
                if(model[edge_variables[i][j]] == 1):
                    graph_out.add_edge(i, j)
        print(graph_out)

    def add_path_equations(edge_variables, solver, path_subset, source_reach, target_reach, number_nodes):
        for i in range(number_nodes):
            sum_out = Sum([path_subset[i][j] for j in range(number_nodes)])
            sum_in = Sum([path_subset[j][i] for j in range(number_nodes)])
            if((i != source_reach) and (i != target_reach)):
                solver.add(Or(And(sum_in == 1, sum_out == 1), And(sum_in == 0, sum_out == 0)))
            elif(i == source_reach):
                solver.add(sum_out == 1)
                solver.add(sum_in == 0)
            else:
                solver.add(sum_in == 1)
                solver.add(sum_out == 0)
               
    def solve(graph_inp, k, source_reach, target_reach, source_not_reach, target_not_reach, graph_out):
        
        number_nodes = graph_inp.number_nodes

        solver = Solver() 

        edge_variables = [[Int(f'edge_variables_{i}_{j}') for j in range(number_nodes)] for i in range(number_nodes)]
        path_subset = [[Int(f'path_subset_{i}_{j}') for j in range(number_nodes)] for i in range(number_nodes)]
        group = [Bool(f'group_{i}') for i in range(number_nodes)]

        for edge in graph_inp.edge_list:
            solver.add(edge_variables[edge[0]][edge[1]] == 1)

        for i in range(number_nodes):
            solver.add(edge_variables[i][i] == 0)

        for i in range(number_nodes):
            for j in range(number_nodes):
                solver.add(Or(edge_variables[i][j] == 1, edge_variables[i][j] == 0))
                solver.add(Or(edge_variables[i][j] == path_subset[i][j], 
                            And(edge_variables[i][j] == 1, path_subset[i][j] == 0)))
        solver.add(group[source_not_reach] == False)
        solver.add(group[target_not_reach] == True)
        for i in range(number_nodes):
            for j in range(number_nodes):
                solver.add(Implies(And(group[i] == False, group[j] == True), edge_variables[i][j] == 0))
        #number of edges be num_edges + k
        solver.add(Sum([edge_variables[i][j] for i in range(number_nodes) for j in range(number_nodes)]) == (len(graph_inp.edge_list) + k))

        SMT_Grouping.add_path_equations(edge_variables, solver, path_subset, source_reach, target_reach, number_nodes)
        print("answer SMT Grouping ")
        print("****************")
        if solver.check() == sat:

                print("*******sat*******")
                model = solver.model()
                SMT_Grouping.print_answer(graph_out, edge_variables, model, number_nodes)

        else:
            print('No solution found.')
