# Rock Paper Scissor (Lizard Spock) By Michi Tanaka

# Imports
import tkinter as tk
import tkinter.messagebox
import random
from PIL import ImageTk, Image
# Initialize tkinter window
window = tk.Tk()

window.title("Rock Paper Scissor Lizard Spock")
# bg = yellow
window['background'] = '#FFE717'


# Function to display the winner
def RPSLS(player, computer):
    try:
        # RPSLS function
        win = ((computer - player) + 5) % 5
        message = "You chose " + choice[player - 1] + " and Computer chose " + choice[computer - 1]
        if (win == 0):
            message = str(message) + "\nDraw"
            tk.messagebox.showinfo("Result", message)
            # print("Draw...")
        elif (win < 3):
            message = str(message) + "\nComputer Wins!"
            tk.messagebox.showinfo("Result", message)
            # print("Computer Wins!")
        elif (win >= 3):
            message = str(message) + "\nYou Win!"
            tk.messagebox.showinfo("Result", message)
            # print("You Win!")
    except:
        tk.messagebox.showerror()
   
# Psuedo-random code for computer selection     
def computerChoice():
    # Computer choses 1, 2, 3, 4, or 5 for RPSLS
    global computer, choice
    compChoice = random.randint(1, 5)
    choice = ["rock", "spock", "paper", "lizard", "scissor"]
    computer = choice[compChoice - 1]
    return compChoice

def win(player):
        compChoice = computerChoice()
        RPSLS(player, compChoice)
        


# Import images through PIL
imgRock = ImageTk.PhotoImage(Image.open("Rock.png"))
imgPaper = ImageTk.PhotoImage(Image.open("Paper.png"))
imgScissors = ImageTk.PhotoImage(Image.open("Scissors.png"))
imgLizard = ImageTk.PhotoImage(Image.open("Lizard.png"))
imgSpock = ImageTk.PhotoImage(Image.open("Spock.png"))



# Frame
frame = tk.Frame(background = '#FFE717')



# Buttons
rock = tk.Button(
    master = frame, 
    text = 'Rock', 
    width = 150, 
    height = 150, 
    image = imgRock, 
    command = lambda: win(1)
)
paper = tk.Button(
    master = frame, 
    text = 'Paper', 
    width = 150, 
    height = 150, 
    image = imgPaper, 
    command = lambda: win(3)
)
scissor = tk.Button(
    master = frame, 
    text = 'Scissor', 
    width = 150, 
    height = 150, 
    image = imgScissors, 
    command = lambda: win(5)
)
lizard = tk.Button(
    master = frame, 
    text = 'Lizard', 
    width = 150, 
    height = 150, 
    image = imgLizard, 
    command = lambda: win(4)
)
spock = tk.Button(
    master = frame, 
    text = 'Spock', 
    width = 150, 
    height = 150, 
    image = imgSpock, 
    command = lambda: win(2)
)


# Pack everything
rock.pack(side = "left", padx = 20)
paper.pack(side = "left", padx = 20)
scissor.pack(side = "left", padx = 20)
lizard.pack(side = "left", padx = 20)
spock.pack(side = "left", padx = 20)
frame.pack(padx = 50, pady = 100)





tk.mainloop()
    



    
