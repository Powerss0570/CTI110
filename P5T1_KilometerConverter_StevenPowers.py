#Kilometer Converter Problem
#11/3/2019
#CTI-110-0007 P5T1_KilometerConverter
#Steven Powers


#This program converst kilometers to miles.
CONVERSTION_FACTOR = 0.6214

def main():
    #Get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

    #Display the distance converted to miles.
    show_miles(kilometers)

def show_miles(km):
    #Calculate miles.
    miles = km * 0.6214

    #Display the miles.
    print(km, 'kilometers equals', miles, 'miles.')

#Call the main function.
main()
