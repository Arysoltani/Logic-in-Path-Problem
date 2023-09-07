from z3 import *


class SMT_Floyd_Warshall():

    def print_answer(graph_out, edge_variables, model, number_nodes):

        print("output graph: ")
        for i in range(number_nodes):
            for j in range(number_nodes):
                if(model[edge_variables[i][j]] == 1):
                    graph_out.add_edge(i, j)
        print(graph_out)

    def solve(graph_inp, k, source_reach, target_reach, source_not_reach, target_not_reach, graph_out):
            
        number_nodes = graph_inp.number_nodes

        solver = Solver() 


        edge_variables = [[Int(f'edge_variables_{i}_{j}') for j in range(number_nodes)] for i in range(number_nodes)]

        for edge in graph_inp.edge_list:
            solver.add(edge_variables[edge[0]][edge[1]] == 1)

        for i in range(number_nodes):
            solver.add(edge_variables[i][i] == 0)
            
        solver.add(Sum([edge_variables[i][j] for i in range(number_nodes) for j in range(number_nodes)]) == (len(graph_inp.edge_list) + k))

        for i in range(number_nodes):
            for j in range(number_nodes):
                solver.add(Or(edge_variables[i][j] == 1, edge_variables[i][j] == 0))

        reachability = [[[Bool(f'reachability_{i}_{j}_{k}') for k in range(number_nodes + 1)] for j in range(number_nodes)] 
                        for i in range(number_nodes)]

        for i in range(number_nodes):
            solver.add(reachability[i][i][0] == True)
            for j in range(number_nodes):
                if(i != j):
                    solver.add(Implies((edge_variables[i][j] == 1), reachability[i][j][0] == True))
                    solver.add(Implies((edge_variables[i][j] == 0), reachability[i][j][0] == False))
    
        for k in range(1, number_nodes + 1):
            for i in range(number_nodes):
                for j in range(number_nodes):
                    solver.add(reachability[i][j][k] == Or(reachability[i][j][k - 1], 
                                                           And(reachability[i][k - 1][k - 1], reachability[k - 1][j][k - 1])))
        solver.add(reachability[source_reach][target_reach][number_nodes] == True)

        solver.add(reachability[source_not_reach][target_not_reach][number_nodes] == False)

        print("answer SMT with Floyd Warshal ")
        print("****************")
        if solver.check() == sat:  

                print("*******sat*******")
                model = solver.model()
                SMT_Floyd_Warshall.print_answer(graph_out, edge_variables, model, number_nodes)

        else:
            print('No solution found.')