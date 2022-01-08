from tkinter import Tk, Radiobutton, Button, Label, StringVar, IntVar, Entry


class TipCalculator:
    def __init__(self):
        window = Tk()
        window.title("Kalkulačka spropitného")
        window.configure(background="#1ba49c")
        window.geometry("375x250")
        window.resizable(width=False, height=False)

        self.cost = StringVar()
        self.tip_percent = IntVar()
        self.tip = StringVar()
        self.total_cost = StringVar()

        tip_percent = Label(window, text="Procento spropitného", bg="#ffd1b3", fg="black")
        tip_percent.grid(column=0, row=0, padx=15, pady=15)

        bill_amount = Label(window, text="Částka účtu", bg="white", fg="black")
        bill_amount.grid(column=1, row=0, padx=15)

        bill_amount_entry = Entry(window, textvariable=self.cost, width=14)
        bill_amount_entry.grid(column=2, row=0)

        five_percent_tip = Radiobutton(window, text="0.5%", variable=self.tip_percent, value=5)
        five_percent_tip.grid(column=0, row=1)
        ten_percent_tip = Radiobutton(window, text="10%", variable=self.tip_percent, value=10)
        ten_percent_tip.grid(column=0, row=2)
        fifteen_percent_tip = Radiobutton(window, text="15%", variable=self.tip_percent, value=15)
        fifteen_percent_tip.grid(column=0, row=3)
        twenty_percent_tip = Radiobutton(window,text="20%" ,variable=self.tip_percent, value=20)
        twenty_percent_tip.grid(column=0, row=4)
        twentyfive_percent_tip = Radiobutton(window, text="25%", variable=self.tip_percent, value=25)
        twentyfive_percent_tip.grid(column=0, row=5)
        thirty_percent_tip = Radiobutton(window, text="30%", variable=self.tip_percent, value=30)
        thirty_percent_tip.grid(column=0, row=6)

        tip_amount_lbl = Label(window,text ="Výše spropitného",bg="brown",fg="white")
        tip_amount_lbl.grid(column=1,row=3,padx=15)
        tip_amount_entry = Entry(window,textvariable =self.tip,width =14)
        tip_amount_entry.grid(column=2,row=3)

        window.mainloop()

TipCalculator()