from tkinter import *


class LoanCalculator:
    def __init__(self):
        window = Tk()
        window.title("Loan Calculator")
        window.configure(background="black")
        # Labels for inputs
        Label(window, font='Helvetica 12 bold', bg="light green",
              text="Annual Interest Rate").grid(row=1, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", text="Number of Years").grid(
            row=2, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", text="Loan Amount").grid(
            row=3, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", text="Monthly Payment").grid(
            row=4, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", text="Total Payment").grid(
            row=5, column=1, sticky=W)

        # Inputs
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable=self.annualInterestRateVar,
              justify=RIGHT).grid(row=1, column=2)
        self.numberofYearsVar = StringVar()
        Entry(window, textvariable=self.numberofYearsVar,
              justify=RIGHT).grid(row=2, column=2)
        self.loanAmountVar = StringVar()
        Entry(window, textvariable=self.loanAmountVar,
              justify=RIGHT).grid(row=3, column=2)
        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, textvariable=self.monthlyPaymentVar,
                                  justify=RIGHT).grid(row=4, column=2, sticky=E)
        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, font='Helvetica 12 bold', bg="light green",
                                textvariable=self.totalPaymentVar).grid(row=5, column=2, sticky=E)


LoanCalculator()
