#Sales Prediction Python Code
#9/15/2019
#CTI-110 PST1 - Sales Prediction
#Steven Powers

# Get the projected total sales.
total_sales = float(input('Enter the projected sales: '))

# Calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23

# Display the profit
print('The profit is $', format(profit, ',.2f'))
