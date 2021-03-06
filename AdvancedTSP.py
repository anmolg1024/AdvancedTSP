"""
The following code takes a graph as an input in the form a dictionary whose keys are the vertices and the values are the corresponding neighboring vertices
It identifies the edges in the graph, and subsequently asks for the respective weights of each.
On inputting the edges, it finds all the possible Hamiltonian paths in the code, and then chooses the smallest one of them.
"""
class Graph(object):

    def __init__(self, graph_dict=None): #used to initiate the graph as list of source vertex : target vertices
        #initializes a graph object. If no dictionary or None is given, an empty dictionary will be used
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self): #returns the vertices of a graph in a list
        return sorted(list(self.__graph_dict.keys()))

    def edges(self): #returns the edges of a graph in the form of tuples
        return self.__generate_edges()  #will be defining a method later for this

    def add_vertex(self, vertex):
        #If the vertex "vertex" is not in self.__graph_dict, a key "vertex" with an empty list as a value is added to the dictionary. Otherwise nothing has to be done
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = [] #EXP: puts a key in the dictionary with an empty set of values    
    def add_edge(self, edge): #assumes that edge is of type set, tuple or list; between two vertices can be multiple edges
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge) #refers to the edge's member conveniently through vertex1 and vertex2
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2) #EXP: adds vertex2 as the second vertex of the edge to the dictionary's key's value
        else:
            self.__graph_dict[vertex1] = [vertex2] 
        
    def __generate_edges(self):
        #A static method generating the edges of the graph "graph". Edges are represented as sets with one (a loop back to the vertex) or two vertices
            edges = [] #defines an empty array to display
            for vertex in self.__graph_dict: #refer: http://www.techeuler.com/python/usage-of-underscores-before-and-after-function-name-in-python/
                for neighbour in self.__graph_dict[vertex]:
                    edges.append((vertex, neighbour)) #EXP: simply adds key-value pairs to the set edges
            return edges

    def __str__(self): #simply returns all the vertices in one line and the edges in another line 
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
    
