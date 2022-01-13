import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

my_label = tkinter.Label(text="is equal to:")
my_label.grid(column=0, row=1)

new_label = tkinter.Label(text="Miles")
new_label.grid(column=2, row=0)

new1_label = tkinter.Label(text="Km")
new1_label.grid(column=2, row=1)

new2_label = tkinter.Label(text="0")
new2_label.grid(column=1, row=1)


def button_clicked():
    new2_label.config(text=float(input.get()) * 1.609344)


button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


input = tkinter.Entry(width=10)
input.grid(column=1, row=0)
input.focus()

window.mainloop()

