# Logic-in-Path-Problem

Finding Solution To Path Problem with SMT, SAT, and ASP

## The main problem: 

Given variables $n$, $m$, $s$, $t$, $s'$, $t'$, $k$ following $m$ edges with ($v$, $u$) format where $n$ is number of nodes in the graph and $m$ shows number of edges in the graph, $s$ and $t$ are first pair of source and destination, also $s'$ and $t'$ are the second pair of source and destination. Additionally $k$ is the number of edges we want to add to the graph. We want to find out is it possible to add k fresh new edges to the graph where after adding the edges there should be at least one path between node $s$ and $t$, also there shouldn't be any path between nodes $s'$ and $t'$. 

## Solvers

We used ASP, SMT and SAT for solving this question, and compare the solution and solvers with each other. 

### Answer Set Programming Solver(ASP):

The main advatage of this method is its usage of least fix point which could be very useful for finding reachability.

### Satisfiability Modulo Theory Solver(SMT):

Have the ability of defining problems in first order logic, which makes it a strong tool. It's advantages over ASP like defing more complex formula is not that much helpful in this problem.

### Satisfiability Solver(SAT): 

It could define propositional logic, which just have variables with True and False. This leads to exhibit exponential growth in complexity when compared to more efficient approaches like SMT (Satisfiability Modulo Theories) and ASP (Answer Set Programming).

## Solutions

### Floyd-Warshal Smilar Algorithm: 

We applied a variant of the Floyd-Warshall algorithm using both SMT and ASP.

## Floyd Warshal with Least Fixed Point:

This implementation is essentially identical to the previous solution, but it leverages the benefits of the least fixed point approach in Answer Set Programming (ASP).

### Grouping 


In this solution, implemented using ASP and SMT, we aim to select paths for both $s$ and $t$ based on a formulated formula. Additionally, we organize nodes into two distinct groups in such a way that edges within each group exclusively have a single direction for ensuring there is no path between $s'$ and $t'$.

## SAT Algorithm 

This algorithm evaluates all potential paths individually and establishes specific conditions for each of them.