#EXP: The following method finds a path from a start vertex to an end vertex, through the Depth First Search Algorithm 
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
                if extended_path: #EXP: whenever none is returned it takes extended path as 0 and when the p is returned, it will take the non empty list as it as '1'
                    return extended_path
        return None

    def __find_all_paths(self, start, end, path=[]):        #same algo as the previous function except this fuctions returns back all the possible path between a pair of cities
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
                for newpath in newpaths:                            #the paths are stored in a list here
                    paths.append(newpath)
        return paths

    def __find_ham(self):       #finds all ham-paths possible between every combination of connected cities
        count=0
        vertices=self.vertices()
        values=self.__graph_dict.values()
        for val in values:
            if (val !=[]):
                count+=1                #counts the no. of cities which has a road connected with them, basically all except the empty nodes
        ham_paths=[]
        for start in vertices:
            for end in vertices:
                if start!=end:
                    allpaths=self.__find_all_paths(start,end)
                    for path in allpaths:
                        if len(path)==count:                #out of all ham paths computed by the find_all_paths function it considers only those which allows the postman to cover every city he needs to travle to.
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
    input_dict = raw_input("Enter the locations of the city to be visited in graph format as '{vertice : [all its neighbouring vertices]}' form" + '\n')
    import ast
    import os
    g = ast.literal_eval(input_dict)    #EXP-converts string input to a dict 
    gobj = Graph(g)                                    #https://stackoverflow.com/questions/17264174/python-how-to-take-a-dictionary-as-input
    #print ('\n','All possible Ham paths between the cities:', '\n',gobj.edgeslist_from_path())
    nodes= gobj.vertices()
    #print('\n',nodes)
    x=0
    nodemap={}
    for i in nodes:             
        nodemap[nodes[x]]=x     #assigning whole no.s starting from 0 to the node to be used later in pygame
        x+=1
    #print (nodemap)
    graph={}
   
    for i in nodes:
        l=g[i]
        templist=[]
        for j in l:
            templist.append(nodemap[j])         #changing the representation of the graph using the number's assigned to the nodes
        graph[nodemap[i]]=templist
    #print (graph)
    
    temp_edges = list(gobj.edges())
    print ("These are the paths that have been identified in the city:")
    print (temp_edges)
    weights = raw_input("Please enter the length of each path in the same order in list format:" + '\n')
    
    weights = ast.literal_eval(weights)  #makes the input accessible as a list item
    #print ('\n', weights)

    weighted_edges = {}
    j = 0
    for i in weights:
        weighted_edges[temp_edges[j]] = i       #mapping the weights with their respective edges
        j+=1

    print ("These are the assigned lengths of each path:")
    print (weighted_edges)                                          
    
    speed = raw_input("Enter the average speed of the salesman:" + '\n') #used to calculate time taken
    speed = float(speed)
   # total_distance = 0
    #for i in weights:
     #   total_distance += i

    all_ham_paths_in_tupleformat=gobj.edgeslist_from_path() #finding the shortest path in terms of edges using weights
    minsum=sum(weights) #takes a sum of the items in the weights list to calculate total distance in the city
    shortest_way_edges=list()
    for i in all_ham_paths_in_tupleformat:
        tempsum=0
        for j in i:
            tempsum=tempsum+weighted_edges[j]
        if (tempsum<minsum): #algorithm that finds the smallest path
            minsum=tempsum
            shortest_way_edges=i

    #print (minsum)
    total_distance = float(minsum)
    time_taken = total_distance/speed

    mileage = raw_input("Enter the average mileage of the salesman's car in km/litre:" + '\n')
    mileage = float(mileage)

    fuel_consumed = total_distance/mileage
    
    cities_time = raw_input("Enter the time spent by the salesman at each destination in list format:" + '\n')
    cities_time = ast.literal_eval(cities_time) 
    #print (cities_time)
    for i in cities_time:
        time_taken += i #in order to find the total time taken in the day job

    print ("The path which shall take the minimum amount of time to travel to all locations (in terms of paths):")
    print (shortest_way_edges)          #the final path in terms of edges
    
    #print (time_taken) 
    print 'The time taken by the salesman for his job will be: %f hours.' % time_taken

    print 'The fuel consumed during the job is %f litres.' % fuel_consumed

    shortest_way_vertices=[]
    for i in shortest_way_edges:                    #from shortest_way_edges to shortest_way in the form of vertices
        for j in i:
            if j not in shortest_way_vertices:
                shortest_way_vertices.append(j)
   #print ("The path which shall take the minimum amount of time to travel to all cities (in terms of cities):")
 #   print (shortest_way_vertices)

    #pygame code starts-
    path=[]
    for i in shortest_way_vertices:
        path.append(nodemap[i])             #changing the represention of path by using the alloted numbers instead of alphabetical nodes.
    #print(path)
        
'''
#readymade input:       g = { "a" : ["d","e"],"b" : ["c","d"],"c" : ["b", "d", "e"],"d" : ["a","b", "c"],"e" : ["c","a"],"f" : []}
'''#[1,2,3,4,5,3,6,5,2,1,6,4]
# { "agra" : ["delhi","bombay"],"bombay" : ["agra","chennai","delhi"],"chennai" : ["delhi","bombay"],"delhi":["agra","bombay","chennai"] }

# Start of Pygame code
import pygame
import math
start_pygame = raw_input("Do you want to start Pygame? Type 'Y' for yes, and 'N' for no:" + '\n')
start_pygame = str(start_pygame)
if start_pygame == 'Y':
    pygame.init()

