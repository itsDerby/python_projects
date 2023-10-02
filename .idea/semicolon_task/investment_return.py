principal = int(input('Enter the amount invested: '))
annual_rate_return = 0.7
number_of_year = int(input('Enter the amount of year: '))
investment_return = principal * (1 + annual_rate_return)** number_of_year
print(investment_return)