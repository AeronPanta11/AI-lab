from queue import PriorityQueue
import pprint

dict_graph = {
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

def aStar(dict_graph, h, start, goal):
    PQ = PriorityQueue()
    prev = dict()
    visited = set()

    PQ.put((0+h[start], (start,0)))
    
    prev[start] = " "

    while(PQ.empty() == False):
        outStateFScore,( outState, outStateGScore) = PQ.get()
        visited.add(outState)
        if outState == goal:
            return True, prev, outStateFScore
        for chimeki in dict_graph[outState]:
            if chimeki not in visited:
                chimekiGScore = outStateGScore + dict_graph[outState][chimeki]
                PQ.put((chimekiGScore+h[chimeki], (chimeki, chimekiGScore)))
                prev[chimeki] = outState
    return False, prev

def reconstruct_path(dict_graph, prev, goal):
    path = goal
    while previous[goal] != " ":
        path = previous[goal] + " -> " + path
        goal = previous[goal]
    return path  

start=input("please enter the start state")     
goal=input("plese enter the goal state")   
goalFound, previous, goalFScore = aStar(dict_graph,h, start, goal)
if(goalFound):
    pprint.pprint(reconstruct_path(dict_graph,previous,goal))
    print(goalFScore)
else:
    pprint.pprint("No solution")