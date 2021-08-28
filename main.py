                                                                 DATA STRUCTURES AND ALGORITHMS
INDEX

Data structurs
--> Arrays
--> Linked Lists
--> Stacks
--> Queues
--> Binary search trees
--> Balanced binary trees
--> Heaps
--> Dictionaries
--> Trees


Graph Algorithms
--> Graph traversal algorithms: BFS and DFS
--> Shortest paths
--> Spanning trees


Sorting algorithms

---------------------------------------------------------


->DATA STRUCTURES : to store data in an efficiend way.
->why to use data structures ?
->we often have the intuition -> if we want to make an algorithms fast we have to optimize it.
  -> avoid nested for loops
  -> make every calculation as fast as possible
  -> but algorithms can be boosted up by proper data structures
  -> data structures make sure the running time will be better.
  -> ex : Facebook uses millions of data so their the speed matters so we must use a good data structure.


Dijkstra algorithm

--> Without a proper data structure ( heap / priority queue ) the running time would be quadratic // O(N^2)
--> Priority queue approach makes sure the running time will be far better // O(N*logN)

Spanning trees

--> We can boost up the algorithm with the help of priority queues as well.
--> So the running time of the algorithms are determined by the data structures we use.

ABT (Abstract Data Type)

--> Basically this is the model ( logical description ) fir a certain data structure.
--> it is like a super =tyoe in programming ( so an interface in java ).
--> We just define what methods / fuctions the data structures will have so we define the basic behavior.
--> important : it is just the model, ADT does not specify the concreate implementation or programming language.
--> for ex : stack -> push() pop() peek()

Data structure

--> The concrete implementation, the actual representation of the data.
--> The aim is to be able to store and retrieve data in an efficient manner.
--> What we want : to be able to insert / find items in o(1) time complexity and to be able to retrive items in o(1) as well.
--> for ex : arrays , linked lists , binary trees etc,.