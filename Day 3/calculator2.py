import tkinter 

def button_click(number):
    current = entry.get()
    entry.delete(0, tkinter.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tkinter.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tkinter.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tkinter.END)
        entry.insert(0, "Error")

window = tkinter.Tk()
window.title("Calculator")

entry = tkinter.Entry(window, width=20)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row, col = 1, 0
for button in buttons:
    if button == 'C':
        tkinter.Button(window, text=button, padx=20, pady=20, command=clear).grid(row=row, column=col)
    elif button == '=':
        tkinter.Button(window, text=button, padx=20, pady=20, command=calculate).grid(row=row, column=col)
    else:
        tkinter.Button(window, text=button, padx=20, pady=20, command=lambda b=button: button_click(b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

window.mainloop()
