def reverse_array(array):
    reverser = (len(array)) - 1
    number = 0
    array_reverse = []
    for number in range(reverser, -1, -1):
        array_reverse.append(array[number])

    return array_reverse


def largest_number(array):
    largest = array[0]
    for count in array:
        if count > largest:
            largest = count
    return largest


print(largest_number(2, 4, 5, 6))
