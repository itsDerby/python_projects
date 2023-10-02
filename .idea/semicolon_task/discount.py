print ('********************************')
print('        ','invoice','        ')
print ('********************************')
name_of_item = input('Name of Item: ')

price_of_item = int(input('Enter the price for the item: '))
credit_score = int(input('Do you have good credit score? press: 1. Yes 2. No  '))

if credit_score == 1:
    discount = price_of_item * 0.1
    deposit = price_of_item * 0.1
    discount1_in_percentage = 0.1 * 100
    print(f'Discount:   is {discount1_in_percentage}% ')
    print(f'Deposit:    is {deposit} ')

elif credit_score != 1:
    discount2 = price_of_item * 0.25
    discount2_in_percentage = 0.25 * 100
    deposit2 = price_of_item * 0.25

    print(f'Discount:       {discount2_in_percentage}% ')
    print(f'Deposit:        {deposit2} ')

print ('********************************')
