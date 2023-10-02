for row in range (1, 11):
    for column in range(row -1):
        print("*", end=' ')
    print("*")

for row in range(1, 11):
    for column in range(10-row):
        print("*", end=' ')
    print("*")

for row in range(1, 11):
    for column in range(10-row):
        print("*", end='')
    print("*")

