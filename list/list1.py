# # basket = []
# # basket [0] = "shirt"
# # basket [1] = 40
# # print(basket)
#
# basket = []
# basket.append("shirt")
# basket.append(40)
# print(basket)
# basket.append("trouser")
# print(basket[0])
# print(basket[1])
# print(basket[2])

# number = []


def multiply(*number):
    product = 1
    for i in number:
        product *= i
    return product


print(multiply(2, 3, 4, 5, 6))
