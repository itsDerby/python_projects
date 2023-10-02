# # # # # # # def average(scores):
# # # # # # #     total = 0
# # # # # # #     scores = int(input("Enter scores: "))
# # # # # # #     for i in scores:
# # # # # # #         total = scores + total
# # # # # # #         avg = len(scores)
# # # # # # #         average_sc = total / avg
# # # # # # #         return average_sc
# # # # # # #
# # # # # # #
# # # # # # # print(average())
# # # # # #
# # # # # # exam_score = []
# # # # # #
# # # # # #
# # # # # # def average_score(scores):
# # # # # #     return sum(scores) / len(scores)
# # # # # #
# # # # # #
# # # # # # for i in range(10):
# # # # # #     scores = int(input("Enter scores: "))
# # # # # #     exam_score.append(scores)
# # # # # #
# # # # # # print(average_score(exam_score))
# # # # #
# # # # # def average_score(*scores):
# # # # #     total = 0
# # # # #     for i in scores:
# # # # #         total += i
# # # # #         return total / len(scores)
# # # # #
# # # # # print(average_score(3,4,5,6,7,8))
# # # # #
# # # # # def me(name, number, age: int = 18) -> str:
# # # # #     x = 2 +3
# # # # #
# # # # # me ("joy", 2000, 21)
# # # # # me(number=2323, age = 21, name = "joy")
# # # # # name = 'joe'
# # # # # if name:
# # # # #     x = 2 +3
# # # # principal = int(input("Enter the principal: "))
# # # # rate = float(input("Enter rate: "))
# # # # # number_of_year = int(input("Enter the number of year: "))
# # # # rate = 1 + rate
# # # # for number in range (1,11):
# # # #
# # # #     amount = principal *(rate ** number)
# # # #
# # # #     print(f"{number:>2}{amount:>20.2f}")
# # # from _pydecimal import Decimal
# # #
# # # # tax = 6.25
# # # # bill_amount = 37.45
# # #
# # # print(f"Bill Total is {Decimal(37.45)} * {Decimal(1.0625):.2f}")
# #
# # for number in range (100):
# #     if number == 20:
# #         continue
# #     print(number)
#
# # a = b = 7
# # print('a' = a , '\nb =' , b)
# passes = 0
# failed = 0
# count = 1
# while count <= 10:
#     user_input = int(input("Enter either 1 or 2: "))
#     if user_input == 1:
#         passes = passes + 1
#         count += 1
#     elif user_input ==2:
#         failed = passes + 1
#         count += 1
# print(f"passes ={passes} , failed = {failed}")
#

print("number\tsquare\tcube")
for number in range (0, 6):
    print(f"{number:<8}{number * number:<8}{number *number* number:<8}")