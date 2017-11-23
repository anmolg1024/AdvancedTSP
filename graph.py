""" A Python Class
A simple Python graph class, demonstrating the essential 
facts and functionalities of graphs.
"""

'''	
		g = { "a" : ["d","e"],
		  "b" : ["c","d"],
		  "c" : ["b", "c", "d", "e"],
		  "d" : ["a","b", "c"],
		  "e" : ["c","a"],
		  "f" : []
		}
'''
	
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
		return sorted(list(self.__graph_dict.keys())) #EXP: cool

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
		for vertex in self.__graph_dict:            #EXP:refer: http://www.techeuler.com/python/usage-of-underscores-before-and-after-function-name-in-python/
			for neighbour in self.__graph_dict[vertex]:
				edges.append((vertex, neighbour)) #EXP: simply adds key-value pairs to the set edges
					
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

	def __find_ham(self):
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
	def edgeslist_from_path(self):
		edge_tup=[]
		m=0
		path_list=self.__find_ham()
		count=0
		values=self.__graph_dict.values()
		for val in values:
			if (val !=[]):
				count+=1 
		for i in path_list:
			edge_tup.append([])                           
			for j in range(0,count-1):
				edge_tup[m].append((i[j],i[j+1]))
			m+=1
		return edge_tup
			
		
		
