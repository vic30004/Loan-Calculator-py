from tkinter import *


class LoanCalculator:
    def __init__(self):
        window = Tk()
        window.title("Loan Calculator")
        window.configure(background="black")
        # Labels for inputs
        Label(window, font='Helvetica 12 bold',
              text="Annual Interest Rate", bg="black", fg="white").grid(row=1, column=1, pady=10, padx=10, sticky=W)
        Label(window, font="Helvetica 12 bold", text="Number of Years", bg="black", fg="white").grid(
            row=2, pady=10, padx=10, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", text="Loan Amount", bg="black", fg="white").grid(
            row=3, column=1, pady=10, padx=10, sticky=W)
        Label(window, font="Helvetica 12 bold", text="Monthly Payment", bg="black", fg="white").grid(
            row=4, column=1, pady=10, padx=10, sticky=W)
        Label(window, font="Helvetica 12 bold", text="Total Payment", bg="black", fg="white").grid(
            row=5, column=1, pady=10, padx=10, sticky=W)

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
        lblMonthlyPayment = Label(window, textvariable=self.monthlyPaymentVar, bg="black", fg="white",
                                  justify=RIGHT).grid(row=4, column=2, sticky=E)
        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, font='Helvetica 12 bold', bg="black", fg="white",
                                textvariable=self.totalPaymentVar).grid(row=5, column=2, sticky=E)

        # Buttons
        btnComputePayment = Button(window, text="Compute Payment", bg="dark green", fg="white",
                                   font="Helvetica 14 bold", command=self.computePayment).grid(row=6, column=2, sticky=E)
        btClear = Button(window, text="Clear", bg="red", fg="white", font="Helvetica 14 bold",
                         command=self.delete_all).grid(row=6, column=8, padx=20, pady=20, sticky=E)

        window.mainloop()

        # Functions

    def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get()) / 1200,
            int(self.numberofYearsVar.get()))

        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
            * int(self.numberofYearsVar.get())

        self.totalPaymentVar.set(format(totalPayment, '10.2f'))

    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberofYears):
        monthlyPayment = loanAmount * monthlyInterestRate / \
            (1-1/(1+monthlyInterestRate) ** (numberofYears*12))
        return monthlyPayment

    def delete_all(self):
        self.monthlyPaymentVar.set("")
        self.loanAmountVar.set("")
        self.annualInterestRateVar.set("")
        self.numberofYearsVar.set("")
        self.totalPaymentVar.set("")


LoanCalculator()
