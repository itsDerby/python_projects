rows = 6
for row in range(rows):
    for column in range(row):
        print("*", end=' ')
    print('')
rows = 6
for row in range(rows, 0, -1):
    for column in range(1, row + 1):
        print("*", end=' ')
    print('\r')