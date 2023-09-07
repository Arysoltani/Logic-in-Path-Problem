# Logic-in-Path-Problem

Finding Solution To Path Problem with SMT, SAT, and ASP

## The main problem: 

Given variables $n$, $m$, $s$, $t$, $s'$, $t'$, $k$ following $m$ edges with ($v$, $u$) format where $n$ is number of nodes in the graph and $m$ shows number of edges in the graph, $s$ and $t$ are first pair of source and destination, also $s'$ and $t'$ are the second pair of source and destination. Additionally $k$ is the number of edges we want to add to the graph. We want to find out is it possible to add k fresh new edges to the graph where after adding the edges there should be at least one path between node $s$ and $t$, also there shouldn't be any path between nodes $s'$ and $t'$. 

## Solvers

We used ASP, SMT and SAT for solving this question, and compare the solution and solvers with each other. 

### ASP
