largest_number = 0

count = 1
while count <= 3:
    number = int(input("Enter number: "))
    if number > largest_number:
        largest_number = number
        count += 1

        second_largest = number
    elif number != largest_number:
        second_largest = number
        count += 1
print(largest_number)
print(second_largest)