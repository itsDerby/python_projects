print("number\t\tsquare\t\tcube")
for number in range (6):
    print(number, end='\t\t\t')
    square = number*number
    cube = number*number*number
    print(square , end='\t\t\t')
    print(cube)