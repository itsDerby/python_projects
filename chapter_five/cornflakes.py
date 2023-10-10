from copy import deepcopy


def reverse(numbers):
    reverse_to_list = []
    reverse_turple = ()
    for num in range(1, len(numbers) + 1):
        reverse_to_list.append(numbers[-num])
    for num in reverse_to_list:
        reverse_turple += (num,)
        print(reverse_to_list)
    return reverse_turple


def nested_tuple(numbers):
    number = []
    for count in range(len(numbers)):
        for count in range(count + 1, len(numbers)):
            firstnumber = numbers[0][1]
            secondnumber = numbers[1][2]
            number = (firstnumber, secondnumber)
    return number


def last_and_first_number(numbers):
    return None


def sorted_numbers():
    sorted = ()
    for count in range(len(numbers)):
        firstnumber = numbers[0]
        secondnumber = numbers[1]
        thirdnumber = numbers[2]
        forthnumber = numbers[3]
        sorted = ((thirdnumber, firstnumber), (forthnumber, secondnumber))
    return sorted
