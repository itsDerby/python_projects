# print('number\t\tsquare\t\tcube')
# for number in range(1,11):
#     print(f'{number}\t\t\t{number ** 2}\t\t\t {number ** 3}')
#

print('number\tsquare\tcube')
number = 1
count = 1
while number <= 10:
    count = count +1
    print(f'{number}\t\t{number ** 2}\t\t{number ** 3}')
    number += 1
