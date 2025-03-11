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

def DFS(start,goal,graph):
    fountier=[start]
    visited=set()
    prev=dict()
    prev[start]=None
    while fountier:
        current_state=fountier.pop()
        if current_state==goal:
            return True , prev
        if current_state not in visited:
            visited.add(current_state)
            for neighbours in graph[current_state]:
                if neighbours not in visited:
                    fountier.append(neighbours)
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
sol,path=DFS(start,goal,G)
if sol==True:
   print(constructPath(start,goal,path))
else:
    print("soln not found")
