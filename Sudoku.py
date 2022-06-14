import copy
import numpy as np
class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent


def goalCheck(node):
    check = True
    value = node.value
    cell = set([])
    for i in range(len(value)):
        row = set([])
        for j in range((len(value[i]))):
            if value[i][j] == 0:
                check = False
                return(check) 
            row.add(value[i][j])
            #print(row)
        if row != {1,2,3,4}:
            check = False
            return(check) 
              
    for j in range((len(value))):
        column = set([])
        for i in range((len(value[j]))):
            column.add(value[i][j])
            #print(column,"-------------")
        if column != {1,2,3,4}:
            check = False
            return(check) 
    
    
    for n in [0,2]:
        cell = set([])
        for i in [0+n,1+n]:
            for j in [0,1]:
                cell.add(value[i][j])
                #print(cell,"++++++++++++++")
        if cell != {1,2,3,4}:
            check = False
            return(check)
        
    for n in [0,2]:
        cell = set([])
        for j in [0+n,1+n]:
            for i in [0,1]:
                cell.add(value[i][j])
                #print(cell,"777777777777777777777777")
        if cell != {1,2,3,4}:
            check = False
            return(check)
        
    return(check)


def oneNumberStep(node):
    value = node.value
    blank = []
    while not goalCheck(node):
        cellChange = 0
        for i in range(4):
            for j in range(4):
                if value[i][j] ==0:
                    blank = [i,j]
                    possibleNumber ={1,2,3,4}
                    for a in range(4):
                        if value[i][a] in possibleNumber:
                            possibleNumber.remove(value[i][a])
                        if value[a][j] in possibleNumber:
                            possibleNumber.remove(value[a][j])
                    
                    position = []
                    for a in blank:
                        if a == 0 or a == 2:
                            position.append(a+1)
                        else:
                            position.append(a-1)
                
                    if value[position[0]][blank[1]] in possibleNumber:
                        possibleNumber.remove(value[position[0]][blank[1]])
                    if value[blank[0]][position[1]] in possibleNumber:
                        possibleNumber.remove(value[blank[0]][position[1]])
                    if value[position[0]][position[1]] in possibleNumber:
                        possibleNumber.remove(value[position[0]][position[1]])
                
                    if len(possibleNumber) == 1:
                        possiblelist = list(possibleNumber)
                        value[i][j] = possiblelist[0]
                        cellChange = cellChange +1
        if cellChange == 0 :
            print("Can not add number")
            break
                    
    return(Node(value, None))


def addNumber(node, number, cell):
    value = copy.deepcopy(node.value)
    i = cell[0]
    j = cell[1]
    
    value[i][j] = number
    
    child = None
    if value != None:
        child = Node(value, node)
    return(child)



numberList = [1,2,3,4]
blankCell = []

def expand(node):
    listNextNode = []
    currentBlankCell = copy.copy(blankCell)
    currentNumberList = copy.copy(numberList)
    
    for num in currentNumberList:
        for cell in currentBlankCell:
            i = cell[0]
            j = cell[1]
            if node.value[i][j] != 0:
                break
            if node.value[0][j] == num or node.value[1][j] == num or node.value[2][j] == num or node.value[3][j] == num :
                continue
            if node.value[i][0] == num or node.value[i][1] == num or node.value[i][2] == num or node.value[i][3] == num :
                continue
            # for a in range(4):
            #     if node.value[i][a] == num :       
            #         continue
            #     if node.value[a][j] == num :
            #         continue
            child = addNumber(node, num, cell)
            if child != None:
                listNextNode.append(child)
    
    return(listNextNode)



def printsolution(solution):
    for node in solution:
        print(np.array(node.value),'\n')

def solve(initial):
    frontier = [initial]
    visited = []
    solution = []
    
    value = [initial].pop(0).value
    for i in range(4):
        for j in range(4):
            if value[i][j] == 0:
                blankCell.append([i,j])
    
    while True:
        if len(frontier) == 0:
            break
        else:
            # get one node out of the frontier
            node = frontier.pop(0)
            if goalCheck(node):
                path = [node]
                while node.parent != None :
                    path.insert(0, node.parent)
                    node = node.parent
                solution = path
                break
            else:
                # avoid loop
                newNodes = expand(node)
                for newNode in newNodes:
                    repeat = False
                    for oldNode in visited:
                        if newNode.value == oldNode.value:
                            repeat = True
                    if not repeat:
                        frontier.append(newNode)
                        visited.append(newNode)

    return(solution)

def solveWithStepOne(initial):
    newNode = oneNumberStep([initial].pop(0))
    newValue = [newNode].pop(0).value
    
    
    print(newValue,"======")
    solution = solve(newNode)
    
    return(solution)

startNode = Node([[4,0,0,3],[1,0,0,4],[0,0,0,2],[0,0,0,1]], None)
# solution = solveWithStepOne(startNode)
solutionII = solve(startNode)


printsolution(solutionII)
