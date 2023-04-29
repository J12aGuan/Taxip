from tkinter import *

#Value Set
Tem_Amount = 0
tip_Amount = 0

Button_Space = 1
Text_Space = 1
Entry_Space = 1

def California_Tip():
    Amount = float(Tem_Amount)
    Tip_temp = float(tip_Amount)
    Tax_amount = Amount * 0.0882
    Tax_amount1 = round(Tax_amount, 2)
    TotalAmount = Amount + Tax_amount1
    tax_str = str(Tax_amount1)
    Total_Amount = str(TotalAmount)
    Tax.config(text = "Tax Amount: " + tax_str)
    Final_Amount.config(text = "Total Amount: " + Total_Amount)
    Tip_temp = Tip_temp * 0.01
    Tip_final = Tip_temp * TotalAmount
    Tip_final1 = round(Tip_final, 2)
    Tip_string = str(Tip_final1)
    Tip_Output.config(text = "Tip Amount: " + Tip_string)
    After_tip_total = Tip_final1 + TotalAmount
    After_tip_total_str = str(After_tip_total)
    After_tip.config(text = "After Tip: " + After_tip_total_str)

def Texas_Tip():
    Amount = float(Tem_Amount)
    Tip_temp = float(tip_Amount)
    Tax_amount = Amount * 0.0625
    Tax_amount1 = round(Tax_amount, 2)
    TotalAmount = Amount + Tax_amount1
    tax_str = str(Tax_amount1)
    Total_Amount = str(TotalAmount)
    Tax.config(text = "Tax Amount: " + tax_str)
    Final_Amount.config(text = "Total Amount: " + Total_Amount)
    Tip_temp = Tip_temp * 0.01
    Tip_final = Tip_temp * TotalAmount
    Tip_final1 = round(Tip_final, 2)
    Tip_string = str(Tip_final1)
    Tip_Output.config(text = "Tip Amount: " + Tip_string)
    After_tip_total = Tip_final1 + TotalAmount
    After_tip_total_str = str(After_tip_total)
    After_tip.config(text = "After Tip: " + After_tip_total_str)

def onclick():
    Amount = Total.get()
    try:
        global Tem_Amount
        Tem_Amount = float(Amount)
        Total.delete(0,"end")
        Text.config(text = "Number Recieved")
    except:
        Total.delete(0,"end")
        Text.config(text="Not a number")

def onclick1():
    tip = Tip.get()
    try:
        global tip_Amount
        tip_Amount = float(tip)
        Tip.delete(0,"end")
        Text1.config(text = "Number Recieved")
    except:
        Tip.delete(0,"end")
        Text1.config(text="Not a number")

window = Tk()
window.title("Taxip")                           #Name it "PhysicsCalculator"
window.geometry("800x450")

Space = Label(window, text = "")
Space.pack()

Total = Entry(window, width=20)
Total.pack(padx = Entry_Space, pady = Entry_Space)
Total.focus()

Text = Label(window, text = "Enter The Total Amount")
Text.pack(padx = Text_Space, pady = Text_Space)

Tip = Entry(window, width=20)
Tip.pack(padx = Entry_Space, pady = Entry_Space)

Text1 = Label(window, text = "Enter The Tip Percentage")
Text1.pack(padx = Text_Space, pady = Text_Space)

Submit = Button(window, text = "Submit", command = lambda:[onclick(), onclick1()], font = ("Comic Sans", 15), width = "15")
Submit.pack(padx = Button_Space, pady = Button_Space)

California = Button(window, text = "California", command = California_Tip, font = ("Comic Sans", 15), width = "15")
California.pack(padx = Button_Space, pady = Button_Space)

Texas = Button(window, text = "Texas", command = Texas_Tip, font = ("Comic Sans", 15), width = "15")
Texas.pack(padx = Button_Space, pady = Button_Space)

Tax = Label(window, text = "Amount Of Tax")
Tax.pack(padx = Text_Space, pady = Text_Space)

Final_Amount = Label(window, text = "Total Amount")
Final_Amount.pack(padx = Text_Space, pady = Text_Space)

Tip_Output = Label(window, text = "Tip Amount")
Tip_Output.pack(padx = Text_Space, pady = Text_Space)

After_tip = Label(window, text = "After Tip")
After_tip.pack(padx = Text_Space, pady = Text_Space)

window.mainloop()                                           #Create a window
