The code provided defines several classes that work together
to model a Graph object and simulate Fleas moving on it.

The Graph class is responsible for maintaining the adjacency list
of the graph and the state of each vertex.

The Permutation class is used to represent the state of each vertex
as a permutation of its neighbors.

The Flea class is responsible for simulating the movement
of the flea on the graph by applying the appropriate permutation
to determine the destination vertex and updating the state
of the vertices it moves between.

The structure of the graph and number of fleas can be initialized.
The rule of state change can be modified in the state_change function.