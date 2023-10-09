numbers_in_list = [15, 20, 25, 20, 10, 5]
total = 0
for numbers in numbers_in_list:
    total += numbers
print(f"The total is  {total}")

multiply = 1
for numbers in numbers_in_list:
    multiply *= numbers
print(f"The multiplication of the numbers is : {multiply}")

largest = numbers_in_list[0]
for numbers in numbers_in_list:
    if numbers > largest:
        largest = numbers

print(f"The largest is {largest}")

smallest = numbers_in_list[0]
for number in numbers_in_list:
    if number < smallest:
        smallest = number
print(smallest)


duplicate = []
for numbers in numbers_in_list:
    if numbers not in duplicate:
        duplicate.append(numbers)
print(duplicate)
