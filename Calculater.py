import tkinter as tk

# To perform the calculation
def calculate():
    try:
        expression = entry_display.get()
        result = eval(expression)
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, result)
    except Exception as e:
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, "Error")


def button_click(number):
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, current + str(number))


def clear():
    entry_display.delete(0, tk.END)


app = tk.Tk()
app.title("Basic Calculator")


entry_display = tk.Entry(app, width=18, font=('Arial', 20), justify="right")
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


button_1 = tk.Button(app, text="1", command=lambda: button_click(1), font=('Arial', 20), padx=20, pady=10)
button_2 = tk.Button(app, text="2", command=lambda: button_click(2), font=('Arial', 20), padx=20, pady=10)
button_3 = tk.Button(app, text="3", command=lambda: button_click(3), font=('Arial', 20), padx=20, pady=10)
button_4 = tk.Button(app, text="4", command=lambda: button_click(4), font=('Arial', 20), padx=20, pady=10)
button_5 = tk.Button(app, text="5", command=lambda: button_click(5), font=('Arial', 20), padx=20, pady=10)
button_6 = tk.Button(app, text="6", command=lambda: button_click(6), font=('Arial', 20), padx=20, pady=10)
button_7 = tk.Button(app, text="7", command=lambda: button_click(7), font=('Arial', 20), padx=20, pady=10)
button_8 = tk.Button(app, text="8", command=lambda: button_click(8), font=('Arial', 20), padx=20, pady=10)
button_9 = tk.Button(app, text="9", command=lambda: button_click(9), font=('Arial', 20), padx=20, pady=10)
button_0 = tk.Button(app, text="0", command=lambda: button_click(0), font=('Arial', 20), padx=20, pady=10)


button_add = tk.Button(app, text="+", command=lambda: button_click('+'), font=('Arial', 20), padx=20, pady=10)
button_subtract = tk.Button(app, text="-", command=lambda: button_click('-'), font=('Arial', 20), padx=20, pady=10)
button_multiply = tk.Button(app, text="*", command=lambda: button_click('*'), font=('Arial', 20), padx=20, pady=10)
button_divide = tk.Button(app, text="/", command=lambda: button_click('/'), font=('Arial', 20), padx=20, pady=10)


button_dot = tk.Button(app, text=".", command=lambda: button_click('.'), font=('Arial', 20), padx=20, pady=10)
button_clear = tk.Button(app, text="C", command=clear, font=('Arial', 20), padx=20, pady=10)
button_equal = tk.Button(app, text="=", command=calculate, font=('Arial', 20), padx=20, pady=10)


button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_add.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_0.grid(row=4, column=0)
button_dot.grid(row=4, column=1)
button_clear.grid(row=4, column=2)
button_divide.grid(row=4, column=3)

button_equal.grid(row=5, column=0, columnspan=4)

app.mainloop()
