from tkinter import *
import tkinter as tk
import customtkinter as ctk


class TicTacToeMainMenu(Tk):
  def __init__(self):
    super().__init__()

    self.title("TicTacToe")
    self.geometry("325x350")

    self["bg"]="lightblue"

    self.create_base()
    
  def create_base(self):

    #lABELSS
    self.label1=Label(self, text="TicTacToe", font=("Helvetica", 25,"bold"),bg="lightblue",fg="black")
    self.label1.place(relx=0.5,rely=0.1,anchor=CENTER)
    self.label2=Label(self, text="Main Menu", font=("Helvetica", 16,"bold"),bg="lightblue")
    self.label2.place(relx=0.5,rely=0.25,anchor=CENTER)

    self.label3=Label(self, text="Choose a game mode", font=("Helvetica", 13,"bold"),bg="lightblue")
    self.label3.place(relx=0.5,rely=0.38,anchor=CENTER)

    #BUTTONS
    self.button1 = ctk.CTkButton(self, width=10,text="Play With Computer",font=("Helvetica", 16),bg_color="#89CFF0", fg_color="#13274F",command=self.open_1player)
    self.button1.place(relx=0.5,rely=0.5,anchor=CENTER)
    self.button2 = ctk.CTkButton(self, width=10,text="Play With Friend" ,font=("Helvetica", 16),bg_color="#89CFF0", fg_color="#13274F",command=self.open_2player)
    self.button2.place(relx=0.5,rely=0.6,anchor=CENTER)
    self.button3 = ctk.CTkButton(self, width=10,text="Quit" ,font=("Helvetica", 16),bg_color="#89CFF0", fg_color="#13274F",command=self.quit)  
    self.button3.place(relx=0.5,rely=0.8,anchor=CENTER)


  def open_1player(self):
    self.destroy()
    from player1 import TicTacToe1
    c = TicTacToe1()
    c.mainloop()

  def open_2player(self):
    self.destroy()
    from multiplayers import TicTacToe2
    c = TicTacToe2()
    c.mainloop()

  def quit(self):
    self.destroy()
    

a=TicTacToeMainMenu()
a.mainloop()
