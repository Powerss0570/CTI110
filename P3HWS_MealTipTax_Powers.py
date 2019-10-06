#CTI-110-0007
#P3HW2 - MealTipTax
#Steven Powers
#10/6/2019

#Ask user to enter the charge for food
Meal = float(input("How much did your Meal cost?"))

#Ask user to enter the tip for Server
Tip = float(input("Enter the Tip for server either 16% or 18% or 20%?"))

#Ask use to enter the Tax Amount
Tax = float(input("Enter the Tax amount for Meal"))

#Calculate tip and tax
total_cost = Meal

#Display total cost of Meal
print("Your total Meal cost:$ %.2f" % total_cost)

if Tip==Meal * 0.16:
    print('The calculated tip is $', Meal * 0.16)
if Tip==Meal * 0.18:
    print('The calculated tip is $', Meal * 0.18)
if Tip==Meal * 0.20:
    print('The calculated tip is $', Meal * 0.20)
if Tip<=0.15:
    print('Error')
if Tip==0.17:
    print('Error')
if Tip==0.19:
    print('Error')
if Tip>=0.21:
    print('Error')

print('The calculated tax is $', Meal * 0.06)
print('The total cost of the meal is $', total_cost + (total_cost * 0.16) + (total_cost * 0.06))
print('Above is Total with 16% Tip')
print('The total cost of the meal is $', total_cost + (total_cost * 0.18) + (total_cost * 0.06))
print('Above is Total with 18% Tip')
print('The total cost of the meal is $', total_cost + (total_cost * 0.20) + (total_cost * 0.06))
print('Above is Total with 20% Tip')





