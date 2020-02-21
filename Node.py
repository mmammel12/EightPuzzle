import math
from numpy import array, reshape


class Node:
    def __init__(self, board, parent=None, depth=0):
        super().__init__()
        self.children = []
        self.parent = parent
        self.board = board.copy()
        self.colSize = int(math.sqrt(len(board)))
        self.depth = depth
        self.fScore = 0

    def __eq__(self, value):
        # overload equality operator
        return self.board == value.board

    def setFScore(self, fScore):
        self.fScore = fScore

    def expandNode(self):
        # find zero index
        zeroIndex = -1
        for i, value in enumerate(self.board):
            if value == 0:
                zeroIndex = i
                break
        # expand all possible moves from current board state
        self.moveLeft(zeroIndex)
        self.moveRight(zeroIndex)
        self.moveUp(zeroIndex)
        self.moveDown(zeroIndex)

    def _createChild(self, board):
        # create child node with new board state
        child = Node(board, self, self.depth + 1)
        self.children.append(child)

    def moveLeft(self, index):
        # move left
        if index % self.colSize > 0:
            # element can move left
            newBoard = self.board.copy()
            newBoard[index], newBoard[index - 1] = (
                newBoard[index - 1],
                newBoard[index],
            )
            self._createChild(newBoard)

    def moveRight(self, index):
        # move right
        if index % self.colSize < self.colSize - 1:
            # element can move right
            newBoard = self.board.copy()
            newBoard[index], newBoard[index + 1] = (
                newBoard[index + 1],
                newBoard[index],
            )
            self._createChild(newBoard)

    def moveUp(self, index):
        # move up
        if index - self.colSize >= 0:
            # element can move up
            newBoard = self.board.copy()
            newBoard[index], newBoard[index - self.colSize] = (
                newBoard[index - self.colSize],
                newBoard[index],
            )
            self._createChild(newBoard)

    def moveDown(self, index):
        # move down
        if index + self.colSize < len(self.board):
            # element can move down
            newBoard = self.board.copy()
            newBoard[index], newBoard[index + self.colSize] = (
                newBoard[index + self.colSize],
                newBoard[index],
            )
            self._createChild(newBoard)

    def isGoal(self):
        # check for goal state
        isGoal = True
        for i, value in enumerate(self.board):
            if i < len(self.board) - 1:
                # check for [1,2,3...] to one before end
                if value != i + 1:
                    isGoal = False
                    break
            else:
                # final value should be 0
                if value != 0:
                    isGoal = False

        return isGoal

    def hasParent(self):
        return self.parent is not None

    def printBoard(self):
        # using numpy to reshape and print the board
        npBoard = array(self.board).reshape((self.colSize, self.colSize))
        print(npBoard)
