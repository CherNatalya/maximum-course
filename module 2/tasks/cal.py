from tkinter import *
from decimal import *


def calculate():
    global stack
    global label
    result = 0
    operand2 = Decimal(stack.pop())
    operation = stack.pop()
    operand1 = Decimal(stack.pop())
    if operation == '+':
        result = operand1 + operand2
    if operation == '-':
        result = operand1 - operand2
    if operation == '/':
        result = operand1 / operand2
    if operation == '*':
        result = operand1 * operand2
    if operation == '**':
        result = operand1 ** operand2
    label.configure(text=str(result))


def click(text):
    global activeStr
    global stack
    if text == 'CE':
        stack.clear()
        activeStr = ''
        label.configure(text='0')
    elif '0' <= text <= '9':
        activeStr += text
        label.configure(text=activeStr)
    elif text == '.':
        if activeStr.find('.') == -1:
            activeStr += text
            label.configure(text=activeStr)
    else:
        if len(stack) >= 2:
            stack.append(label['text'])
            calculate()
            stack.clear()
            stack.append(label['text'])
            activeStr = ''
            if text != '=':
                stack.append(text)
        else:
            if text != '=':
                stack.append(label['text'])
                stack.append(text)
                activeStr = ''
                label.configure(text='0')


calc = Tk()
calc.title('Калькулятор')
buttons = (('7', '8', '9', '/', '4'),
           ('4', '5', '6', '*', '4'),
           ('1', '2', '3', '-', '4'),
           ('0', '.', '=', '+', '4'))
activeStr = ''
stack = []
label = Label(calc, text='0', width=35)
label.grid(row=0, column=0, columnspan=4, sticky="nsew")
button = Button(calc, text='CE', command=lambda text='CE': click(text))
button.grid(row=1, column=3, sticky="nsew")
for row1 in range(4):
    for col1 in range(4):
        button = Button(calc, text=buttons[row1][col1], command=lambda row=row1, col=col1: click(buttons[row][col]))
        button.grid(row=row1 + 2, column=col1, sticky="nsew")
calc.grid_rowconfigure(6, weight=1)
calc.grid_columnconfigure(4, weight=1)
calc.mainloop()
