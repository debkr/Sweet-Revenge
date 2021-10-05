# Sweet Revenge I
# Version 2021.01.011
# 04.10.2021

########################################################
#                                                      #
#             License and copyright notice             #
#             ============================             #
#                                                      #
# Copyright © 2021 D.K.Roberts                         #
#                  debkroberts.com                     #
#                                                      #
# Licence: Apache License 2.0                          #
# You may distribute and modify this file for private  #
# or commercial use, upon condition that you state     #
# all changes and preserve this license and copyright  #
# notice in full. The author accepts no liability and  #
# offers no warranty for the use of this software.     #
# Trademark use is prohibited.                         #
#                                                      #
########################################################


# import packages
import random
from tabulate import tabulate

# global parameters
playerName = ''
gameBoardSize = dict()
gameBoard = dict()
gameBoardArray = dict()
pointsScoredThisLevel = 0
pointsScoredGlobal = 0
gameBoardSize = []
gameBoardArray = {}
validCellsList = []

# function: initiate starting game level
def getFirstGameLevel(playerName):
    print('Do you want to start on an easy, moderate or hard level?')
    print('Enter \'E\' for easy, \'M\' for moderate, or \'H\' for hard.')
    ans = input()
    if ans.lower() == 'e' : firstGameLevel = 1
    elif ans.lower() == 'm' : firstGameLevel = 6
    elif ans.lower() == 'h' : firstGameLevel = 11
    else : firstGameLevel = 1
    return firstGameLevel

# function: update game level
def updateGameLevel(gameLevel):
    gameLevel = gameLevel + 1
    return gameLevel

# function: initialise game board size
def getGameBoardSize(nextGameLevel):
    gameBoardSize = {1:[3,3], 2:[3,3], 3:[3,3], 4:[3,3], 5:[3,3], 6:[4,4], 7:[4,4], 8:[4,4], 9:[4,4], 10:[4,4], 11:[5,5], 12:[5,5], 13:[5,5], 14:[5,5], 15:[5,5]}
    return gameBoardSize

# function: initialise empty game board
def getGameBoard(nextGameLevel, gameBoardSize):
    rowCount = gameBoardSize[nextGameLevel][0]
    columnCount = gameBoardSize[nextGameLevel][1]
    for r in range(rowCount):
        if r+1 == 1 : rowLabel = 'A'
        elif r+1 == 2 : rowLabel = 'B'
        elif r+1 == 3 : rowLabel = 'C'
        elif r+1 == 4 : rowLabel = 'D'
        elif r+1 == 5 : rowLabel = 'E'
        elif r+1 == 6 : rowLabel = 'F'
        elif r+1 == 7 : rowLabel = 'G'
        elif r+1 == 8 : rowLabel = 'H'
        for c in range(columnCount):
            row = r+1
            col = c+1
            colLabel = str(c+1)
            cellRef = rowLabel+colLabel
            values = {'row':row, 'col':col, 'cellRef':cellRef, 'val':0, 'colour':None, 'graphic':'display', 'moveStatus':'unlocked', 'fillStatus':'empty'}
            gameBoardArray[cellRef] = values
    return gameBoardArray

# function: randomly fill newly-initialised game board with counters
def fillGameBoardArray(gameBoardArray):
    for cell,vals in gameBoardArray.items():
        randomFill = random.randint(1,4) ## REFACTOR: REPLACE STATIC WITH DYNAMIC CODE; USE len(colours) 
        vals['val'] = randomFill
        vals['fillStatus'] = 'filled'
    return gameBoardArray

# function: get next game level
def getLevelParams(firstGameLevel, nextGameLevel):
    thisGameLevel = nextGameLevel
    allowedMoves = movesAllowedThisLevel(thisGameLevel)
    availableMoves = allowedMoves
    pointsScoredThisLevel = 0
    return thisGameLevel, allowedMoves, availableMoves, pointsScoredThisLevel

# function: checking available moves based on game level
def movesAllowedThisLevel(thisGameLevel):
    allowedMoves = 0
    if thisGameLevel <= 5 : allowedMoves = 20
    elif thisGameLevel >= 6 and thisGameLevel <= 10 : allowedMoves = 15
    elif thisGameLevel >= 11 : allowedMoves = 10
    return allowedMoves

