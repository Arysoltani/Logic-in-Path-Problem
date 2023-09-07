from Graph import Graph
import itertools
from z3 import *
import sys

def find_combinations(n, k):
    if(n < k):
        return -1
    elements = list(range(n)) 
    return list(itertools.combinations(elements, k))

def generate_permutations(n):
    all_permutations = []
    for r in range(2, n + 1):
        permutations_r = list(itertools.permutations(range(n), r))
        all_permutations.extend(permutations_r)
    return all_permutations



def print_answer(solver, number_nodes, edge_variables):
    print("output graph: ")
    graph_out = Graph(number_nodes)
    for i in range(number_nodes):
         for j in range(number_nodes):
              if(model[edge_variables[i][j]] == True):
                   graph_out.add_edge(i, j)
    print(graph_out)


number_nodes, k, source_reach, target_reach, source_not_reach, target_not_reach = map(int, input().split())
graph_inp = Graph(number_nodes)
graph_inp.read_adj_matrix()
print("input_graph:")
print(graph_inp)

solver = Solver()

edge_variables = [[Bool(f'edge_variables_{i}_{j}') for j in range(number_nodes)] for i in range(number_nodes)]

remain_edges = [(i, j) for i in range(number_nodes) for j in range(number_nodes)]

for edges in graph_inp.edge_list:
    solver.add(edge_variables[edges[0]][edges[1]] == True)
    remain_edges.remove(edges)

combinations = find_combinations(len(remain_edges), k)
if(combinations == -1):
    print('No solution found.')
    sys.exit()

or_predicates = False
if(k == 0):
    or_predicates =True
for combination in combinations:
    and_predicate = True
    for i in range(len(remain_edges)):
        edge = remain_edges[i]
        if(i in combination):
            and_predicate = And(edge_variables[edge[0]][edge[1]], and_predicate)
        else:
            and_predicate = And(Not(edge_variables[edge[0]][edge[1]]), and_predicate)
    or_predicates = Or(and_predicate, or_predicates)
solver.add(or_predicates)

permutations = generate_permutations(number_nodes)

for i in range(number_nodes):
     solver.add(edge_variables[i][i] == False)


and_predicate_cycle = True
and_predicate_no_path = True 
or_predicate_path_exist = False

for perm in permutations:

    or_predicate_cyle = False
    or_predicate_no_path = False 
    and_predicate_path_exist = True

    for i in range(len(perm)):
        nxt = i + 1
        if(nxt == len(perm)):
            nxt = 0
        or_predicate_cyle = Or(Not(edge_variables[perm[i]][perm[nxt]]), or_predicate_cyle)
    and_predicate_cycle = And(or_predicate_cyle, and_predicate_cycle)

    if(perm[0] == source_reach and perm[-1] == target_reach):
        for i in range(len(perm) - 1):
            and_predicate_path_exist = And(edge_variables[perm[i]][perm[i + 1]], 
                                           and_predicate_path_exist)
        or_predicate_path_exist = Or(and_predicate_path_exist, or_predicate_path_exist)
        solver.add(or_predicate_path_exist)
    
    if(perm[0] == source_not_reach and perm[-1] == target_not_reach):
        for i in range(len(perm) - 1):
            or_predicate_no_path = Or(Not(edge_variables[perm[i]][perm[i + 1]]), or_predicate_no_path)
        and_predicate_no_path = And(and_predicate_no_path, or_predicate_no_path)
        solver.add(and_predicate_no_path)

solver.add(and_predicate_cycle)


if solver.check() == sat:

        print("*******sat*******")
        model = solver.model()
        print_answer(model, number_nodes, edge_variables)

else:
    print('No solution found.')

