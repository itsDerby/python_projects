stopper = -1
gallons_used = float(input('Enter the number of gallons used: '))
gallon_count = 0
miles_count = 0
miles_driven= float(input('Enter the miles used: '))
average = miles_driven / gallons_used
print(f'The miles/gallon for this tank was {average:.6f}')

user_response = int(input("Do you wish to continue? yes or no"))
while user_response != stopper:
    gallon_count += gallons_used
    miles_count += miles_driven
    gallons_used = float(input('Enter the number of galons used (-1 to end): '))
    miles_driven = float(input('Enter the miles used: '))
    average = miles_driven / gallons_used
    print(f'The miles/gallon for this tank was {average}')
    user_response = int(input("""Do you wish to continue? 
                                 press 1 to continue: 
                                 press -1 to end"""))

average2 = miles_count / gallon_count
print(f'The miles/gallon for this tank was {average2:.6f}')




