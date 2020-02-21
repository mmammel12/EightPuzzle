import Node
import math
import random
import time


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


def A_Star(root):
    solutionPath = []
    openList = []
    closedList = []

    keepGoing = True

    if root.isGoal():
        keepGoing = False
        solutionPath.append(root)

    currentNode = root
    openList.append(currentNode)

    while keepGoing:
        minFScore = 10000
        for node in openList:
            if node.parent is not None:
                node.setFScore(calcFScore(node))
                if node.fScore < minFScore:
                    currentNode = node
                    minFScore = node.fScore

        openList.remove(currentNode)
        closedList.append(currentNode)

        # expand all moves for current node
        currentNode.expandNode()
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


def calcFScore(node):
    misplaced = 0
    fScore = 0
    for i, value in enumerate(node.board):
        # count misplaced tiles
        if value != 0:
            # 0 tile does not count
            if value != i + 1:
                misplaced += 1
    fScore = misplaced + node.depth
    return fScore


def getGoalPath(goalNode):
    currentNode = goalNode
    nodes = [goalNode]
    while currentNode.hasParent():
        currentNode = currentNode.parent
        nodes.append(currentNode)
    return nodes


def runBFS(root):
    print("\nRunning BFS")
    startTime = time.time()
    BFS(root)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print("\nBFS took: {:.4f} seconds\n".format(elapsedTime))


def runAStar(root):
    print("\nRunning A*")
    startTime = time.time()
    A_Star(root)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print("\nA* took: {:.4f} seconds\n".format(elapsedTime))


def printBoard(board):
    colSize = int(math.sqrt(len(board)))
    boardStr = ""
    for i in range(colSize):
        boardStr += "[ "
        for j in range(colSize):
            boardStr += "{} ".format(board[colSize * i + j])
        boardStr += "]\n"

    print(boardStr)


def main():
    boardSize = 9
    # if boardSize comes from user input it needs to be checked to see if it is square
    if math.sqrt(boardSize).is_integer():
        # the following three boards run in a reasonable time for BFS
        board = [2, 5, 3, 1, 6, 0, 4, 7, 8]
        print("Board 1:\n")
        printBoard(board)
        root = Node.Node(board)

        runBFS(root)
        runAStar(root)

        board = [1, 6, 2, 7, 4, 3, 5, 0, 8]
        print("----------------------------")
        print("Board 2:\n")
        printBoard(board)
        root = Node.Node(board)

        runBFS(root)
        runAStar(root)

        board = [0, 3, 6, 1, 5, 8, 4, 2, 7]
        print("----------------------------")
        print("Board 3:\n")
        printBoard(board)
        root = Node.Node(board)

        runBFS(root)
        runAStar(root)
    else:
        print("Board size must be a square number")


if __name__ == "__main__":
    main()
