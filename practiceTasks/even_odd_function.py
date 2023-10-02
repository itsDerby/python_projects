# def even_odd_function(number):
#     if number % 2 == 0:
#         return 'even'
#     else:
#         return 'odd'
#
#
# print(even_odd_function(14))
#
#



def calculator():
    user_input = int(input("""
    1 Addition
    2 Subtraction
    3 Multiplication
    4 Division
    """))
    match(user_input):
        case 1:
           number1 = print('Enter the first number: ')
           number2 = print("Enter the second number: ")
           result = number1 + number2
           print(result)

        case 1:
            number1 = print('Enter the first number: ')
            number2 = print("Enter the second number: ")
            result = number1 - number2
            print(result)

        case 3:
            number1 = print('Enter the first number: ')
            number2 = print("Enter the second number: ")
            print(f'{ number1 / number2 } ')
        case 4:
            number1 = print('Enter the first number: ')
            number2 = print("Enter the second number: ")
            print(f'{ number1 * number2 } ')
        case 5:
            number1 = print('Enter the first number: ')
            number2 = print("Enter the second number: ")
            print(f'{number1 ** number2} ')


print(calculator())

