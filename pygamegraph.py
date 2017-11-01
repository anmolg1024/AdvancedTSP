import pygame
import math
pygame.init()

nodes = ['a','b','c','d','e','f']
graph = {0:[1], 1:[2], 2:[4,5], 3:[4], 4:[5]}
path = [0,1,2,5,4,3]
red = (150,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
tot = 10

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('TSP')
myfont = pygame.font.SysFont("monospace", 20)
pygame.time.Clock()

pygame.display.update()

gameExit = False

for ham in range(len(path)-1):
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
        pygame.draw.circle(gameDisplay, (255-(20*i),0,0), (int(x),int(y)), int(r), 5)
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
    
    pygame.display.update()
    
pygame.quit()
quit()
