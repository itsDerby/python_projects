digits = int(input("ENTER FIVE INTEGERS: "))
first_number = digits // 10000
second_number = digits // 1000 % 10
third_number = digits // 100 % 10
fourth_number = digits // 10 % 10
fifth_number = digits % 10

print (first_number , second_number, third_number, fourth_number, fifth_number)