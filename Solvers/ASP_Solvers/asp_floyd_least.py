from z3 import *
import clingo

class ASP_Floyd_Least():

    control = None 
    solution_find = False
    model_ans = None

    def on_model(model):
        
        print("Answer Set Exist")

        print("output graph: ")

        for symbol in model.symbols(shown=True):
            if symbol.name == "edge":
                node0 = symbol.arguments[0].number
                node1 = symbol.arguments[1].number 
                ASP_Floyd_Least.graph_out.add_edge(node0, node1)
        print(ASP_Floyd_Least.graph_out)        
        ASP_Floyd_Least.solution_find = True
        raise StopIteration

        
        
               
    def solve(graph_inp, k, source_reach, target_reach, source_not_reach, target_not_reach, graph_out):
        
        ASP_Floyd_Least.graph_out = graph_out
        ASP_Floyd_Least.control = clingo.Control()
        # Prepare data using Python functions
        asp_code = ""
        for i in range(graph_inp.number_nodes):
            asp_code += f"node({i}).\n"

        for edge in graph_inp.edge_list: 
            asp_code +=  f'edge({edge[0]}, {edge[1]}).\n' 
        


        asp_code += "reachability(X, Y) :- reachability(X, Z), edge(Z, Y), node(X), node(Y), node(Z).\n"
        asp_code += "reachability(X, X) :- node(X).\n"
        asp_code += ":- reachability(X, Y), reachability(Y, Z), not reachability(X, Z), node(X), node(Y), node(Z).\n"
        asp_code += " :- edge(X, X), node(X).\n"

        asp_code += f"reachability({source_reach}, {target_reach}).\n"
        asp_code += f" :- reachability({source_not_reach}, {target_not_reach}).\n"

        asp_code += f"{k + len(graph_inp.edge_list)}{{edge(X, Y): node(X), node(Y)}}{k + len(graph_inp.edge_list)}\n."

        
        ASP_Floyd_Least.control.add("base", [], asp_code)
        ASP_Floyd_Least.control.ground([("base", [])])
        print("answer ASP Floyd Least")
        print("****************")
        try:
            ASP_Floyd_Least.control.solve(on_model = ASP_Floyd_Least.on_model)
        except: 
            pass
        if(ASP_Floyd_Least.solution_find == False):
            print("No solution found.")
