def reverse_array(array):
    reverser = (len(array)) - 1
    number = 0
    array_reverse = []
    for number in range(reverser, -1, -1):
        array_reverse.append(array[number])

    return array_reverse


num = [4,6,5,4,3,2,1]
print(reverse_array(num))

