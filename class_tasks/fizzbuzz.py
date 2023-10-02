# multiples = 1
# multiples5 = 1
# count = 1
# for number in range(1, 51):
#     print(number)
# while number // 3:
#     print("Fizz")
# count = count + 1
# # multiples = 5 * number
# # print("Buzz")

number = 1
count = 1
while count <= 50:
    if count % 5 == 0 and count % 3 == 0:
        print("FizzBuzz")
    elif count % 3 == 0:
        print("Fizz")
    elif count % 5 == 0:
        print("Buzz")
    else:
        print(count)
    count = count + 1
