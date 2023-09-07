from z3 import *
import clingo

class ASP_Floyd_Normal():

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
                ASP_Floyd_Normal.graph_out.add_edge(node0, node1)
        print(ASP_Floyd_Normal.graph_out)        
        ASP_Floyd_Normal.solution_find = True
        raise StopIteration

        
        
               
    def solve(graph_inp, k, source_reach, target_reach, source_not_reach, target_not_reach, graph_out):
        
        ASP_Floyd_Normal.graph_out = graph_out
        ASP_Floyd_Normal.control = clingo.Control()
        # Prepare data using Python functions
        asp_code = ""
        for i in range(graph_inp.number_nodes):
            asp_code += f"node({i}).\n"

        for edge in graph_inp.edge_list: 
            asp_code +=  f'edge({edge[0]}, {edge[1]}).\n' 

        asp_code += f"reachability(X, Y, K) :- reachability(X, K - 1, K - 1), reachability(K - 1, Y, K - 1), node(X), node(Y), node(K - 1).\n"
        
        asp_code += f"no_path_k(X, Y, K) :- not reachability(X, K - 1, K - 1), node(X), node(Y), node(K - 1).\n"
        asp_code += f"no_path_k(X, Y, K) :- not reachability(K - 1, Y, K - 1), node(X), node(Y), node(K -1).\n"
        asp_code += f":- reachability(X, K - 1, K - 1), reachability(K - 1, Y, K - 1), no_path_k(X, Y, K), node(X), node(Y), node(K - 1).\n"


        asp_code += f":- no_path_k(X, Y, K), not reachability(X, Y, K - 1), reachability(X, Y, K), node(X), node(Y), node(K - 1).\n"

        asp_code += "reachability(X, X, 0) :- node(X).\n"
        asp_code += "reachability(X, Y, 0) :- edge(X, Y), node(X), node(Y).\n"
        asp_code += "edge(X, Y) :- reachability(X, Y, 0), node(X), node(Y), X != Y.\n"

        asp_code += "reachability(X, Y, K) :- reachability(X, Y, K - 1), node(X), node(Y), node(K - 1).\n"

        asp_code += f"reachability({source_reach}, {target_reach}, {graph_inp.number_nodes}).\n"
        asp_code += f" :- reachability({source_not_reach}, {target_not_reach}, {graph_inp.number_nodes}).\n"

        asp_code += " :- edge(X, X), node(X).\n"

        asp_code += f"{k + len(graph_inp.edge_list)}{{edge(X, Y): node(X), node(Y)}}{k + len(graph_inp.edge_list)}.\n"
        ASP_Floyd_Normal.control.add("base", [], asp_code)
        ASP_Floyd_Normal.control.ground([("base", [])])
        print("answer ASP Floyd Normal")
        print("****************")
        try:
            ASP_Floyd_Normal.control.solve(on_model = ASP_Floyd_Normal.on_model)
        except: 
            pass
        if(ASP_Floyd_Normal.solution_find == False):
            print("No solution found.")
