# Simple Calculator!
from tkinter import*

class Calculator:
    #initializer
    def __init__(self, root) -> None:
        self.root = root #stores the TK root window on the calc instance so every method can access it later
        self.title = self.root.title("Simple Calculator")
        self.root.geometry("615x680+400+100") #sets the size of the window to 615x680 pixels and positions it at (400, 100) on the screen
        self.root.configure(bg = "#EEA9BF") #sets the background color of the window to light pink

        self.MainFrame = Frame(self.root, bd = 18, width = 600, height = 670, relief = RIDGE, 
                               bg = "#F4BECF") #created inside of the window - Main Frame, relief = RIDGE gives a 3D raised grooved border style


    #addition function
    def addition(self):
        pass

    #subtraction function
    def subtraction(self):
        pass

    #multiplication function
    def multiplication(self):
        pass

    #division function
    def division(self):
        pass
    
    #