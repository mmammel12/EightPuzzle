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
            print()
            board.printBoard()
    else:
        print("\nNo solution found\n")


def getGoalPath(goalNode):
    currentNode = goalNode
    nodes = [goalNode]
    while currentNode.hasParent():
        currentNode = currentNode.parent
        nodes.append(currentNode)
    return nodes


def main():
    boardSize = 9
    # If boardSize comes from user input it needs to be checked to see if it is square
    if math.sqrt(boardSize).is_integer():
        colSize = int(math.sqrt(boardSize))
        # the following three boards run in a reasonable time for BFS
        # board = [2, 5, 3, 1, 6, 0, 4, 7, 8]
        # board = [1, 6, 2, 7, 4, 3, 5, 0, 8]
        board = [0, 3, 6, 1, 5, 8, 4, 2, 7]
        npBoard = array(board).reshape((colSize, colSize))
        print("Initial Board:")
        print(npBoard)
        print()
        root = Node.Node(board)
        print("Running BFS")
        startTime = time.time()
        BFS(root)
        endTime = time.time()
        elapsedTime = endTime - startTime
        print("\nBFS took: {:.2f} seconds".format(elapsedTime))
    else:
        print("Board size must be a square number")


if __name__ == "__main__":
    main()
