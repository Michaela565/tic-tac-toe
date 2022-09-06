from glob import glob
from multiprocessing.connection import wait
import tkinter as tk
from tkinter import font
import tkinter.ttk as ttk



window = tk.Tk() # Initializes the window 
window.title("Tic Tac Toe") # Makes the title Tic Tac Toe
window.geometry("465x520")
gameOver = False
oWins = False
lastMove = 0
# Width and Height of my buttons
myWidth = 10
myHeight = 5
buttonColor = "#7C94CE"
# -----------------------------


# Possible texts of the buttons
emptySpace = ""
emptySpaceImg = tk.PhotoImage(file = r"emptySpace.png")
xSpace = "X"
xSpaceImg = tk.PhotoImage(file = r"x.png")
oSpace = "O"
oSpaceImg = tk.PhotoImage(file = r"o.png")
# -----------------------------

isO = False # Boolean that tells us if it's O's turn

# Main brain of this game, an array with 9 numbers
# 0 == empty space
# 1 == used by X
# 2 == used by O
playSpace = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# -----------------------------

background = tk.Frame(width=510, height=520, bg = "#CFE6FF")
background.place(x=-5,y=0)

whosTurn = tk.Label(text="It's X turn.", bg = "#CFE6FF", font=("Arial", 16, "bold")) # Label that tells us who's turn is it

# Changes the text of whosTurn to show who's turn is it
def changeWhosTurn():
    # Declare global variables
    global whosTurn
    if isO:
        whosTurn['text'] ="It's " + oSpace + " turn."
    else:
        whosTurn['text'] = "It's " + xSpace + " turn."
# -----------------------------

# Changes the text on the buttons to which player pressed it
def changeBtnText(btn):
    # Declare global variables
    global isO
    global gameOver
    if not gameOver:
        if isO and btn['text'] == emptySpace:
            btn['text'] = oSpace
            btn['image'] = oSpaceImg
            isO = False
            changeWhosTurn()
        elif isO == False and btn['text'] == emptySpace:
            btn['text'] = xSpace
            btn['image'] = xSpaceImg
            isO = True
            changeWhosTurn()
        else:
            pass
# -----------------------------

# All the buttons
button1 = tk.Button(text = emptySpace, image= emptySpaceImg, command= lambda: [changeIndex(button1), changeBtnText(button1),])
button2 = tk.Button(text = emptySpace, image= emptySpaceImg, command= lambda: [changeIndex(button2), changeBtnText(button2)])
button3 = tk.Button(text = emptySpace, image= emptySpaceImg, command= lambda: [changeIndex(button3), changeBtnText(button3)])
button4 = tk.Button(text = emptySpace, image= emptySpaceImg, command= lambda: [changeIndex(button4), changeBtnText(button4)])
button5 = tk.Button(text = emptySpace, image= emptySpaceImg, command= lambda: [changeIndex(button5), changeBtnText(button5)])
button6 = tk.Button(text = emptySpace, image= emptySpaceImg, command= lambda: [changeIndex(button6), changeBtnText(button6)])
button7 = tk.Button(text = emptySpace, image= emptySpaceImg, command= lambda: [changeIndex(button7), changeBtnText(button7)])
button8 = tk.Button(text = emptySpace, image= emptySpaceImg, command= lambda: [changeIndex(button8), changeBtnText(button8)])
button9 = tk.Button(text = emptySpace, image= emptySpaceImg, command= lambda: [changeIndex(button9), changeBtnText(button9)])
# -----------------------------

# Change numbers of the assigned index in the array
def changeIndex(btnn):
    # Declare global variables
    global lastMove
    global playSpace
    global isO
    global gameOver
    # -----------------------------
    if not gameOver:
        if isO:
            if btnn == button1:
                playSpace[0] = 2
                lastMove = 1
            elif btnn == button2:
                playSpace[1] = 2
                lastMove = 2
            elif btnn == button3:
                playSpace[2] = 2
                lastMove = 3
            elif btnn == button4:
                playSpace[3] = 2
                lastMove = 4
            elif btnn == button5:
                playSpace[4] = 2
                lastMove = 5
            elif btnn == button6:
                playSpace[5] = 2
                lastMove = 6
            elif btnn == button7:
                playSpace[6] = 2
                lastMove = 7
            elif btnn == button8:
                playSpace[7] = 2
                lastMove = 8
            elif btnn == button9:
                playSpace[8] = 2
                lastMove = 9
        else:
            if btnn == button1:
                playSpace[0] = 1
            elif btnn == button2:
                playSpace[1] = 1
            elif btnn == button3:
                playSpace[2] = 1
            elif btnn == button4:
                playSpace[3] = 1
            elif btnn == button5:
                playSpace[4] = 1
            elif btnn == button6:
                playSpace[5] = 1
            elif btnn == button7:
                playSpace[6] = 1
            elif btnn == button8:
                playSpace[7] = 1
            elif btnn == button9:
                playSpace[8] = 1
# -----------------------------

