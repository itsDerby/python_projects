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






