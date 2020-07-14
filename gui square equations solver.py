from math import sqrt
from Tkinter import *
import numba

def solver(a,b,c):
    """ Решает квадратное уравнение и выводит отформатированный ответ """
    # находим дискриминант
    D = b*b - 4*a*c
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        text = "The discriminant is: %s \n X1 is: %s \n X2 is: %s \n" % (D, x1, x2)
    else:
        text = "The discriminant is: %s \n This equation has no solutions" % D
    return text


# родительский элемент
root = Tk()
# устанавливаем название окна
root.title("Quadratic calculator")
# устанавливаем минимальный размер окна
root.minsize(325, 230)
# выключаем возможность изменять окно
root.resizable(width=False, height=False)

# создаем рабочую область
frame = Frame(root)
frame.grid()

# поле для ввода первого аргумента уравнения (a)
a = Entry(frame, width=3)
a.grid(row=1, column=1, padx=(10, 0))

# текст после первого аргумента
a_lab = Label(frame, text="x**2+").grid(row=1, column=2)

# поле для ввода второго аргумента уравнения (b)
b = Entry(frame, width=3)
b.grid(row=1, column=3)
# текст после второго аргумента
b_lab = Label(frame, text="x+").grid(row=1, column=4)

# поле для ввода третьего аргумента уравнения (с)
c = Entry(frame, width=3)
c.grid(row=1, column=5)
# текст после третьего аргумента
c_lab = Label(frame, text="= 0").grid(row=1, column=6)

# кнопка решить
but = Button(frame, text="Solve").grid(row=1, column=7, padx=(10, 0))

# место для вывода решения уравнения
output = Text(frame, bg="lightblue", font="Arial 12", width=35, height=10)
output.grid(row=2, columnspan=8)

# запускаем главное окно
root.mainloop()


def inserter(value):
    """ Inserts specified value into text widget """
    output.delete("0.0","end")
    output.insert("0.0",value)


def handler():
    """ Get the content of entries and passes result to the output area """
    try:
        # make sure that we entered correct values
        a_val = float(a.get())
        b_val = float(b.get())
        c_val = float(c.get())
        inserter(solver(a_val, b_val, c_val))
    except ValueError:
        inserter("Make sure you entered 3 numbers")


but = Button(frame, text="Solve", command=handler).grid(row=1, column=7, padx=(10,0))

def clear(event):
    """ Clears entry form """
    caller = event.widget
    caller.delete("0", "end")


a.bind("<FocusIn>", clear)
b.bind("<FocusIn>", clear)
c.bind("<FocusIn>", clear)