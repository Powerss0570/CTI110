# Create a python code for Bug collector.
# 10/12/2019
# CTI-110-0007 P4T2 - Bug Collector
# Steven Powers

# Define the variables.
total_bugs = 0

# Create the loop that asks the user for the amount of bugs collected each day.
for day in range(5) :
	bugs = int(input("How many bugs did you collect today?"))
	total_bugs += bugs
	
# Display the amount of bugs collected.
print("\nYou have collected", format(total_bugs, ",.0f"), "bugs.")
