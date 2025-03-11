G = {
    "Biratnagar": {"Itahari": 22, "Biratchowk": 30, "Rangeli": 25},
    "Itahari": {"Biratnagar": 22, "Biratchowk": 11, "Dharan": 20},
    "Rangeli": {"Kanepokhari": 25, "Biratnagar": 25},
    "Biratchowk": {"Itahari": 11, "Biratnagar": 30, "Kanepokhari": 10},
    "Dharan": {"Itahari": 20},
    "Kanepokhari": {"Rangeli": 25, "Biratchowk": 10, "Urlabari": 12},
    "Urlabari": {"Rangeli": 40, "Kanepokhari": 12, "Damak": 6},
    "Damak": {"Urlabari": 6},
}
from queue import Queue
def BFS(start,goal,G):
    frontier=Queue()
    visited=set()
    prev=dict()
    prev[start]=None
    frontier.put(start)
    while not frontier.empty():
        current_state=frontier.get()
        if current_state==goal:
            return True,prev
        if current_state not in visited:
            visited.add(current_state)
            for neighbours in G[current_state]:
                if neighbours not in visited:
                    frontier.put(neighbours)
                    if neighbours not in prev:
                        prev[neighbours]=current_state
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
sol,path=BFS(start,goal,G)
if sol==True:
   print(constructPath(start,goal,path))
else:
    print("soln not found")
     
        
        
