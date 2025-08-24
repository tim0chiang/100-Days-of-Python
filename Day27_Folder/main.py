from tkinter import *


def calculating():
    km_value.config(text=str(round(float(mile.get()) * 1.609344, 2)))


window = Tk()
window.geometry('300x100')
window.title('Kilometer Converter')

mile = Entry(width=5)
mile.grid(column=1, row=0)

text1 = Label(text=' Miles', font=('Arial', 10, 'bold'))
text1.grid(column=2, row=0)

text2 = Label(text='is equal to', font=('Arial', 10, 'bold'))
text2.grid(column=0, row=1)

km_value = Label(text='  0  ', font=('Arial', 10, 'bold'))
km_value.grid(column=1, row=1)

km = Label(text='km', font=('Arial', 10, 'bold'))
km.grid(column=2, row=1)

calculate = Button(text='Calculate', command=calculating)
calculate.grid(column=1, row=2)

window.mainloop()
