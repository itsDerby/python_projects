def add_function(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def multiply(numbers):
    multiplyNumber = 1
    for num in numbers:
        multiplyNumber *= num
    return multiplyNumber


def largest(numbers):
    maxi = numbers[0]
    for num in numbers:
        if num > maxi:
            maxi = num

            return maxi
