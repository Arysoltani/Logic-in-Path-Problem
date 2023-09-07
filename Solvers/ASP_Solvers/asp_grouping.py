from z3 import *
import clingo

class ASP_Grouping():

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
                ASP_Grouping.graph_out.add_edge(node0, node1)
        print(ASP_Grouping.graph_out)        
        ASP_Grouping.solution_find = True
        raise StopIteration

        
        
               
    def solve(graph_inp, k, source_reach, target_reach, source_not_reach, target_not_reach, graph_out):
        
        ASP_Grouping.graph_out = graph_out
        ASP_Grouping.control = clingo.Control()
        # Prepare data using Python functions
        asp_code = ""
        for i in range(graph_inp.number_nodes):
            asp_code += f"node({i}).\n"

        for edge in graph_inp.edge_list: 
            asp_code +=  f'edge({edge[0]}, {edge[1]}).\n' 
        

        asp_code += "edge(X, Y) :- path(X, Y).\n"

        asp_code += f"1{{path({source_reach}, X) : node(X)}}1.\n"
        asp_code += f"1{{path(X, {target_reach}) : node(X)}}1.\n"
        asp_code += f"0{{path(X, Y): node(X)}}1  :- Y != {source_reach}, Y!= {target_reach}, node(Y).\n"
        asp_code += f"0{{path(X, Y): node(Y)}}1  :- X != {source_reach}, X!= {target_reach}, node(X).\n"
        
        asp_code += f"0{{path(X, Y): node(Y)}}0 :- 0{{path(Z, X): node(Z)}}0, X != {source_reach}, X!= {target_reach}, node(X).\n"
        asp_code += f"1{{path(X, Y): node(Y)}}1 :- 1{{path(Z, X): node(Z)}}1, X != {source_reach}, X!= {target_reach}, node(X).\n"
        asp_code += f" :- edge(X, X), node(X).\n"

        asp_code += f"group({source_not_reach}).\n"
        asp_code += f":- group({target_not_reach}).\n"
        asp_code += f"group(Y) :- group(X), node(X), node(Y), edge(X, Y).\n"

        asp_code += f"{k + len(graph_inp.edge_list)}{{edge(X, Y): node(X), node(Y)}}{k + len(graph_inp.edge_list)}\n."

        
        ASP_Grouping.control.add("base", [], asp_code)
        ASP_Grouping.control.ground([("base", [])])
        print("answer ASP Grouping")
        print("****************")
        try:
            ASP_Grouping.control.solve(on_model = ASP_Grouping.on_model)
        except: 
            pass
        if(ASP_Grouping.solution_find == False):
            print("No solution found.")
