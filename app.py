vertices = 4
infinite  = 9999
  

grafo = [[0,3,infinite,7], 
             [8,0,2,infinite], 
             [5,infinite,0,1], 
             [2,infinite,infinite,0],
        ] 

selectVertex=int(input("Number of vertex:"))

##Algoritm of Floyd
for k in range(selectVertex): 
    for i in range(vertices): 
        for j in range(vertices): 
            grafo[i][j] = min(grafo[i][j] , grafo[i][k]+ grafo[k][j]) 


## Define constant
i=0
j=0
infinite=999 ## infinite

armTamanho = "" ##Concatenate on string

##Print graph
print("\nBest route:")
for i in range(vertices): 
    for j in range(vertices): 
        if(grafo[i][j] > infinite): 
            armTamanho+="∞" + " "
        else: 
            armTamanho+=str(grafo[i][j]) + " "
        if j == vertices-1: 
            print(armTamanho+"\n")
            armTamanho=""

input("Press enter for exit...")
