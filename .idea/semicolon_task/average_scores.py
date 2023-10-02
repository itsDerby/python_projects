# count = 1
# total = 0
# average_score = 0
# while count <= 10:
#
#     score= int(input('Enter the score: '))
#     total += score
#     count = count + 1
#     average_score = total /10
# print(total)
# print(average_score)

# when the number of the time the loop will work is not known
total = 0
count = 0
score = int(input('Enter the student score or -1 to stop: '))
while score != -1:

    total += score
    count = count + 1
    score = int(input('Enter the student score or -1 to stop: '))
    average_score = total / count
print(total)
print (f'{average_score:.2f}')



# count = 0
# total = 0
#
# while count < 10:
#
#     score = int(input("enter the student score: "))
#
#     # to continue count loop
#     count = count + 1
#     # it can be augmented assignment
#     # After counting, I need total
#     total += score
# average = total / 10
#
# print(f'the total of scores by the student is {total} and the average score is {average}')
#
