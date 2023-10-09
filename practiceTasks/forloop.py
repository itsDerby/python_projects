# names = ['Tobi', "Tolu", "Tosin", "Folake", "Titolomo"]
# name_with_t = []
# for name in names:
#     if "T" in name:
#         name_with_t.append(name)
# print(name_with_t)
#
# name_with_t = [name for name in names if "T" in name]
# print(name_with_t)
import random


# c= [3, 4, 5, 6]
# print(c)
# print(c[0])

# v= "hello"
# v[0] = "G"


# a_list = []
# for number in range (1,6):
#     a_list += [number]
# print(a_list)

# letters = []
# letters += "python"
# print(letters)

# list = [10,20,30]
# list2 = [40, 50, "bola"]
# l2= (list + list2)
#
# for i in range(len(l2)):
#     print(f"{i}: {l2[i]}")

# list1 = [40, 50, 60, 70, 80]
# list3 = [30, 50, 50]
# sum_list = list1 + list3
# for i in range(len(sum_list)):
#     print(f"{i}: {sum_list[i]}")

# def cube(values):
#
#     for i in range(len(values)):
#         values[i] **= 3
#     num = [1, 2, 3, 4, 5, 6, ]
#     print(i)
# total = 0
# for counter in range (0, 1000001):
#     total += counter
# print(total)

# total = 0
# for counter in [1, 2, 3, 4, 5]:
#     total += counter
# print(total)
#
# total = 0
# count = 0
# grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]
# for number in grades:
#     total += number
#     count += 1
# average = total/count
# print(f"{average}")
#
# import random
#
# for roll in range(10):
#     print(random.randrange(1, 7))

# def roll_dice():
#     die1 = random.randrange(1, 7)
#     die2 = random.randrange(1, 7)
#     die3 = random.randrange(1,7)
#     return die1, die2, die3


# print(roll_dice())

# tuple1 = (10, 20, 30, 40, 50)
# turr = reversed(tuple1)
# for i in turr:
#     print(i)
#
# tuple1 = (10, 20, 30, 40, 50)
#
# turple2 = ()
# turple2 = (reversed(tuple1)
# print(turple2)
#
# def reverse(numbers):
#     convert_reverse_to_list = []
#     reverseNumber = ()
#     for num in range(1, len(numbers) + 1):
#         convert_reverse_to_list.append(numbers[-num])
#
#     return reverseNumber
# print(reverse((1, 2, 3)))

lis = [2, 5, 6]
print(tuple(lis))