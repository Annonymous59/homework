from tkinter import *
import random
from tkinter import messagebox
tk = Tk()

tk.geometry("680x280")

tk.resizable(0, 0)


def Play(choice):
    bot = random.choice("rps")
    define_winner(choice, bot,)

def define_winner(player, bot):

    if (player == "r" and bot == "s") or (player == "p" and bot == "r") or (player == "s" and bot == "p"):

        messagebox.showinfo("Result","You won 🏆🍾")

    elif (player == "r" and bot == "p") or (player == "p" and bot == "s") or (player == "s" and bot == "r"):
        messagebox.showinfo("Result","You lose 😶 try again")


    else:
        messagebox.showinfo("Result","It's a draw 🥱")





button_r = Button(tk, text="Rock", width=10, height=5, font= ("Helvetica 25 "), bg="yellow",fg="white", command=lambda: Play("r"))

button_r.grid(row = 0, column = 0, padx = 10, pady = 10)

button_p = Button(tk, text="Paper", width=10, height=5,font= ("Helvetica 25"), bg="cyan", fg="white", command=lambda: Play("p"))

button_p.grid(row = 0, column = 1,padx = 10, pady = 10)

button_s = Button(tk, text="Scissors", width=10, height=5,font= ("Helvetica 25"), bg="pink",fg="white", command=lambda: Play("s"))

button_s.grid(row = 0, column = 2,padx = 10, pady = 10)

label = Label(text="Choose: ",  font=("Helvatica 25"))
label.grid(row = 2, column = 1)

mainloop()