if __name__ == "__main__": #EXP: refer: https://stackoverflow.com/questions/419163/what-does-if-name-main-do
	input_dict = raw_input("Input a dictonary in 'vertice : [all its neighbouring vertices]' form ")
	import ast
	import os
	g = ast.literal_eval(input_dict)	#EXP-converts string input to a dict 
	gobj = Graph(g)                                    #https://stackoverflow.com/questions/17264174/python-how-to-take-a-dictionary-as-input
	#print ('\n','All possible Ham paths between the cities:', '\n',gobj.edgeslist_from_path())
	nodes= gobj.vertices()
	#print('\n',nodes)
	x=0
	nodemap={}
	for i in nodes:
		nodemap[nodes[x]]=x
		x+=1
	print ('\n',(nodemap))
	graph={}
   
	for i in nodes:
		l=g[i]
		templist=[]
		for j in l:
			templist.append(nodemap[j])
		graph[nodemap[i]]=templist
	#print ('\n',(graph))
	
	temp_edges = list(gobj.edges())
	print (temp_edges)
	weights = raw_input("^These are the edges that have been identified in the graph. \n Please enter the weights of each edge in the same order in list format:")
	
	weights = ast.literal_eval(weights)
	#print ('\n', weights)

	weighted_edges = {}
	j = 0
	for i in weights:
		weighted_edges[temp_edges[j]] = i
		j+=1

	print ('\n', (weighted_edges))                                          #finding the shortest path in terms of edges using weights
	all_ham_paths_in_tupleformat=gobj.edgeslist_from_path()
	minsum=sum(weights)
	shortest_way_edges=list()
	for i in all_ham_paths_in_tupleformat:
		tempsum=0
		for j in i:
			tempsum=tempsum+weighted_edges[j]
		if (tempsum<minsum):
			minsum=tempsum
			shortest_way_edges=i
	print ('\n',"path which shall take the minimum amount to travel to all cities in terms of edges:",shortest_way_edges)
	shortest_way_vertices=[]
	for i in shortest_way_edges:                    #from shortest_way_edges to shortest_way in the form of vertices
		for j in i:
			if j not in shortest_way_vertices:
				shortest_way_vertices.append(j)
	print ('\n',"path which shall take the minimum amount to travel to all cities in terms of vertices:",shortest_way_vertices)

	#pygame code starts-
	path=[]
	for i in shortest_way_vertices:
		path.append(nodemap[i])
	print(path)
	import pygame
	import math
	pygame.init()
	red = (150,0,0)
	green = (0,255,0)
	blue = (0,0,255)
	darkBlue = (0,0,128)
	white = (255,255,255)
	black = (0,0,0)
	pink = (255,200,200)
	orange = (255,69,0)

	gameDisplay = pygame.display.set_mode((800,600))
	pygame.display.set_caption('TSP')
	myfont = pygame.font.SysFont("monospace", 20)
	myfont1 = pygame.font.SysFont("monospace", 15)
	pygame.time.Clock()

	pygame.display.update()

	gameExit = False

	for ham in range(len(path)-1):
	    tot = 10*(weighted_edges[shortest_way_edges[ham]])
	    legendx = 10
	    legendy = 10
	    for step in range(tot):
	        gameDisplay.fill(white)
	        for i in range(len(nodes)):
	            x = 400+(200*(math.cos((360*i)/(len(nodes)+1))))
	            y = 300+(200*(math.sin((360*i)/(len(nodes)+1))))
	            r= 157/len(nodes)
	            label = myfont.render(nodes[i], 2, darkBlue)
	            gameDisplay.blit(label, ((int(x)-2*int(r)),int(y)))
	            pygame.draw.circle(gameDisplay, red, (int(x),int(y)), int(r), 5)
	        for node in graph:
	            x = 400+(200*(math.cos((360*node)/(len(nodes)+1))))
	            y = 300+(200*(math.sin((360*node)/(len(nodes)+1))))
	            for neigh in range(len(graph[node])):
	                x1 = 400+(200*(math.cos((360*graph[node][neigh])/(len(nodes)+1))))
	                y1 = 300+(200*(math.sin((360*graph[node][neigh])/(len(nodes)+1))))
	                pygame.draw.lines(gameDisplay, black, False, [(x,y),(x1,y1)], 1)

	        x = 400+(200*(math.cos((360*path[ham])/(len(nodes)+1))))
	        y = 300+(200*(math.sin((360*path[ham])/(len(nodes)+1))))
	        x1 = 400+(200*(math.cos((360*path[ham+1])/(len(nodes)+1))))
	        y1 = 300+(200*(math.sin((360*path[ham+1])/(len(nodes)+1))))
	        x2 = ((step*x1)+((tot-step)*x))/tot
	        y2 = ((step*y1)+((tot-step)*y))/tot
	        r= 157/len(nodes)
	        pygame.time.delay(100)

	        gameDisplay.fill(green, rect = [(int(x2)-((int(r))/2)),(int(y2)-((int(r))/2)),int(r),int(r)])
	        
	        label = myfont1.render("Path", 2, blue)
	        gameDisplay.blit(label, (10, 10))
	        label = myfont1.render("Weight", 2, darkBlue)
	        gameDisplay.blit(label, (80, 10))

	        legendy = 10
	        legendx = 20
	            
	        for legend in range(len(temp_edges)):
	            legendy = legendy + 20;
	            label = myfont1.render(temp_edges[legend][0]+temp_edges[legend][1], 2, blue)
	            gameDisplay.blit(label, (legendx, legendy))
	            label = myfont1.render(str(weighted_edges[temp_edges[legend]]), 2, darkBlue)
	            gameDisplay.blit(label, (legendx+70, legendy))

	        pygame.display.update()
	            
	while not gameExit:
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            gameExit = True

	    gameDisplay.fill(white)
	    for i in range(len(nodes)):
	        x = 400+(200*(math.cos((360*i)/(len(nodes)+1))))
	        y = 300+(200*(math.sin((360*i)/(len(nodes)+1))))
	        r= 157/len(nodes)
	        label = myfont.render(nodes[i], 2, darkBlue)
	        gameDisplay.blit(label, ((int(x)-2*int(r)),int(y)))
	        pygame.draw.circle(gameDisplay, red, (int(x),int(y)), int(r), 5)
	        for node in graph:
	            x = 400+(200*(math.cos((360*node)/(len(nodes)+1))))
	            y = 300+(200*(math.sin((360*node)/(len(nodes)+1))))
	            for neigh in range(len(graph[node])):
	                x1 = 400+(200*(math.cos((360*graph[node][neigh])/(len(nodes)+1))))
	                y1 = 300+(200*(math.sin((360*graph[node][neigh])/(len(nodes)+1))))
	                pygame.draw.lines(gameDisplay, black, False, [(x,y),(x1,y1)], 1)

	    x = 400+(200*(math.cos((360*path[len(path)-1])/(len(nodes)+1))))
	    y = 300+(200*(math.sin((360*path[len(path)-1])/(len(nodes)+1))))
	    r= 157/len(nodes)
	    pygame.time.delay(500)

	    gameDisplay.fill(green, rect = [(int(x)-((int(r))/2)),(int(y)-((int(r))/2)),int(r),int(r)])

	    label = myfont1.render("Path", 2, orange)
	    gameDisplay.blit(label, (10, 10))
	    label = myfont1.render("Weight", 2, orange)
	    gameDisplay.blit(label, (80, 10))

	    legendy = 10
	    legendx = 20
	            
	    for legend in range(len(temp_edges)):
	        legendy = legendy + 20;
	        label = myfont1.render(temp_edges[legend][0]+temp_edges[legend][1], 2, blue)
	        gameDisplay.blit(label, (legendx, legendy))
	        label = myfont1.render(str(weighted_edges[temp_edges[legend]]), 2, darkBlue)
	        gameDisplay.blit(label, (legendx+70, legendy))
	    
	    pygame.display.update()
	    
	pygame.quit()
	quit()

		
'''
#readymade input:		g = { "a" : ["d","e"],"b" : ["c","d"],"c" : ["b", "d", "e"],"d" : ["a","b", "c"],"e" : ["c","a"],"f" : []}
'''#[1,2,3,4,5,3,6,5,2,1,6,4]
# { "agra" : ["delhi","bombay"],"bombay" : ["agra","chennai","delhi"],"chennai" : ["delhi","bombay"],"delhi":["agra","bombay","chennai"] }
