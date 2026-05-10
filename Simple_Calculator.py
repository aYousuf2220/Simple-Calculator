# Simple Calculator!
import tkinter

#----------VARIABLES----------
button_values = [
    ["↻", "AC", "+/-", "←"], #top row
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "x"],
    ["1", "2", "3", "-"],
    [".", "0", "=", "+"] #bottom row
]

#reference
top_row = button_values[0]
operation_symbols = ["÷", "x", "-", "+", "=", "."]
row_count = len(button_values) #5
column_count = len(button_values[0]) #4

#for operations
A = "0"
operator = None
B = None

#for colours
colour_special_buttons = "#EEA9BF"
colour_number_buttons = "#FFE0EA"
colour_text_special = "#FFE8F1"
colour_text_number = "#000000"
colour_background = "#FFDBE6"

#----------WINDOW SET UP----------
window = tkinter.Tk() #creates the window
window.title("Simple Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text = "0", font = ("Average, 45"), bg = colour_background,
                      foreground = colour_text_number, anchor = "e", #e for east (placement of text)
                      width = column_count)
label.grid(row = 0, column = 0, columnspan = column_count, sticky = "we") #columnspan spans label across all columns

#----------BUTTONS SET UP----------
for row in range (row_count):
    for column in range (column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text = value, font = ("Average, 30"), width = column_count-1, height = 1,
                                command = lambda value = value: button_clicked(value))
        
        if value in top_row:
            button.configure(bg = colour_special_buttons, foreground = colour_text_special)
        elif value in operation_symbols:
            button.configure(bg = colour_special_buttons, foreground = colour_text_special)
        else: #number buttons
            button.configure(bg = colour_number_buttons, foreground = colour_text_number)

        button.grid(row = row + 1, column = column) #+1 because the label is in row 0

frame.pack()


#----------MAIN FUNCTIONS----------
def button_clicked(value):
    global top_row, operation_symbols, label, A, B, operator

    if value in top_row:
        special_operations(value)
    elif value in operation_symbols:
        operations(value)
    else:
        digits(value)

def special_operations(value):
    global label, A, B, operator

    if value == "↻":
        history()
    elif value == "AC":
        clear_all()
    elif value == "+/-":
        changing_sign()
    else: #backspace
        backspace()

def operations(value):
    global label, A, B, operator

    #decimal point
    if value == ".":
        if value not in label["text"]:
            label["text"] += value

    #addition

    #subtraction

    #multiplication

    #division

    #equal

def digits(value):
    global label

    if label["text"] == "0":
        label["text"] = value
    else:
        label["text"] += value

#----------HELPER FUNCTIONS----------
def clear_all():
    global label, A, B, operator

    A = "0"
    B = None
    operator = None

    label["text"] = "0"

def changing_sign():
    global label

    result = float(label["text"]) * -1
    label["text"] = remove_zero_decimal(result)

def remove_zero_decimal(number):
    if number % 1 == 0:
        number = int(number)

    return str(number)

def backspace():
    global label
    
    if label["text"] == "0":
        return
    else:
        label["text"] = label["text"][:-1]

        if label["text"] == "":
             label["text"] = "0"
        
        return label["text"]
    
def history():
    pass

window.mainloop() #to keep the window open