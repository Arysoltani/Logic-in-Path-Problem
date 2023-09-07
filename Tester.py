from Solvers.SMT_Solvers.smt_grouping import SMT_Grouping
from Solvers.SMT_Solvers.smt_floyd_warshall import SMT_Floyd_Warshall
from Solvers.ASP_Solvers.asp_grouping import ASP_Grouping
from Solvers.ASP_Solvers.asp_floyd_least import ASP_Floyd_Least
from Solvers.ASP_Solvers.asp_floyd_normal import ASP_Floyd_Normal
import time
import sys

from Solvers.Graph import Graph


number_nodes, k, source_reach, target_reach, source_not_reach, target_not_reach = map(int, input().split())
graph_inp = Graph(number_nodes)
graph_inp.read_adj_matrix()
# print("input_graph:")
# print(graph_inp)

type_solver = sys.argv[1]

if(type_solver == "SMT_Grouping"):
    solver = SMT_Grouping
if(type_solver == "SMT_Floyd_Warshall"):
    solver = SMT_Floyd_Warshall
if(type_solver == "ASP_Grouping"):
    solver = ASP_Grouping 
if(type_solver == "ASP_Floyd_Normal"):
    solver = ASP_Floyd_Normal
if(type_solver == "ASP_Floyd_Least"):
    solver = ASP_Floyd_Least

start_time = time.time()
graph_out = Graph(number_nodes)
solver.solve(graph_inp, k, source_reach, target_reach, source_not_reach, target_not_reach, graph_out)
end_time = time.time()
time_taken = end_time - start_time

with open(f'Times/{type_solver}_time.txt', 'a') as file:
    file.write(str(number_nodes) + " " + str(time_taken) + "\n")

print(f"Time taken by {type_solver}: {time_taken} seconds.")
