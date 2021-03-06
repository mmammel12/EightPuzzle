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
        # update open and close lists
        currentNode = openList.pop(0)
        closedList.append(currentNode)
        # generate child board states and check for goal
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
        print("Nodes Checked: {}".format(len(closedList)))
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
            # calculate f-score to decide which node to check
            if node.parent is not None:
                if node.fScore is None:
                    node.setFScore(calcFScore(node))
                if node.fScore < minFScore:
                    currentNode = node
                    minFScore = node.fScore
        # update open and closed lists
        openList.remove(currentNode)
        closedList.append(currentNode)
        # generate child board states and check for goal
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
        print("Nodes Checked: {}".format(len(closedList)))
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
    # climb up the tree to find full path
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
    print("\nBFS took: {:.4f} seconds\n".format(endTime - startTime))


def runAStar(root):
    print("\nRunning A*")
    startTime = time.time()
    A_Star(root)
    endTime = time.time()
    print("\nA* took: {:.4f} seconds\n".format(endTime - startTime))


def printBoard(board):
    colSize = int(math.sqrt(len(board)))
    boardStr = ""
    # print board as a matrix instead of one dimensional list
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
        board = [2, 5, 3, 1, 6, 0, 4, 7, 8]
        print("Board 1:\n")
        printBoard(board)
        root = Node.Node(board)
        root.setFScore(0)

        runBFS(root)
        runAStar(root)

        board = [1, 6, 2, 7, 4, 3, 5, 0, 8]
        print("----------------------------")
        print("Board 2:\n")
        printBoard(board)
        root = Node.Node(board)
        root.setFScore(0)

        runBFS(root)
        runAStar(root)

        board = [0, 3, 6, 1, 5, 8, 4, 2, 7]
        print("----------------------------")
        print("Board 3:\n")
        printBoard(board)
        root = Node.Node(board)
        root.setFScore(0)

        runBFS(root)
        runAStar(root)
    else:
        print("Board size must be a square number")


if __name__ == "__main__":
    main()
