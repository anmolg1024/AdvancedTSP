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
   
#EXP: The following method finds a path from a start vertex to an end vertex: 
    def find_path(self, start_vertex, end_vertex, path=None):
        if path == None:
            path = []
        graph = self.__graph_dict   
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path     #EXP: quite trivial
        if start_vertex not in graph:  
            return None     #EXP: Invalid input
        for vertex in graph[start_vertex]: #EXP: valid input, graph[start_vertex] accesses the neighbouring vertices of start_vertex
            if vertex not in path: #EXP if neighbouring edges aren't already in path
                extended_path = self.find_path(vertex,  #EXP: did not understand this part
                                               end_vertex, 
                                               path)
                if extended_path: #EXP: did not understand this part:[crack-whenever none is returned it takes extended path 
                                  #exp:  as 0 and when the p is returned(line 71) it will take the non empty list as it as '1'
                    return extended_path
        return None

    def __find_all_paths(self, start, end, path=[]):
        if path == None:
            path = []
        path = path + [start]
        graph = self.__graph_dict
        if start == end:
            return [path]
        if start not in graph:  
            return None     #EXP: Invalid input
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = self.__find_all_paths( node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def find_ham(self):
        count=0
        vertices=self.vertices()
        values=self.__graph_dict.values()
        for val in values:
            if (val !=[]):
                count+=1    
        ham_paths=[]
        for start in vertices:
            for end in vertices:
                if start!=end:
                    allpaths=self.__find_all_paths(start,end)
                    for path in allpaths:
                        if len(path)==count:
                            ham_paths.append(path)
        if ham_paths:
            return ham_paths
        else:
            print ("ham path not present")
            return None
if __name__ == "__main__":					 #EXP: refer: https://stackoverflow.com/questions/419163/what-does-if-name-main-do
    input_dict = input("Input a dictonary in 'vertice : [all its neighbouring vertices]' form ")
    import ast
    g = ast.literal_eval(input_dict)	#EXP-converts string input to a dict 
    graph = Graph(g)                                    #https://stackoverflow.com/questions/17264174/python-how-to-take-a-dictionary-as-input
    print (graph.find_ham())
    

'''	
#readymade input:		g = { "a" : ["d","e"],"b" : ["c","d"],"c" : ["b", "c", "d", "e"],"d" : ["a","b", "c"],"e" : ["c","a"],"f" : []}
'''

""" Code for making the 
