payroll_name = input("Enter Payroll Name: ")
hours_worked = int(input("Enter Pay Rate: "))
pay_rate= int(input('Enter Gross Pay Amount: '))

gross_pay = hours_worked * pay_rate
input('deductions: ')
federal_withholding = gross_pay * 0.2
print(federal_withholding)
state_withholding = 0.09 * gross_pay
print(state_withholding)
total_reduction = federal_withholding + state_withholding
print(total_reduction)
net_pay = gross_pay - total_reduction
print(net_pay)
