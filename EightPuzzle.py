import Node
import math
import random
import time
from numpy import array, reshape


def BFS(root):
    solutionPath = []
    openList = []
    closedList = []

    openList.append(root)
    keepGoing = True
    if root.isGoal():
        keepGoing = False
        solutionPath.append(root)

    while keepGoing:
        currentNode = openList.pop(0)
        closedList.append(currentNode)
        # expand all moves for current node
        currentNode.expandNode()
        # check if one of the children is the goal state
        for child in currentNode.children:
            if child.isGoal():
                keepGoing = False
                solutionPath = getGoalPath(child)
            if child not in openList and child not in closedList:
                openList.append(child)
        if len(openList) == 0:
            keepGoing = False

    if len(solutionPath) > 0:
        for board in solutionPath:
            board.printBoard()
    else:
        print("\nNo solution found\n")


def getGoalPath(goalNode):
    currentNode = goalNode
    nodes = [goalNode]
    while currentNode.parent != None:
        currentNode = currentNode.parent
        nodes.append(currentNode)
    return nodes.reverse()


def main():
    boardSize = 9
    if math.sqrt(boardSize).is_integer():
        colSize = int(math.sqrt(boardSize))
        board = []
        for i in range(boardSize):
            board.append(i)
        random.shuffle(board)
        npBoard = array(board).reshape((colSize, colSize))
        print("Initial Board:")
        print(npBoard)
        print()
        root = Node.Node(board)
        print("Running BFS")
        startTime = time.time()
        BFS(root)
        endTime = time.time()
        print("BFS took: " + (endTime - startTime) + " seconds")
    else:
        print("Board size must be a square number")
    input()


if __name__ == "__main__":
    main()