# The main brain of the gameplay, keeps checking if one of the players wins
def game():
    # Declare global variables
    global oWins
    global whosTurn
    global gameOver
    global thisistrue
    global playSpace
    # -----------------------------

    # Checks if O wins, wanted to merge X and O together but there was no elegant way really (not that this is rlly elegant in any way)
    if playSpace[0] == 2 and playSpace[1] == 2 and playSpace[2] == 2:
        oWins = True
        gameOver = True
            
    elif playSpace[3] == 2 and playSpace[4] == 2 and playSpace[5] == 2:
        oWins = True
        gameOver = True
            
    elif playSpace[6] == 2 and playSpace[7] == 2 and playSpace[8] == 2:
        oWins = True
        gameOver = True
            
    elif playSpace[0] == 2 and playSpace[3] == 2 and playSpace[6] == 2:
        oWins = True
        gameOver = True
            
    elif playSpace[1] == 2 and playSpace[4] == 2 and playSpace[7] == 2:
        oWins = True
        gameOver = True
            
    elif playSpace[2] == 2 and playSpace[5] == 2 and playSpace[8] == 2:
        oWins = True
        gameOver = True
            
    elif playSpace[0] == 2 and playSpace[4] == 2 and playSpace[8] == 2:
        oWins = True
        gameOver = True
            
    elif playSpace[2] == 2 and playSpace[4] == 2 and playSpace[6] == 2:
        oWins = True
        gameOver = True
    # -----------------------------

    # Check if X wins
    elif playSpace[0] == 1 and playSpace[1] == 1 and playSpace[2] == 1:
        gameOver = True
            
    elif playSpace[3] == 1 and playSpace[4] == 1 and playSpace[5] == 1:
        gameOver = True
            
    elif playSpace[6] == 1 and playSpace[7] == 1 and playSpace[8] == 1:
        gameOver = True
        
    elif playSpace[0] == 1 and playSpace[3] == 1 and playSpace[6] == 1:
        gameOver = True
            
    elif playSpace[1] == 1 and playSpace[4] == 1 and playSpace[7] == 1:
        gameOver = True
            
    elif playSpace[2] == 1 and playSpace[5] == 1 and playSpace[8] == 1:
        gameOver = True
            
    elif playSpace[0] == 1 and playSpace[4] == 1 and playSpace[8] == 1:
        gameOver = True
            
    elif playSpace[2] == 1 and playSpace[4] == 1 and playSpace[6] == 1:
        gameOver = True
    # -----------------------------

    # Checks for gameover and if there is, loop stops and instead of whos turn is it, it prints out who wins
    if not gameOver:
        window.after(1000, game)
    elif gameOver and oWins:
        whosTurn['text'] = "Player O wins."
        whosTurn['fg'] = "#E24599"
    elif gameOver and not oWins:
        whosTurn['text'] = "Player X wins."
        whosTurn['fg'] = "#E24599"
    # -----------------------------
def ai():
    if not isO and not gameOver:
        print(lastMove)
        if lastMove == 1:
            if playSpace[1] == 2:
                button3.invoke()
            elif playSpace[3] == 2:
                button7.invoke()
            elif playSpace[4] == 2:
                button9.invoke()
            else:
                button4.invoke()
        elif lastMove == 2:
            if playSpace[0] == 2:
                button3.invoke()
            elif playSpace[2] == 2:
                button1.invoke()
            elif playSpace[4] == 2:
                button7.invoke()
            else:
                button4.invoke() 
        elif lastMove == 3:
            if playSpace[1] == 2:
                button1.invoke()
            elif playSpace[5] == 2:
                button9.invoke()
            elif playSpace[4] == 2:
                button7.invoke()
            else:
                button5.invoke()
        elif lastMove == 4:
            if playSpace[0] == 2:
                button7.invoke()
            elif playSpace[6] == 2:
                button1.invoke()
            elif playSpace[4] == 2:
                button6.invoke()
            else:
                button4.invoke()
        elif lastMove == 5:
            if playSpace[0] == 2:
                button9.invoke()
            elif playSpace[1] == 2:
                button8.invoke()
            elif playSpace[2] == 2:
                button7.invoke()
            elif playSpace[3] == 2:
                button6.invoke()
            elif playSpace[5] == 2:
                button4.invoke()
            elif playSpace[6] == 2:
                button3.invoke()
            elif playSpace[7] == 2:
                button2.invoke()
            elif playSpace[8] == 2:
                button1.invoke()
        elif lastMove == 6:
            if playSpace[2] == 2:
                button9.invoke()
            elif playSpace[8] == 2:
                button3.invoke()
            elif playSpace[4] == 2:
                button4.invoke()
            else:
                button9.invoke()
        elif lastMove == 7:
            if playSpace[3] == 2:
                button1.invoke()
            elif playSpace[7] == 2:
                button9.invoke()
            elif playSpace[4] == 2:
                button3.invoke()
            else:
                button4.invoke()
        elif lastMove == 8:
            if playSpace[6] == 2:
                button9.invoke()
            elif playSpace[8] == 2:
                button7.invoke()
            elif playSpace[4] == 2:
                button2.invoke()
            else:
                button4.invoke()
        else: # 9
            if playSpace[5] == 2:
                button3.invoke()
            elif playSpace[7] == 2:
                button7.invoke()
            elif playSpace[4] == 2:
                button1.invoke()
            else:
                button4.invoke()
    window.after(1000, ai)


# -----------------------------        

# Renders the whole thing
whosTurn.grid(row=0, column= 2, padx=10, pady= 10)
button1.grid(row=1, column=1, padx=10, pady= 10)
button2.grid(row=1, column=2, padx=10, pady= 10)
button3.grid(row=1, column=3, padx=10, pady= 10)
button4.grid(row=2, column=1, padx=10, pady= 10)
button5.grid(row=2, column=2, padx=10, pady= 10)
button6.grid(row=2, column=3, padx=10, pady= 10)
button7.grid(row=3, column=1, padx=10, pady= 10)
button8.grid(row=3, column=2, padx=10, pady= 10)
button9.grid(row=3, column=3, padx=10, pady= 10)
# -----------------------------


window.after(1000, game)
window.after(1000, ai)
window.mainloop()