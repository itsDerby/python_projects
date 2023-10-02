employee_name = input("Enter employee name name:")
number_of_hours = int(input("Enter number of hours worked in a week:"))
pay_rate = float(input("Enter hourly pay rate:"))
month = input("Month:")
federal_rate = float(input("Enter the federal tax withholding rate:"))
state_rate = float(input("Enter_state_tax_withholding_rate:"))


gross_pay = number_of_hours * pay_rate
federal_withholding = gross_pay * (federal_rate / 100)
state_withholding = gross_pay * (state_rate / 100)
total_deduction = federal_withholding + state_withholding
net_pay = gross_pay - total_deduction


print("\n\n")
print("{} Payroll statement for the month of {}".format(employee_name, month))
print("Employees name:",employee_name)
print("Number of hours worked in a week:",number_of_hours)
print("Hourly pay rate:$",pay_rate)
print("Gross pay:$",gross_pay)
print("Month",month)
print("Federal tax withholding rate({}%):".format(federal_rate),federal_withholding)
print("State tax withholding rate:",state_rate )
print("Total Deduction:$",total_deduction)
print("Net pay:$",net_pay)