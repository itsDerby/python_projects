numbers = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))
number3 = int(input('Enter the third number: '))

if numbers < number2:
    print(numbers)
elif number2 < numbers:
    print(number2)
elif number2 < number3:
    print(number3)

if numbers > number2:
    print(numbers)
elif number2 > numbers:
    print(number2)
elif number2 > number3:
    print(number3)


