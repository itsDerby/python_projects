investment = int(input('Enter the amount you have invested: '))

for count in range(1, 31):

    roi = 0.1 * investment
    total = investment + roi
    investment = total

    print(f'Your ROI is now ${roi:.2f} your investment is ${total:.2f} in year{count: <5} ')