#Defines colors
red = (150,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
orange = (255,69,0)

#Initialising pygame and setting the fonts, etc.
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('TSP')
myfont = pygame.font.SysFont("monospace", 20)
myfont1 = pygame.font.SysFont("monospace", 15)
pygame.time.Clock()
postmanImage = pygame.image.load("post.png").convert()

pygame.display.update()

gameExit = False
"""
The following loops create the frames at every clock tick, and keep updating the coordinates to make the postman traverse the hamiltonian path.
The inputs to this are the Hamiltonian path, and the weight of each edge in the path.
The speed of the postman varies accordinng to the weight of the path, more the weight less the speed.
"""
for ham in range(len(path)-1):  #this outer loop goes over every node in the hamiltonan path
    tot = 10*(weighted_edges[shortest_way_edges[ham]]) # this is the number of intervals that each weighted edges is to be divided into so that we get more steps(more time to travel) for a heavy weighted path
    legendx = 10    #x and y coordinates of the legend at the top left corner of the screen which lists out the weights of the paths
    legendy = 10
    pygame.time.delay(500)
    for step in range(tot):
        gameDisplay.fill(white)
        for i in range(len(nodes)): #this loop displays the nodes in a circular fasion and draws a circle at every vertex of the graph
            x = 400+(200*(math.cos((360*i)/(len(nodes)+1))))
            y = 300+(200*(math.sin((360*i)/(len(nodes)+1))))
            r= 157/len(nodes)
            label = myfont.render(nodes[i], 2, darkBlue)
            gameDisplay.blit(label, ((int(x)-2*int(r)),int(y)))     #command to display the name of the vertex next to each circle created
            pygame.draw.circle(gameDisplay, red, (int(x),int(y)), int(r), 5)
        for node in graph:      #this loop draws edges between the relevant vertices, as specified by the user
            x = 400+(200*(math.cos((360*node)/(len(nodes)+1))))
            y = 300+(200*(math.sin((360*node)/(len(nodes)+1))))
            for neigh in range(len(graph[node])):
                x1 = 400+(200*(math.cos((360*graph[node][neigh])/(len(nodes)+1))))
                y1 = 300+(200*(math.sin((360*graph[node][neigh])/(len(nodes)+1))))
                pygame.draw.lines(gameDisplay, black, False, [(x,y),(x1,y1)], 1)

        x = 400+(200*(math.cos((360*path[ham])/(len(nodes)+1))))       #calculates the cordinates that the postman needs to follow on the edges using the ratio formula of a line where it divides the line into 'tot' number of intervals
        y = 300+(200*(math.sin((360*path[ham])/(len(nodes)+1))))
        x1 = 400+(200*(math.cos((360*path[ham+1])/(len(nodes)+1))))
        y1 = 300+(200*(math.sin((360*path[ham+1])/(len(nodes)+1))))
        x2 = ((step*x1)+((tot-step)*x))/tot
        y2 = ((step*y1)+((tot-step)*y))/tot
        r= 157/len(nodes)
        pygame.time.delay(100)  #delays the postman by 100 ms after every step he takes

        gameDisplay.blit(postmanImage, ((int(x2)-((int(r))/2)),(int(y2)-((int(r))/2)-10)))  #command to display the image of the postman at the coordinates at calculated above        
        
        label = myfont1.render("Path", 2, blue)     #displayes the legend at the top left corner
        gameDisplay.blit(label, (10, 10))
        label = myfont1.render("Weight", 2, darkBlue)
        gameDisplay.blit(label, (80, 10))

        legendy = 10
        legendx = 20
            
        for legend in range(len(temp_edges)):      #takes the edges from the temp_edges and displays it at the coordinates of the legend
            legendy = legendy + 20;
            label = myfont1.render(temp_edges[legend][0]+temp_edges[legend][1], 2, blue)
            gameDisplay.blit(label, (legendx, legendy))
            label = myfont1.render(str(weighted_edges[temp_edges[legend]]), 2, darkBlue)
            gameDisplay.blit(label, (legendx+70, legendy))

        pygame.display.update()     #this updates the display at the end of every iteration so we can see the postman moving
            
while not gameExit: #till the window is not closed display the end frame of the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill(white)     #this just displayes the end frame of the game.
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

    gameDisplay.blit(postmanImage, ((int(x2)-((int(r))/2)),(int(y2)-((int(r))/2)-10)))

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
