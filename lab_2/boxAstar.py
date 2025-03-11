from itertools import product
import time
import copy
def getindex(matrix,element):
    for i,j in product(range(3),range(3)):
        if matrix[i][j]==element:
            return i,j
        
        
def inputbox():
    matrix=[]
    for i in range (0,3):
        rows=[]
        for j in range(0,3):
            element=int(input(f"please enter the [{i}][{j}] elements"))
            rows.append(element)
        matrix.append(rows)
    return matrix
def legalMoves(matrix):
    for i ,row in enumerate(matrix):
        for j,cols in enumerate(row):
            if cols==0:
                x=i
                y=j
                index=(x,y)
                break
    possible_moves=[(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
    allowedMoves=[]
    for i in possible_moves:
        if i[0]<3 and i[1]<3 and i[0]>=0 and i[1]>=0:
            allowedMoves.append(i)
    return allowedMoves,index

def bestMoves(gn,nextmoves,goalstate,visitedState):
    hn=float('inf')
    state=None
    for moves in nextmoves:
        h,h1,h2=0,0,0
        for i ,j in product(range(3),range(3)):
            if moves[i][j]!=goalstate[i][j]:
                h+=1
        h1=h
        for rows in moves:
            for elements in rows:
                igoal,jgoal=getindex(goalstate,elements)
                icurent,jcurent=getindex(moves,elements)
                h2=abs(igoal-icurent)+abs(jgoal-jcurent)
        fn=h1+h2+gn
        if fn<hn and moves not in visitedState:
            state=moves
            hn=h1+h2
    gn+=1
    return gn,state
                    

def nextState(nexto,currentState,emptyIndex):
    possibleMatrix=[]
    for matrix in nexto:
        temp=copy.deepcopy(currentState)
        temp[emptyIndex[0]][emptyIndex[1]]=temp[matrix[0]][matrix[1]]
        temp[matrix[0]][matrix[1]]=0
        possibleMatrix.append(temp)
    return possibleMatrix
        
def Astar(start,goal):
    visitedState=[]
    gn=0
    currentState=start
    while currentState!=goal:
        visitedState.append(currentState)
        for i in currentState:
            print(i)
        print("***********")
        nexto,emptyIndex=legalMoves(currentState)
        print(nexto)
        possibleNextState=nextState(nexto,currentState,emptyIndex)
        fn,bestMove=bestMoves(gn,possibleNextState,goal,visitedState)
        currentState=bestMove
        gn=fn
    print(f"goal found and cost is {gn}")
if __name__=="__main__":
    print("Please enter the start state")   
    start=inputbox()
    print("Please enter goal state")
    goal=inputbox()
    Astar(start,goal)