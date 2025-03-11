import time
G= {
    "Biratnagar": {"Itahari": 22, "Biratchowk": 30, "Rangeli": 25},
    "Itahari": {"Biratnagar": 22, "Biratchowk": 11, "Dharan": 20},
    "Rangeli": {"Kanepokhari": 25, "Biratnagar": 25,"Urlabari":40},
    "Biratchowk": {"Itahari": 11, "Biratnagar": 30, "Kanepokhari": 10},
    "Dharan": {"Itahari": 20},
    "Kanepokhari": {"Rangeli": 25, "Biratchowk": 10, "Urlabari": 12},
    "Urlabari": {"Rangeli": 40, "Kanepokhari": 12, "Damak": 6},
    "Damak": {"Urlabari": 6},
}

h= {
    "Biratnagar" : 46, "Itahari": 39, "Dharan": 41, "Rangeli": 28, "Biratchowk":29,
      "Kanepokhari":17, "Urlabari":6, "Damak":0,
}

def Astar(start,goal,G,H):
    prev={start:None}
    currentState=start
    minCost=0
    visited=set()
    while currentState!=goal:
        nextState=None
        visited.add(currentState)
        mindis=float('inf')
        stat=0
        for neighbours in G[currentState]:
            if neighbours not in visited:
                fn=(H[neighbours])+G[currentState][neighbours]
                if mindis>fn:
                    mindis=fn
                    nextState=neighbours
                    stat=1
        if nextState==None or stat==0:
            return False,prev,minCost
        minCost+=G[currentState][nextState]
        prev[nextState]=currentState
        currentState=nextState
    return True,prev,minCost

def constructPath(start,goal,path):
    track=[]
    currensState=goal
    while currensState is not None:
        track.append(currensState)
        currensState=path[currensState]
    c=""
    for el in track:
        c="->"+el+c
    return c
   
start=input("please enter the start state")     
goal=input("plese enter the goal state")   
sol,path,cost=Astar(start,goal,G,h)
if sol==True:
   print(constructPath(start,goal,path))
   print(f"The minimum cost is: {cost}")
else:
    print("soln not found")
     