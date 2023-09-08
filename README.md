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

## Solution
