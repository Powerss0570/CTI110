#CTI-110-0007
#P3HW1 - Month number
#Steven Powers
#10/6/2019

# Get a month entry from the user.
Input_month = int(input('Enter your Month entry; '))

# Determine the month.
if Input_month==1:
    print('Your month is January.')
if Input_month==2:
    print('Your month is February.')
if Input_month==3:
    print('Your month is March.')
if Input_month==4:
    print('Your month is April.')
if Input_month==5:
    print('Your month is May.')
if Input_month==6:
    print('Your month is June.')
if Input_month==7:
    print('Your month is July.')
if Input_month==8:
    print('Your month is August.')
if Input_month==9:
    print('Your month is September.')
if Input_month==10:
    print('Your month is October.')
if Input_month==11:
    print('Your month is November.')
if Input_month==12:
    print('Your month is December.')
elif Input_month<1:
    print('Invalid Entry.')
elif Input_month>12:
    print('Invalid Entry.')