# function: game board & counters
def drawGameBoard(thisGameLevel, gameBoardSize, gameBoardArray):
    valuesOnlyDict = dict()
    for cell,vals in gameBoardArray.items():
        cellVal = vals['val']
        valuesOnlyDict[cell] = cellVal
    if thisGameLevel <= 5:
        print(tabulate(
            [
            ['A',gameBoardArray['A1']['val'],gameBoardArray['A2']['val'],gameBoardArray['A3']['val']],
            ['B',gameBoardArray['B1']['val'],gameBoardArray['B2']['val'],gameBoardArray['B3']['val']],
            ['C',gameBoardArray['C1']['val'],gameBoardArray['C2']['val'],gameBoardArray['C3']['val']]
            ], 
            headers=['','1','2','3']
            ))
    elif thisGameLevel >= 6 and thisGameLevel <= 10:
        print(tabulate(
            [
            ['A',gameBoardArray['A1']['val'],gameBoardArray['A2']['val'],gameBoardArray['A3']['val'],gameBoardArray['A4']['val']],
            ['B',gameBoardArray['B1']['val'],gameBoardArray['B2']['val'],gameBoardArray['B3']['val'],gameBoardArray['B4']['val']],
            ['C',gameBoardArray['C1']['val'],gameBoardArray['C2']['val'],gameBoardArray['C3']['val'],gameBoardArray['C4']['val']],
            ['D',gameBoardArray['D1']['val'],gameBoardArray['D2']['val'],gameBoardArray['D3']['val'],gameBoardArray['D4']['val']]
            ], 
            headers=['','1','2','3','4']
            ))
    elif thisGameLevel >= 11:
        print(tabulate(
            [
            ['A',gameBoardArray['A1']['val'],gameBoardArray['A2']['val'],gameBoardArray['A3']['val'],gameBoardArray['A4']['val'],gameBoardArray['A5']['val']],
            ['B',gameBoardArray['B1']['val'],gameBoardArray['B2']['val'],gameBoardArray['B3']['val'],gameBoardArray['B4']['val'],gameBoardArray['B5']['val']],
            ['C',gameBoardArray['C1']['val'],gameBoardArray['C2']['val'],gameBoardArray['C3']['val'],gameBoardArray['C4']['val'],gameBoardArray['C5']['val']],
            ['D',gameBoardArray['D1']['val'],gameBoardArray['D2']['val'],gameBoardArray['D3']['val'],gameBoardArray['D4']['val'],gameBoardArray['D5']['val']],
            ['E',gameBoardArray['E1']['val'],gameBoardArray['E2']['val'],gameBoardArray['E3']['val'],gameBoardArray['E4']['val'],gameBoardArray['E5']['val']]
            ], 
            headers=['','1','2','3','4','5']
            ))
    print()

# function: get list of valid cells for this game level
def getValidCellsList(validCellsList, gameBoardArray):
    validCellsList = []
    for k, v in gameBoardArray.items():
        validCellsList.append(k)
    return validCellsList

# function: play next player move
def getPlayerMove(thisGameLevel, availableMoves, allowedMoves, gameBoardArray, validCellsList):
    print('Which counter would you like to move?')
    print('(Enter the row/column cell reference, for example: A1, B3)')
    selectedCounter = input().upper()
    while selectedCounter not in validCellsList:
        print('\'%s\' is not a valid entry. Please select again from the list:' % selectedCounter)
        print(validCellsList)
        selectedCounter = input().upper()
    print('Which counter would you like to swap it with?')
    print('(Enter the row/column cell reference.)')
    swappedCounter = input().upper()
    while swappedCounter not in validCellsList:
        print('\'%s\' is not a valid entry. Please select again from the list:' % selectedCounter)
        print(validCellsList)
        swappedCounter = input().upper()
    gameBoardArray = updateGameBoard(gameBoardArray, selectedCounter, swappedCounter, thisGameLevel)
    availableMoves -= 1
    return thisGameLevel, availableMoves, gameBoardArray

# function: update game board after move
def updateGameBoard(gameBoardArray, selectedCounter, swappedCounter, thisGameLevel):
    print()
    print('Selected:', selectedCounter)
    print('Swapping with:', swappedCounter)
    print()
    selectedValue = gameBoardArray[selectedCounter]['val']
    swappedValue = gameBoardArray[swappedCounter]['val']
    newSelectedValue = swappedValue
    newSwappedValue = selectedValue
    gameBoardArray[selectedCounter]['val'] = newSelectedValue
    gameBoardArray[swappedCounter]['val'] = newSwappedValue
    drawGameBoard(thisGameLevel, gameBoardSize, gameBoardArray)
    return gameBoardArray

