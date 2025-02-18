import tkinter as tk

def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(value))

def clear():
    entry.delete(0, tk.END)

def backspace():
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text[:-1])  

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


window = tk.Tk()
window.title("Simple Calculator")


entry = tk.Entry(window, width=16, font=("Arial", 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == "=":
        tk.Button(window, text=button, width=5, height=2, font=("Arial", 18), command=calculate).grid(row=row_val, column=col_val)
    else:
        tk.Button(window, text=button, width=5, height=2, font=("Arial", 18), command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1


tk.Button(window, text="C", width=5, height=2, font=("Arial", 18), command=clear).grid(row=row_val, column=col_val)


tk.Button(window, text="←", width=5, height=2, font=("Arial", 18), command=backspace).grid(row=row_val, column=col_val + 1)


window.mainloop()
