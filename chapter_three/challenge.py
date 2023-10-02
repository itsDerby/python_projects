# # name = "debby"
# # name2 = "ope"
# # print(f"{name} {name2}", end=' ')
#
# total = 0
# count = 0
# for number in [1,2,3,4,5]:
#     total += number
#     print(total)

total = 0
for number in range (1, 11):
    grade = int(input("Enter grade: "))
    total += grade
average = total/number
print(average)