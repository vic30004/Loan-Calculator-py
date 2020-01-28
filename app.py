from tkinter import *


class LoanCalculator:
    def __init__(self):
        window = Tk()
        window.title("Loan Calculator")
        window.configure(background="black")
        Label(window, font='Helvetica 12 bold', bg="light green",
              text="Annual Interest Rate").grid(row=1, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", Text="Number of Years").grid(
            row=2, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", Text="Loan Amount").grid(
            row=3, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", Text="Monthly Payment").grid(
            row=4, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", Text="Total Payment").grid(
            row=5, column=1, sticky=W)
