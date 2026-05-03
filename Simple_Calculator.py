# Simple Calculator!
import tkinter

button_values = [
    ["↻", "AC", "+/-", "←"], #top row
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "x"],
    ["1", "2", "3", "-"],
    [".", "0", "=", "+"] #bottom row
]

#reference for button values
top_row = button_values[0]
operation_symbols = ["÷", "x", "-", "+", "="]
row_count = len(button_values) #5
coloumn_count = len(button_values[0]) #4

#colours
colour_buttons = "#E37F9D"
colour_text = "#FFE8F1"
colour_screen = "#E994AE" #if this doesn't work out, then use black
colour_background = "#F4BECF"

#window setup
window = tkinter.Tk() #creates the window
window.title("Simple Calculator")

frame = tkinter.Frame(window, bg = colour_background)
label = tkinter.Label(frame, text = "0", font = ("Average, 45"), bg = colour_screen,
                      foreground = colour_text)

window.mainloop() #we want the window to stay open until we close it, so we use mainloop() to keep it running
