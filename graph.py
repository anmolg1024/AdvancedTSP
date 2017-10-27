""" A Python Class
A simple Python graph class, demonstrating the essential 
facts and functionalities of graphs.
"""


class Graph(object):

    def __init__(self, graph_dict=None): #EXP: used to initiate the graph as list of source vertex : target vertices
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys()) #EXP: cool

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()  #EXP: will be defining a method later for this

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = [] #EXP: puts a key in the dictionary with an empty set of values

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge) #EXP: refers to the edge's member conveniently through vertex1 and vertex2
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2) #EXP: adds vertex2 as the second vertex of the edge to the dictionary's key's value
        else:
            self.__graph_dict[vertex1] = [vertex2] #EXP: cool

    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = [] #defines an empty array to display
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour}) #EXP: simply adds key-value pairs to the set edges
        return edges

    def __str__(self): #EXP: simply returns all the vertices in one line and the edges in another line 
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
    
    def find_path(self, start_vertex, end_vertex, path=None):
	    if path == None:
	        path = []
	    graph = self.__graph_dict
	    path = path + [start_vertex]
	    if start_vertex == end_vertex:
	        return path 	#EXP: quite trivial
	    if start_vertex not in graph:  
	        return None 	#EXP: Invalid input
	    for vertex in graph[start_vertex]: #EXP: valid input, graph[start_vertex] accesses the neighbouring vertices of start_vertex
	        if vertex not in path: #EXP if neighbouring edges aren't already in path
	            extended_path = self.find_path(vertex,  #EXP: did not understand this part
	                                           end_vertex, 
	                                           path)
	            if extended_path: #EXP: did not understand this part
	                return extended_path
	    return None


if __name__ == "__main__":

    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }

    graph = Graph(g)