# function: calculate score after player move
def getMoveScore(thisGameLevel, gameBoardSize, gameBoardArray, pointsScoredThisLevel):
    valuesOnlyDict = dict()
    for cell,vals in gameBoardArray.items():
        cellVal = vals['val']
        valuesOnlyDict[cell] = cellVal
    rowCount = gameBoardSize[thisGameLevel][0]
    columnCount = gameBoardSize[thisGameLevel][1]
    rowA = list()
    rowB = list()
    rowC = list()
    rowD = list()
    rowE = list()
    scoreFromThisMove = 0
    for k,v in valuesOnlyDict.items():
        if k[0] == 'A':
            rowA.append(v)
        elif k[0] == 'B':
            rowB.append(v)
        elif k[0] == 'C':
            rowC.append(v)
        elif k[0] == 'D':
            rowD.append(v)
        elif k[0] == 'E':
            rowE.append(v)
    if rowCount == 3:
        if len(rowA) == 3 and (rowA[0] == rowA[1] == rowA[2]):
            print('Row A is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['A1']['val'] = 0
            gameBoardArray['A2']['val'] = 0
            gameBoardArray['A3']['val'] = 0
        if len(rowB) == 3 and (rowB[0] == rowB[1] == rowB[2]):
            print('Row B is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['B1']['val'] = 0
            gameBoardArray['B2']['val'] = 0
            gameBoardArray['B3']['val'] = 0
        if len(rowC) == 3 and (rowC[0] == rowC[1] == rowC[2]):
            print('Row C is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['C1']['val'] = 0
            gameBoardArray['C2']['val'] = 0
            gameBoardArray['C3']['val'] = 0
    elif rowCount == 4:
        if len(rowA) == 4 and (rowA[0] == rowA[1] == rowA[2]):
            print('Row A is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['A1']['val'] = 0
            gameBoardArray['A2']['val'] = 0
            gameBoardArray['A3']['val'] = 0
        if len(rowA) == 4 and (rowA[1] == rowA[2] == rowA[3]):
            print('Row A is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['A2']['val'] = 0
            gameBoardArray['A3']['val'] = 0
            gameBoardArray['A4']['val'] = 0
        if len(rowB) == 4 and (rowB[0] == rowB[1] == rowB[2]):
            print('Row B is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['B1']['val'] = 0
            gameBoardArray['B2']['val'] = 0
            gameBoardArray['B3']['val'] = 0
        if len(rowB) == 4 and (rowB[1] == rowB[2] == rowB[3]):
            print('Row B is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['B2']['val'] = 0
            gameBoardArray['B3']['val'] = 0
            gameBoardArray['B4']['val'] = 0
        if len(rowC) == 4 and (rowC[0] == rowC[1] == rowC[2]):
            print('Row C is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['C1']['val'] = 0
            gameBoardArray['C2']['val'] = 0
            gameBoardArray['C3']['val'] = 0
        if len(rowC) == 4 and (rowC[1] == rowC[2] == rowC[3]):
            print('Row C is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['C2']['val'] = 0
            gameBoardArray['C3']['val'] = 0
            gameBoardArray['C4']['val'] = 0
        if len(rowD) == 4 and (rowD[0] == rowD[1] == rowD[2]):
            print('Row D is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['D1']['val'] = 0
            gameBoardArray['D2']['val'] = 0
            gameBoardArray['D3']['val'] = 0
        if len(rowD) == 4 and (rowD[1] == rowD[2] == rowD[3]):
            print('Row D is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['D2']['val'] = 0
            gameBoardArray['D3']['val'] = 0
            gameBoardArray['D4']['val'] = 0
    elif rowCount == 5:
        if len(rowA) == 5 and (rowA[0] == rowA[1] == rowA[2]):
            print('Row A is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['A1']['val'] = 0
            gameBoardArray['A2']['val'] = 0
            gameBoardArray['A3']['val'] = 0
        if len(rowA) == 5 and (rowA[1] == rowA[2] == rowA[3]):
            print('Row A is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['A2']['val'] = 0
            gameBoardArray['A3']['val'] = 0
            gameBoardArray['A4']['val'] = 0
        if len(rowA) == 5 and (rowA[2] == rowA[3] == rowA[4]):
            print('Row A is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['A3']['val'] = 0
            gameBoardArray['A4']['val'] = 0
            gameBoardArray['A5']['val'] = 0
        if len(rowB) == 5 and (rowB[0] == rowB[1] == rowB[2]):
            print('Row B is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['B1']['val'] = 0
            gameBoardArray['B2']['val'] = 0
            gameBoardArray['B3']['val'] = 0
        if len(rowB) == 5 and (rowB[1] == rowB[2] == rowB[3]):
            print('Row B is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['B2']['val'] = 0
            gameBoardArray['B3']['val'] = 0
            gameBoardArray['B4']['val'] = 0
        if len(rowB) == 5 and (rowB[2] == rowB[3] == rowB[4]):
            print('Row B is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['B3']['val'] = 0
            gameBoardArray['B4']['val'] = 0
            gameBoardArray['B5']['val'] = 0
        if len(rowC) == 5 and (rowC[0] == rowC[1] == rowC[2]):
            print('Row C is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['C1']['val'] = 0
            gameBoardArray['C2']['val'] = 0
            gameBoardArray['C3']['val'] = 0
        if len(rowC) == 5 and (rowC[1] == rowC[2] == rowC[3]):
            print('Row C is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['C2']['val'] = 0
            gameBoardArray['C3']['val'] = 0
            gameBoardArray['C4']['val'] = 0
        if len(rowC) == 5 and (rowC[2] == rowC[3] == rowC[4]):
            print('Row C is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['C3']['val'] = 0
            gameBoardArray['C4']['val'] = 0
            gameBoardArray['C5']['val'] = 0
        if len(rowD) == 5 and (rowD[0] == rowD[1] == rowD[2]):
            print('Row D is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['D1']['val'] = 0
            gameBoardArray['D2']['val'] = 0
            gameBoardArray['D3']['val'] = 0
        if len(rowD) == 5 and (rowD[1] == rowD[2] == rowD[3]):
            print('Row D is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['D2']['val'] = 0
            gameBoardArray['D3']['val'] = 0
            gameBoardArray['D4']['val'] = 0
        if len(rowD) == 5 and (rowD[2] == rowD[3] == rowD[4]):
            print('Row D is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['D3']['val'] = 0
            gameBoardArray['D4']['val'] = 0
            gameBoardArray['D5']['val'] = 0
        if len(rowE) == 5 and (rowE[0] == rowE[1] == rowE[2]):
            print('Row E is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['E1']['val'] = 0
            gameBoardArray['E2']['val'] = 0
            gameBoardArray['E3']['val'] = 0
        if len(rowE) == 5 and (rowE[1] == rowE[2] == rowE[3]):
            print('Row E is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['E2']['val'] = 0
            gameBoardArray['E3']['val'] = 0
            gameBoardArray['E4']['val'] = 0
        if len(rowE) == 5 and (rowE[2] == rowE[3] == rowE[4]):
            print('Row E is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['E3']['val'] = 0
            gameBoardArray['E4']['val'] = 0
            gameBoardArray['E5']['val'] = 0
    column1 = list()
    column2 = list()
    column3 = list()
    column4 = list()
    column5 = list()
    for k,v in valuesOnlyDict.items():
        if k[1] == '1':
            column1.append(v)
        elif k[1] == '2':
            column2.append(v)
        elif k[1] == '3':
            column3.append(v)
        elif k[1] == '4':
            column4.append(v)
        elif k[1] == '5':
            column5.append(v)
    if columnCount == 3:
        if len(column1) == 3 and (column1[0] == column1[1] == column1[2]):
            print('Column 1 is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['A1']['val'] = 0
            gameBoardArray['B1']['val'] = 0
            gameBoardArray['C1']['val'] = 0
        if len(column2) == 3 and (column2[0] == column2[1] == column2[2]):
            print('Column 2 is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['A2']['val'] = 0
            gameBoardArray['B2']['val'] = 0
            gameBoardArray['C2']['val'] = 0
        if len(column3) == 3 and (column3[0] == column3[1] == column3[2]):
            print('Column 3 is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['A3']['val'] = 0
            gameBoardArray['B3']['val'] = 0
            gameBoardArray['C3']['val'] = 0
    elif columnCount == 4:
        if len(column1) == 4 and (column1[0] == column1[1] == column1[2]):
            print('Column 1 is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['A1']['val'] = 0
            gameBoardArray['B1']['val'] = 0
            gameBoardArray['C1']['val'] = 0
        if len(column1) == 4 and (column1[1] == column1[2] == column1[3]):
            print('Column 1 is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['B1']['val'] = 0
            gameBoardArray['C1']['val'] = 0
            gameBoardArray['D1']['val'] = 0
        if len(column2) == 4 and (column2[0] == column2[1] == column2[2]):
            print('Column 2 is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['A2']['val'] = 0
            gameBoardArray['B2']['val'] = 0
            gameBoardArray['C2']['val'] = 0
        if len(column2) == 4 and (column2[1] == column2[2] == column2[3]):
            print('Column 2 is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['B2']['val'] = 0
            gameBoardArray['C2']['val'] = 0
            gameBoardArray['D2']['val'] = 0
        if len(column3) == 4 and (column3[0] == column3[1] == column3[2]):
            print('Column 3 is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['A3']['val'] = 0
            gameBoardArray['B3']['val'] = 0
            gameBoardArray['C3']['val'] = 0
        if len(column3) == 4 and (column3[1] == column3[2] == column3[3]):
            print('Column 3 is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['B3']['val'] = 0
            gameBoardArray['C3']['val'] = 0
            gameBoardArray['D3']['val'] = 0
        if len(column4) == 4 and (column4[0] == column4[1] == column4[2]):
            print('Column 4 is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['A4']['val'] = 0
            gameBoardArray['B4']['val'] = 0
            gameBoardArray['C4']['val'] = 0
        if len(column4) == 4 and (column4[1] == column4[2] == column4[3]):
            print('Column 4 is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['B4']['val'] = 0
            gameBoardArray['C4']['val'] = 0
            gameBoardArray['D4']['val'] = 0
    elif columnCount == 5:
        if len(column1) == 5 and (column1[0] == column1[1] == column1[2]):
            print('Column 1 is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['A1']['val'] = 0
            gameBoardArray['B1']['val'] = 0
            gameBoardArray['C1']['val'] = 0
        if len(column1) == 5 and (column1[1] == column1[2] == column1[3]):
            print('Column 1 is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['B1']['val'] = 0
            gameBoardArray['C1']['val'] = 0
            gameBoardArray['D1']['val'] = 0
        if len(column1) == 5 and (column1[2] == column1[3] == column1[4]):
            print('Column 1 is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['C1']['val'] = 0
            gameBoardArray['D1']['val'] = 0
            gameBoardArray['E1']['val'] = 0
        if len(column2) == 5 and (column2[0] == column2[1] == column2[2]):
            print('Column 2 is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['A2']['val'] = 0
            gameBoardArray['B2']['val'] = 0
            gameBoardArray['C2']['val'] = 0
        if len(column2) == 5 and (column2[1] == column2[2] == column2[3]):
            print('Column 2 is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['B2']['val'] = 0
            gameBoardArray['C2']['val'] = 0
            gameBoardArray['D2']['val'] = 0
        if len(column2) == 5 and (column2[2] == column2[3] == column2[4]):
            print('Column 2 is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['C2']['val'] = 0
            gameBoardArray['D2']['val'] = 0
            gameBoardArray['E2']['val'] = 0
        if len(column3) == 5 and (column3[0] == column3[1] == column3[2]):
            print('Column 3 is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['A3']['val'] = 0
            gameBoardArray['B3']['val'] = 0
            gameBoardArray['C3']['val'] = 0
        if len(column3) == 5 and (column3[1] == column3[2] == column3[3]):
            print('Column 3 is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['B3']['val'] = 0
            gameBoardArray['C3']['val'] = 0
            gameBoardArray['D3']['val'] = 0
        if len(column3) == 5 and (column3[2] == column3[3] == column3[4]):
            print('Column 3 is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['C3']['val'] = 0
            gameBoardArray['D3']['val'] = 0
            gameBoardArray['E3']['val'] = 0
        if len(column4) == 5 and (column4[0] == column4[1] == column4[2]):
            print('Column 4 is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['A4']['val'] = 0
            gameBoardArray['B4']['val'] = 0
            gameBoardArray['C4']['val'] = 0
        if len(column4) == 5 and (column4[1] == column4[2] == column4[3]):
            print('Column 4 is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['B4']['val'] = 0
            gameBoardArray['C4']['val'] = 0
            gameBoardArray['D4']['val'] = 0
        if len(column4) == 5 and (column4[2] == column4[3] == column4[4]):
            print('Column 4 is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['C4']['val'] = 0
            gameBoardArray['D4']['val'] = 0
            gameBoardArray['E4']['val'] = 0
        if len(column5) == 5 and (column5[0] == column5[1] == column5[2]):
            print('Column 5 is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['A5']['val'] = 0
            gameBoardArray['B5']['val'] = 0
            gameBoardArray['C5']['val'] = 0
        if len(column5) == 5 and (column5[1] == column5[2] == column5[3]):
            print('Column 5 is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['B5']['val'] = 0
            gameBoardArray['C5']['val'] = 0
            gameBoardArray['D5']['val'] = 0
        if len(column5) == 5 and (column5[2] == column5[3] == column5[4]):
            print('Column 5 is a match-3 : score 3 points')
            scoreFromThisMove += 3
            gameBoardArray['C5']['val'] = 0
            gameBoardArray['D5']['val'] = 0
            gameBoardArray['E5']['val'] = 0
    print('Move score:', scoreFromThisMove)
    return scoreFromThisMove, gameBoardArray

# function: update level score after move
def getLevelScore(scoreFromThisMove, pointsScoredThisLevel):
    pointsScoredThisLevel += scoreFromThisMove
    print('Level score:', pointsScoredThisLevel)
    return pointsScoredThisLevel

# function: update global game score after move
def getGlobalScore(scoreFromThisMove, pointsScoredGlobal):
    pointsScoredGlobal += scoreFromThisMove
    print('Global score:', pointsScoredGlobal)
    return pointsScoredGlobal

# function: check & update win/lose status after player move or system move
def getWinStatus(thisGameLevel, pointsScoredThisLevel, availableMoves, allowedMoves, winStatus):
    # check how many points needed to win this level
    pointsToWinLevel = pointsToWin(thisGameLevel)
    # checking & updating win/lose status
    if pointsScoredThisLevel >= pointsToWinLevel:
        winStatus = True
    return winStatus

# function: check & update win/lose status after player move or system move
def getLoseStatus(availableMoves, loseStatus):
    if availableMoves <= 0:
        loseStatus = True
    else : loseStatus = False
    return loseStatus

# function: advise points needed to win this level
def pointsToWin(thisGameLevel):
    pointsToWinLevel = 0
    if thisGameLevel <= 5 : pointsToWinLevel = 20
    elif thisGameLevel >= 6 and thisGameLevel <= 10 : pointsToWinLevel = 50
    elif thisGameLevel >= 11 : pointsToWinLevel = 90
    return pointsToWinLevel

# function: check if there are empty cells (ie zero-value cells) in gameBoardArray
def checkEmptyCells(gameBoardArray):
    emptyCellsList = []
    for cell,vals in gameBoardArray.items():
        cellVal = vals['val']
        if cellVal == 0 : emptyCellsList.append(cellVal)
    return emptyCellsList

# function: randomly fill any zero-value cells in game board (at system move, after player move)
def getSystemMove(thisGameLevel, gameBoardArray):
    for cell,vals in gameBoardArray.items():
        cellVal = vals['val']
        if cellVal == 0:
            cellVal = random.randint(1,4)
            vals['val'] = cellVal
    return gameBoardArray

# function: initialise next game level
def initialiseNextLevel(nextGameLevel):
    gameBoardSize = getGameBoardSize(nextGameLevel)
    gameBoardArray = getGameBoard(nextGameLevel, gameBoardSize)
    gameBoardArray = fillGameBoardArray(gameBoardArray)
    return gameBoardSize, gameBoardArray

# function: set up next game, initialise & set parameters, & display to player
def getNextGame(firstGameLevel, nextGameLevel, playerName):
    gameBoardSize, gameBoardArray = initialiseNextLevel(nextGameLevel)
    thisGameLevel, allowedMoves, availableMoves, pointsScoredThisLevel = getLevelParams(firstGameLevel, nextGameLevel)
    return gameBoardSize, gameBoardArray, thisGameLevel, allowedMoves, availableMoves, pointsScoredThisLevel 

# function: set up display page
def displayPage(pageType):
    if pageType == 'welcomePage':
        print('''
        
        +++++++++++++++++++++++++++++++++++++++
        +                                     +
        +      Welcome to Sweet Revenge!      +
        +                                     +
        +++++++++++++++++++++++++++++++++++++++
        
        ''')
    elif pageType == 'instructionPage':
        print('''
        
        INSTRUCTIONS
        ++++++++++++
        Objective of the game is to match 3 or more counters of any one number in a row or
        column to score points.
        
        Bonus points are awarded for multiple adjacent matches. You can only select to move
        one counter at a time, but can move it to any other available (empty) cell, or swap
        it with another counter on the board.
        
        You only have a certain number of available moves for each level. To win the level,
        you need to score the required number of points before all your moves are up.
        
        You can choose to start on an easy level (3x3 board), moderate level (4x4 board) or
        a hard level (5x5 board). Available moves decrease and points required to win increase
        as the levels get harder.
        
        Good luck!!
        
        ''')
        print('Press any key to continue...')
    elif pageType == 'winPage':
        print('''
        
        +++++++++++++++++++++++++++++++++++++++
        +                                     +
        + Congratulations! You won the level. +
        +                                     +
        +++++++++++++++++++++++++++++++++++++++
        
        ''')
    elif pageType == 'losePage':
        print('''
        
        +++++++++++++++++++++++++++++++++++++++
        +                                     +
        +     Sorry! You lost that level.     +
        +                                     +
        +++++++++++++++++++++++++++++++++++++++
        
        ''')

# function: display message
def displayMessage(msgType, playerName):
    playerName = str(playerName)
    if msgType == 'getPlayerNameMsg':
        msg = 'Enter your name:'
    if msgType == 'checkForAccountMsg':
        msg = 'Do you already have an account (Y/N)?'
    if msgType == 'welcomeMsg':
        msg = 'Welcome, ' + playerName + '.'
    if msgType == 'queryCreatePersonalAccountMsg':
        msg = 'Would you like to set up an account, to store your winning points (Y/N)?'
    if msgType == 'dontCreatePersonalAccountMsg':
        msg = 'OK, no problems '+ playerName +'. You can change your mind later on if you want.'
    if msgType == 'createPersonalAccountMsg':
        msg = 'Enter email or leave blank:'
    if msgType == 'personalAccountCreatedMsg':
        msg = 'Great, your account is all set up to store your winnings.'
    if msgType == 'getFirstGameLevelMsg':
        msg = '''
        Do you want to start on an easy, moderate or hard level?
        Enter \'E\' for easy, \'M\' for moderate, or \'H\' for hard.
        '''
    if msgType == 'playAgainMsg':
        msg = 'Righto, ' + playerName + ', let\'s go!'
    if msgType == 'dontPlayAgainMsg':
        msg = 'Okey-dokey, ' + playerName + ', bye!'
    if msgType == 'endGameMsg':
        msg = 'We had some fun today, didn\'t we? See you again soon, ' + playerName + '.'
    return msg

# function: get player name 
def getPlayerName():
    playerName = input()
    return playerName

# function: check if player has a personal account
def checkForPersonalAccount(playerName):
    print(displayMessage('checkForAccountMsg', playerName))
    ans = input()
    if ans.lower() == 'y' :
        accExists = True
    else:
        accExists = False
    return accExists

# function: get personal accout details
def getPersonalAccountDetails(playerName):
    print('Nice. Please enter your account number:')
    persAccRef = input()
    ## TODO: ADD CODE TO RETRIEVE ACCOUNT DETAILS FROM DATABASE
    persAccName = playerName
    persAccEmail = 'placeholder email'
    displayAccountDetails(persAccName, persAccRef, persAccEmail)
    loginStatus = True
    return persAccName, persAccRef, persAccEmail, loginStatus

# function: display personal account details
def displayAccountDetails(persAccName, persAccRef, persAccEmail):
    print('Your personal account details are as follows:')
    print('Name: ' + str(persAccName))
    print('Email: ' + str(persAccEmail))
    print('Account #: ' + str(persAccRef))
    print()

# function: ask if player wishes to set up personal account
def queryCreatePersonalAccount(playerName):
    print(displayMessage('queryCreatePersonalAccountMsg', playerName))
    ans = input()
    if ans.lower() == 'y':
        accExists, persAccName, persAccRef, persAccEmail, loginStatus = createPersonalAccount(playerName)
    else:
        print()
        print(displayMessage('dontCreatePersonalAccountMsg', playerName))
        accExists = False
        persAccName = None
        persAccEmail = None
        persAccRef = None
        loginStatus = False
    return accExists, persAccName, persAccRef, persAccEmail, loginStatus

# function: create player personal account
def createPersonalAccount(playerName):
    persAccName = playerName
    print(displayMessage('createPersonalAccountMsg', playerName))
    persAccEmail = input()
    persAccRef = 1000 ## PLACEHOLDER REF#
    ## TODO: ADD CODE TO GET NEXT ACCOUNT REF# & STORE DETAILS TO DATABASE
    accExists = True
    loginStatus = True
    print(displayMessage('personalAccountCreatedMsg', playerName))
    displayAccountDetails(persAccName, persAccRef, persAccEmail)
    return accExists, persAccName, persAccRef, persAccEmail, loginStatus

## set up player logout request function [NOT CURRENTLY USING]
def logoutRequest(persAccName, persAccRef, persAccEmail, loginStatus):
    print('You are currently logged in, do you want to log out (Y/N)?')
    ans = input()
    if ans.lower() == 'y':
        print('Are you sure? Your winnings will only be stored to your account while you\'re logged in (although you can still play on as a guest). (Y/N)')
        ans1 = input()
        if ans1.lower() == 'y':
            persAccName = None
            persAccEmail = None
            persAccRef = None
            loginStatus = False
            print('Successfully logged out')
        elif ans1.lower != 'y' : pass
    elif ans.lower != 'y' : pass
    return persAccName, persAccRef, persAccEmail, loginStatus

# set up play again function [NOT CURRENTLY USING]
def queryPlayAgain(gameLevel, playerName, persAccRef, loginStatus):
    print(displayMessage('queryPlayAgainMsg', playerName))
    ans = input()
    if ans.lower() == 'y':
        playNextGameLevel(gameLevel, playerName, persAccRef, loginStatus, gameBoardArray)
    elif ans.lower() != 'y':
        print()
        print(':( We\'ll miss you.')

# set up store updated game level in DATABASE (personal account record) IF player is logged in function [NOT CURRENTLY USING]
def storeUpdatedGameLevel(gameLevel, loginStatus):
    print()
    print()
    if loginStatus == True:
        print('Storing current game level in personal account record...')
        print('Current game level stored in database is:', gameLevel)
        ## todo: ADD DATABASE CODE HERE
    elif loginStatus == False : print('No database update needed.')

# set up player login request function [NOT CURRENTLY USING]
def loginRequest(persAccName, persAccRef, persAccEmail, loginStatus):
    print('You are currently logged out, do you want to log in (Y/N)?')
    ans = input()
    if ans.lower() == 'n':
        print('Are you sure? Your winnings will not be stored to your account while you\'re logged out. (Y/N)')
        ans1 = input()
        if ans1.lower() == 'y':
            loginStatus = False
            persAccName = None
            persAccEmail = None
            persAccRef = None
            print('You are logged out')
        elif ans1.lower != 'y':
            persAccName, persAccRef, persAccEmail, loginStatus = getPersonalAccountDetails(playerName)
            print('Login successful.')
    elif ans.lower != 'y':
        persAccName, persAccRef, persAccEmail, loginStatus = getPersonalAccountDetails(playerName)
        print('Log in successful.')
    return persAccName, persAccRef, persAccEmail, loginStatus

# function: update global points & current level to player's personal account in database
def storeProgressToDatabase(persAccRef, pointsScoredGlobal, nextGameLevel):
    print('Storing details in database...')
    print('In personal account ref:', persAccRef)
    print('Total points scored:', pointsScoredGlobal)
    print('Next level to play:', nextGameLevel)
    print()
    ## TODO: ADD DATABASE CODE HERE

# function: end the game
def endGame(playerName):
    print(displayMessage('endGameMsg', playerName))



##### START GAME #####
# display welcome page
displayPage('welcomePage')
# collect player's name
print(displayMessage('getPlayerNameMsg', playerName))
playerName = getPlayerName()
print()
print(displayMessage('welcomeMsg', playerName))
print()
# ask if player already has an account (later links to login status, accStatus)
accExists = checkForPersonalAccount(playerName)
print()
# EITHER retrieve account details & print them out OR ask player if they wish to set up an account
if accExists == True:
    persAccName, persAccRef, persAccEmail, loginStatus = getPersonalAccountDetails(playerName)
elif accExists == False:
    accExists, persAccName, persAccRef, persAccEmail, loginStatus = queryCreatePersonalAccount(playerName)
print()
# display instructions page
displayPage('instructionPage')
input()

##### MAIN LOOP & GAME-PLAY LOOP FROM SRloopingGamePlay006.py - CONFIRMED CORRECT #####
# initialise current level
firstGameLevel = getFirstGameLevel(playerName)
nextGameLevel = firstGameLevel
# set up next game
gameBoardSize, gameBoardArray, thisGameLevel, allowedMoves, availableMoves, pointsScoredThisLevel = getNextGame(firstGameLevel, nextGameLevel, playerName)
# gets list of valid cell references for this game level
validCellsList = getValidCellsList(validCellsList, gameBoardArray)

# sets up high-level loop to bring player back into next game level if they request to play again,
# EITHER after winning OR after losing (asked at end after either 'won' or 'lost' page was displayed)
playNextLevel = True
winStatus = False
loseStatus = False

##### HIGH-LEVEL 'PLAY AGAIN?' LOOP STARTS #####
while playNextLevel == True:
    
    ##### MAIN GAME-PLAY LOOP STARTS #####
    
    # as long as win status  AND lose status are both False, make gameplay (player moves first)
    while winStatus == False and loseStatus == False:
        # player takes first move
        # display level & number of moves remaining
        print('''
        
        ++++++++++++++++++++
        +                  +
        +   Player move.   +
        +                  +
        ++++++++++++++++++++
        
        ''')
        print()
        print('You are playing level:', thisGameLevel)
        print('Moves available:', availableMoves, 'of', allowedMoves)
        print('Points so far this level:', pointsScoredThisLevel)
        print()
        # draw game board
        drawGameBoard(thisGameLevel, gameBoardSize, gameBoardArray)
        print()
        thisGameLevel, availableMoves, gameBoardArray = getPlayerMove(thisGameLevel, availableMoves, allowedMoves, gameBoardArray, validCellsList)
        # calculate score after player move
        scoreFromThisMove, gameBoardArray = getMoveScore(thisGameLevel, gameBoardSize, gameBoardArray, pointsScoredThisLevel)
        # update scores (level, global)
        pointsScoredThisLevel = getLevelScore(scoreFromThisMove, pointsScoredThisLevel)
        pointsScoredGlobal = getGlobalScore(scoreFromThisMove, pointsScoredGlobal)
        # check if won or lost after player move
        winStatus = getWinStatus(thisGameLevel, pointsScoredThisLevel, availableMoves, allowedMoves, winStatus)
        # IF won, breaks while loop
        # IF lost, while loop continues...
        # system takes a move, replacing 0s with random values
        print('''
        
        ++++++++++++++++++++
        +                  +
        +   System move.   +
        +                  +
        ++++++++++++++++++++
        
        ''')
        gameBoardArray = getSystemMove(thisGameLevel, gameBoardArray)
        drawGameBoard(thisGameLevel, gameBoardSize, gameBoardArray)
        # calculate score after system move
        scoreFromThisMove, gameBoardArray = getMoveScore(thisGameLevel, gameBoardSize, gameBoardArray, pointsScoredThisLevel)
        # update scores (level, global)
        pointsScoredThisLevel = getLevelScore(scoreFromThisMove, pointsScoredThisLevel)
        pointsScoredGlobal = getGlobalScore(scoreFromThisMove, pointsScoredGlobal)
        # check if won or lost after system move
        winStatus = getWinStatus(thisGameLevel, pointsScoredThisLevel, availableMoves, allowedMoves, winStatus)
        # IF won, breaks while loop
        # IF lost, while loop continues on...
        # check if there are empty cells that need to be refilled
        emptyCellsList = checkEmptyCells(gameBoardArray)
        while len(emptyCellsList) != 0:
            # IF yes, emptyCellsList loop runs to refill cells & rerun system move/score/check for win
            # refill empty cells [replacing 0s with random values]
            gameBoardArray = getSystemMove(thisGameLevel, gameBoardArray)
            print()
            drawGameBoard(thisGameLevel, gameBoardSize, gameBoardArray)
            # repeat win/lose check (as before)
            scoreFromThisMove, gameBoardArray = getMoveScore(thisGameLevel, gameBoardSize, gameBoardArray, pointsScoredThisLevel)
            # update points (as before)
            pointsScoredThisLevel = getLevelScore(scoreFromThisMove, pointsScoredThisLevel)
            pointsScoredGlobal = getGlobalScore(scoreFromThisMove, pointsScoredGlobal)
            emptyCellsList = checkEmptyCells(gameBoardArray)
        # IF no, breaks out of emptyCellsList loop & checks if there are available moves left, before returning to player next move
        emptyCellsList = []
        # check if level lost (by running out of available moves)
        loseStatus = getLoseStatus(availableMoves, loseStatus)
        # IF no more moves available, breaks out of main game-play loop on loseStatus==True
        if loseStatus == True and winStatus == False:
            print('Out of moves.')
        # IF moves still available, repeat player move [returns to start of main game-play loop]
    

    # IF won the level [broke out of main game-play loop on winStatus==True]
    if winStatus == True:
        # display win page
        displayPage('winPage')
        # update game level (outside main game-play loop to update only after player has clearly won the level)
        nextGameLevel = updateGameLevel(thisGameLevel)
        print('Next game level:', nextGameLevel)
    # IF lost the level [broke out of main game-play loop on loseStatus==True]
    elif loseStatus == True:
        # display lose page
        displayPage('losePage')
        print('You are still on level:', nextGameLevel)
    
    ##### MAIN GAME-PLAY LOOP ENDS #####
    
    
    # ask if player wants to play again (at end, after 'won' or 'lost' page was displayed)
    print('Would you like to play again (Y/N)?')
    ans = input()
    # IF yes
    if ans.lower() == 'y':
        # start next level
        # set game level parameters for next game level
        playNextLevel = True
        winStatus = False
        loseStatus = False
        # set up next game level
        gameBoardSize, gameBoardArray, thisGameLevel, allowedMoves, availableMoves, pointsScoredThisLevel = getNextGame(firstGameLevel, nextGameLevel, playerName)
    # IF no, or any other input
    else:
        # end game
        playNextLevel = False
        winStatus = False
        loseStatus = False
        
##### HIGH-LEVEL 'PLAY AGAIN?' LOOP ENDS #####

# end game
# if player is logged in, store global points & current level # in database (against their personal account) before quitting
if accExists == True and loginStatus == True:
    storeProgressToDatabase(persAccRef, pointsScoredGlobal, nextGameLevel)
print()
endGame(playerName)
quit()   
