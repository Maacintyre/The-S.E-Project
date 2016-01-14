__author__ = 'Pete Lozano'
from random import randint

Wordsearch = []
Wordlist = ["cats", "dog", "hog"]
X = 4
Y = 4

def initializeArray(array, Q, R):

    for i in range(Q):
        row = [" "] * R
        array.append(row)

def pickBox(xRan, yRan, H, L):

    if H:
        U = randint(0, (xRan - L))
        V = randint(0, yRan)
    else:
        U = randint(0, xRan)
        V = randint(0, (yRan - L))

    return U, V

def validSelection(array, U, V, H, L):
    print(U, V)
    for i in range(L):
        if array[U][V] != " ":
            return False
        else:
            if H:
                U += 1
            else:
                V += 1
    return True

def insertWord(array, U, V, H, Word):

    if H:
        for i in range(len(Word)):
            array[U][V] = str(Word[i])
            U += 1
    else:
        for i in range(len(Word)):
            array[U][V] = Word[i]
            V += 1

def insertList(Wordsearch, WordList, X, Y):
    Valid = False
    Horizontal = randint(0, 1)

    for Word in WordList:
        L = len(Word)
        while not Valid:
            coordX, coordY = pickBox(X, Y, Horizontal, L - 1)
            Valid = validSelection(Wordsearch, coordX, coordY, Horizontal, L)
            if Valid:
                insertWord(Wordsearch, coordX , coordY , Horizontal, Word)

def format(element):
    return "{" + element + "}"

output = ""

initializeArray(Wordsearch, (X + 1), (Y + 1))

insertList(Wordsearch, Wordlist, X, Y)

for k in range(Y + 1):
     for i in range(X + 1):
         output += format(str(Wordsearch[i][k]))
     print(output)
     output = ""

print(output)