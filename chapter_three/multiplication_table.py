
for count in range(1, 13):
    for number in range(1, 21):

        print(f"{number:>2} * {count:>2} = {number * count:^4}",end="\t\t\t")

        # print(f'1*', number,  '=', result,  '2*', number, '= ', result, end='\t')
    print()

# for i in range(1,13):
#     print()
#     for j in range (1,21):
#         print(f'{i: >2} * {j: >2} = {i * j: ^4}', end='\t\t')