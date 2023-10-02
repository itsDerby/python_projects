number1 = int(input("Enter the first Number: "))
number2 = int(input("Enter the Second Number: "))
number3 = int(input("Enter the third Number: "))

if number1 > number2 and number1 >number3:
    print(number1, " is greater")
if number2 > number1 and number2 > number3:
    print(number2,  " is greater")
if number3 > number1 and  number3 > number2:
    print (number3, " is greater")