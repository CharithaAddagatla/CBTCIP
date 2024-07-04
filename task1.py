'''ROCK PAPER SCISSOR GAME

Winning Rules as follows:



Rock vs paper-> paper wins

Rock vs scissor-> Rock wins

paper vs scissor-> scissor wins '''


import tkinter as tk
import random

def determine_winner(user_choice):
    random_choice = random.choice(["rock", "paper", "scissor"])
   
    if  user_choice ==  random_choice:
        result = "It's a tie"
    elif (user_choice == "rock" and random_choice == "scissor") or (user_choice == "scissor" and random_choice == "rock") :
        result = "Rock Wins"
    elif(user_choice == "rock" and random_choice == "paper") or (user_choice == "paper" and random_choice == "rock"):
         result = "Paper Wins"
    elif(user_choice == "paper" and random_choice == "scissor") or (user_choice == "scissor" and random_choice == "paper"):
        result =  "Scissor wins"
    else:
        result = "You losed..\n try again"

    result_label.config( text=f"computer choosed: { random_choice}\n{result}" , font=('calibri', 20, 'italic') )

def on_button_click(choice):
    determine_winner(choice)


window = tk.Tk()
window.geometry("700x400")
window.title("Rock-Paper-Scissor Game")


start = tk.Label(window, text="Lets START the game! \n click one", font=('calibri', 20, 'italic'))
start.pack()

button_frame = tk.Frame(window)
button_frame.pack()


rock_btn = tk.Button(button_frame, text="Rock", bg='#A17C6E', 
                     font=('calibri', 20, 'bold'), command=lambda: on_button_click("rock"))
rock_btn.pack(side=tk.LEFT, padx=5)

paper_btn = tk.Button(button_frame, text="Paper", bg='#D3C6C6',
                      font=('calibri', 20, 'bold'), command=lambda: on_button_click("paper"))
paper_btn.pack(side=tk.LEFT, padx=5)

scissors_btn = tk.Button(button_frame, text="Scissor",bg='#CCBA78',
                         font=('calibri', 20, 'bold'), command=lambda: on_button_click("scissor"))
scissors_btn.pack(side=tk.LEFT, padx=5)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)


window.mainloop()

