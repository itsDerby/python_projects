number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))
number3 = int(input('Enter the third number: '))
sum = number1 + number2 + number3
average = sum/3
product = number1 * number2 * number3

if number1 < number2  and number1 < number3:
    print(number1 , 'is the smallest')
if number2 < number1 and number2 < number3:
    print(number2 , 'is the smallest')
if number3 < number1 and number3 < number2:
    print(number3 , 'is the smallest')

if number1 > number2  and number1 > number3:
    print(number1 , 'is the highest')
if number2 > number1 and number2 > number3:
    print(number2 , 'is the highest')
if number3 > number1 and number3 > number2:
    print(number3 , 'is the highest')


