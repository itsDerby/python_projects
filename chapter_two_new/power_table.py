rows = 5
column = 3
power =1
print('a   b     pow(a,b)')
for rows in range(1,6):
    for column in range(1, 2):
        column = rows+1
        power = rows ** column
    print(rows, end='   ')
    print(column, end='       ')
    print(power, end='    ')
    print()

