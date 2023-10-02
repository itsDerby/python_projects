# password = input("Enter your password: ")
# hidden_password =len(password) * '*'
# # print(hidden_password)

# age = int(input('Enter an age: '))
# if age < 18:
#     print("You're not eligible to enter our club...")
# else:
#     print("Eligible")
# #     or use a ternary operator
# result = "Not Eligible" if age < 18 else "Eligible"
# print(result)
# # or use a match case
# match age:
#     case (age == 18):
#         print("Not eligible")

# new topic
# language = input('Enter your language: ')
# match language.lower():
#     # lower - this method will convert all input to lower case
#     case "yoruba":
#         print("Welcome to Ibadan")
#     case "Ibo":
#         print("Welcome to Anambra")
#     case "Hausa":
#         print("Welcome to Kano")
#     case _:
#         print("You're not from here")

#NEW TOPIC

# score = int(input("Enter your score:"))
# result =" "
# if score >= 90 and score <= 100:
#     result = "Distinction"
#
# elif 80 <= score < 90:
#     result = "Excellent"
#
# elif score >= 70 and score < 80:
#     result = "B grade"
#
# elif score >= 60 and score < 70:
#     result = "C grade"
#
# elif score >=50 and score < 60:
#     result = "D grade"
#
#
# else:
#     result = "Fail, come back next time"

# print(f'your score is {score} and your result is {result}')

import random
# _precious = random.randint(1,21)
# print(_precious)

count = 0
while count < 10:
    print(random.randint(1, 21))
    count += 1

print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))

