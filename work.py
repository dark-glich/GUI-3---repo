from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("pizza order")
root.configure(bg="white")
root.iconbitmap("mac_icon-icons.com_54610.ico")
root.geometry("600x600")

pizza = StringVar()
pizza.set("peperon")

TOPPINGS = [
    ("peperoni", " peperoni", 1),
    ("mushroom", " mushroom", 2),
    ("olives", " olive", 3),
    ("tomato", " tomato", 4),
    ("sausages", "sausages", 5),
    ("capsicum", "capsicum", 6)
]


def click(num):
    global e
    e = LabelFrame(frame, text="selected topping")
    e.grid(row=7, column=0)
    w = Label(e, text=num)
    w.grid(row=8, column=0)


def show():
    global im
    top = Toplevel()
    top.title("pizza order")
    top.iconbitmap("mac_icon-icons.com_54610.ico")
    im = ImageTk.PhotoImage(Image.open("2-2-pizza-png-pic (1).png"))
    label_im = Label(top, image=im)
    label_im.grid(row=0, column=0)
    butto = Button(top, text="exit", command=top.destroy, padx=30)
    butto.grid(row=1, column=0)


def pop():
    o = messagebox.askyesno("order complete", "are you sure you want to place your order?")
    label2 = Label(root, text=o)
    label2.grid_forget()
    if o == 1:
        label2 = Label(root, text="   your order has been placed   ")
        label2.grid(row=12, column=0)
    if o == 0:
        label2 = Label(root, text="          order not placed         ")
        label2.grid(row=12, column=0)


def pop2():
    z = messagebox.showinfo("order cancel", "are you sure you want to cancel your order")
    label3 = Label(root, text=z)
    label3.grid(row=12, column=0)
    if z == "ok":
        label3 = Label(root, text="your order has been cancelled")
        label3.grid(row=12, column=0)


fral = LabelFrame(root, text="add ons", padx=50, pady=50)
fral.grid(row=0, column=1)

drink = StringVar()
drink.set("def")

beverage = Radiobutton(fral, text="", variable=drink)


def dog():
    return


def good():
    if pa.get() == "on":
        cold_drinks = [
            ("Pepsi", "Pepsi", 3),
            ("sprite", "sprite", 4),
            ("Coca cola", "Coca cola", 5),
            ("mountain dew", "mountain dew", 6)
        ]
        for drinks, gdd, rowss in cold_drinks:
            beverage = Radiobutton(fral, text=drinks, variable=drink, value=gdd)
            beverage.grid(row=rowss, column=0)

    else:

        cold_drinks = [
            ("                        ", 3),
            ("                        ", 4),
            ("                         ", 5),
            ("                                 ", 6)
        ]
        for drinks, rowss in cold_drinks:
            beverage = Label(fral, text=drinks, )
            beverage.grid(row=rowss, column=0)


def change():
    vert = Label(root, text=ver.get())
    vert.grid(row=18, column=0)
    hort = Label(root, text=hor.get())
    hort.grid(row=17, column=0)
    root.geometry(str(ver.get()) + "x" + str(hor.get()))


frame = LabelFrame(root, text="topping", padx=50, pady=50)
frame.grid(row=0, column=0)

root.filename = filedialog.askopenfile(initialdir="/Users/hp/Downloads", title="choose a file"
                                       , filetypes=(("png files", "*.png"), ("jpg files", "*.jpg")))

label_click = Label(frame, text=root.filename)

label_click.grid(row=15, column=0)

for text, value, numi in TOPPINGS:
    i = Radiobutton(frame, text=text, value=value, variable=pizza, command=lambda: click(pizza.get()))
    i.grid(row=numi, column=0)

va = IntVar()
da = IntVar()
pa = StringVar()
c = Checkbutton(fral, text="add extra cheese", variable=va)
c.grid(row=0, column=0)
ce = Checkbutton(fral, text="add garlic bread", variable=da)
ce.grid(row=1, column=0)
che = Checkbutton(fral, text="add cold drink", variable=pa, onvalue="on", offvalue="off", command=good)
che.grid(row=2, column=0)
pa.get()

frap = LabelFrame(fral, text="size")
frap.grid(row=15, column=0)
dp = StringVar()
dp.set("size")
dro = Label(frap, text="choose the size of your pizza")
dro.grid(row=0, column=0)
drop = OptionMenu(frap, dp, "personal", "medium", "large")
drop.grid(row=1, column=0)
but = Button(frame, text="order", command=pop)
but.grid(row=9, column=0)

but2 = Button(frame, text="cancel order", command=pop2)
but2.grid(row=10, column=0)

butt = Button(frame, text="show pizza", command=show)
butt.grid(row=13, column=0)

ver = Scale(frame, from_=600, to=800, orient=HORIZONTAL)
ver.grid(row=12, column=0)

hor = Scale(frame, from_=600, to=800)
hor.grid(row=12, column=1)

e = Label(frame, text="")
e.grid(row=7, column=0)

w = Label(frame, text="")
w.grid(row=8, column=0)

vert = Label(root, text=ver.get())
vert.grid(row=17, column=0)

hort = Label(root, text=hor.get())
hort.grid(row=18, column=0)
verti = Button(root, text="change size", command=change)
verti.grid(row=16, column=0)

root.mainloop()
