average = 1
gallon_count = 0
gallons = float(input("Enter the gallons used or press -1 to end: "))
miles = float(input('Enter the miles driven: '))
while gallons != -1:
    average = miles/gallons
    gallon_count += 1
    
    average = miles / gallons
    print(average/gallon_count)
    gallon_count += 1