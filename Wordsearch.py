##This program will generate a randomized wordsearch with a list of words to be found
__author__ = 'Pete Lozano' , 'Karla Martinez' , 'Adam Seevers'
from random import randint

#This is a predetermined list to be inserted into a wordsearch
Wordlist = ["cats", "dog", "hog"]

#Variables to be used as the bounds for the table
X = 5
Y = 5

def initializeTable(table, Q, R):
#This function creates initializes the table with the default character " "
    for i in range(Q):
        row = [" "] * R
        table.append(row)

def pickBox(xRan, yRan, H, L):
#This function will randomly pick a square constrained to the length of the word
#This function will not pick a box that will cause an out of index error
    if H:
        U = randint(0, (xRan - L))
        V = randint(0, yRan)
    else:
        U = randint(0, xRan)
        V = randint(0, (yRan - L))

    return U, V

def validSelection(table, U, V, H, L):
#This function will ensure the there are no other impedeing words when placing the word down
    for i in range(L):
        if table[U][V] != " ":
            return False
        else:
            if H:
                U += 1
            else:
                V += 1
    return True

def insertWord(table, U, V, H, Word):
#This function will actually insert the word into the table either horizontally or veritically
    if H:
        for i in range(len(Word)):
            table[U][V] = str(Word[i])
            U += 1
    else:
        for i in range(len(Word)):
            table[U][V] = Word[i]
            V += 1

def insertList(Wordsearch, WordList, X, Y):
#This function will insert a list of words into a table based on a random number generator
#This function will ensure each word is placed in bounds and do not overlap
#Further more this function will add the word to a dictionary as a key and the coordinates of its first letter as the values
    Valid = False
    coordDictList = {}

    for Word in WordList:
        L = len(Word)
        Horizontal = bool(randint(0, 1))
        while not Valid:
            coordX, coordY = pickBox(X, Y, Horizontal, L - 1)
            Valid = validSelection(Wordsearch, coordX, coordY, Horizontal, L)
            if Valid:
                insertWord(Wordsearch, coordX , coordY , Horizontal, Word)
                coordDictList[Word] = coordX, coordY
        Valid = False
    return coordDictList

def fillTable(table, U, V):
#This function fills all blank spaces with a random character
    charA = 97

    for V in range(Y + 1):
        for U in range(X + 1):
            if table[U][V] == " ":
                table[U][V] = str(chr(randint(0, 25) + charA))

def printTable(table):
#This function will print the table to cout
#debugging purposes only
    output = ""
    for k in range(Y + 1):
     for i in range(X + 1):
         output += format(str(table[i][k]))
     print(output)
     output = ""

def format(element):
#This function will add brackets for easier viewing in cout
    return "{" + element + "}"

def createWordsearch(Wordlist, lenX, lenY ):
#This function will randomly generate a word search based on a list of words and the size of the desired grid
#This function will also generate the solution for the wordsearch at creation
    table = []

    initializeTable(table, (lenX + 1), (lenY + 1))

    winningList = insertList(table, Wordlist, lenX, lenY)

    fillTable(table, lenX, lenY)

    return table, winningList

def playGame(Words, xSize, ySize):
#This function will allow the user to play one wordsearch
    gameOver = False
    wordBoard, winWordCords = createWordsearch(Wordlist, X, Y)

    while not gameOver:
        printTable(wordBoard)
        row, column = playerTurn()
        winWordCords = calculateTurn(winWordCords, row, column)

        if len(winWordCords) == 0:
            gameOver = True
            print("Game Over")

def playerTurn():
#This function will get the user's input in row and column variables
#This function will also add 1 to the row and column variable for user friendliness
    userInput = input("Enter the column: ")
    UserX = int(userInput) + 1
    userInput = input("Enter the row: ")
    UserY = int(userInput) + 1
    return UserX, UserY

def calculateTurn(wordDict, UserX, UserY):
#This function will determine if the user's choice was the start of a word
    for key in wordDict:
        X, Y = wordDict[key]
        if (X == UserX) and (Y == UserY):
            wordDict.pop(key)
            return wordDict

playGame(Wordlist, X, Y)

