picture =[
[0, 0, 0, 1, 0, 0, 0],
[0, 0, 1, 1, 1, 0, 0],
[0, 1, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0]
]

# for number in range(0, len(picture)):
#     for row1 in picture[number]:
#
#         if row1 == 0:
#             print(end='')
#     else:
#         print("*")

for pixel in picture:
    print()
    for img in pixel:
        if img == 0:
            print(" " , end=' ')
        else:
            print("*" , end=' ')