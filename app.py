vertices = 5
infinite  = 9999
  

grafo = [[0,1,1,0,1], 
             [1,0,1,1,0], 
             [1,1,0,1,1], 
             [0,1,1,0,0],
             [1,0,1,0,0]
        ] 

##Algoritm of Floyd
for k in range(vertices): 
    for i in range(vertices): 
        for j in range(vertices): 
            grafo[i][j] = min(grafo[i][j] , grafo[i][k]+ grafo[k][j]) 

## Define constant
i=0
j=0
infinite=999999 ## infinite

armTamanho = "" ##Concatenate on string

##Print graph
print("Best route:")
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
