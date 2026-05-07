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
operation_symbols = ["÷", "x", "-", "+", "=", "."]
row_count = len(button_values) #5
column_count = len(button_values[0]) #4

#colours
colour_special_buttons = "#EEA9BF"
colour_number_buttons = "#FFE0EA"
colour_text_special = "#FFE8F1"
colour_text_number = "#000000"
colour_background = "#FFDBE6"

#window setup
window = tkinter.Tk() #creates the window
window.title("Simple Calculator")
window.resizable(False, False) #no resizing of the window

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text = "0", font = ("Average, 45"), bg = colour_background,
                      foreground = colour_text_number, anchor = "e") #e for east (placement of text)

label.grid(row = 0, column = 0, columnspan = column_count, sticky = "we") #columnspan spans the label across all columns
                                                                          #we -> west to east spanning of the label
for row in range (row_count):
    for column in range (column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text = value, font = ("Average, 30"), width = column_count-1, height = 1,
                                command = lambda value = value: button.clicked(value))
        
        if value in top_row:
            button.configure(bg = colour_special_buttons, foreground = colour_text_special)
        elif value in operation_symbols:
            button.configure(bg = colour_special_buttons, foreground = colour_text_special)
        else: #number buttons
            button.configure(bg = colour_number_buttons, foreground = colour_text_number)

        button.grid(row = row + 1, column = column) #+1 because the label is in row 0

frame.pack()

def button_clicked(value):
    pass

window.mainloop() #we want the window to stay open until we close it, so we use mainloop() to keep it running

