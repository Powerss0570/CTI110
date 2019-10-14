#CTI-110-0007
#P3HW2 - MealTipTax
#Steven Powers
#10/6/2019

#Ask user to enter the charge for food
Meal = float(input("How much did your Meal cost?"))

#Ask user to enter the tip for Server
Tip = float(input("Enter the Tip for server either 16% or 18% or 20%?"))
defaulttip = .20
if Tip == 0.16 or Tip == 0.18 or Tip == 0.20:
    Tip_Amount = Meal * Tip
    Tax_Amount = Meal * 0.06
    Total_cost = Meal + Tax_Amount + Tip_Amount

    print('The calculated tip is $', Tip_Amount)

    print('The calculated tax is $', Tax_Amount)

    print('The calculated Total is $', Total_cost)


else:
    Tip_Amount2 = Meal * defaulttip
    Tax_Amount = Meal * 0.06
    Total_cost = Meal + Tax_Amount + Tip_Amount2
    print('Incorrect amount, defaulting to 20%')
    
    print('The calculated tip is $', Tip_Amount2)

    print('The calculated tax is $', Tax_Amount)

    print('The calculated Total is $', Total_cost)
