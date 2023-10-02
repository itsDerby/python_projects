# grade = int(input("Enter the grade: "))
# if grade >= 90:
#     print('A')
# elif grade >= 80:
#     print('B')
# elif grade >= 70:
#     print('C')
# elif grade >=60:
#     print('D')
# elif grade < 60:
#     print('F')
#
#while
# product = 7
# while product <= 1000:
#     product = product * 7
#     print(product)

# for character in 'programming':
#     print(character , end= ' ')

# print (10, 20, 30, sep= '  ')

# grade = (98,76,71,87,83,90,57,79,82)
# total = 0
# gradeCounter = 0

# for grade in grade:
#     total = total + grade
#     gradeCounter = gradeCounter + 1
#     average = total/gradeCounter
#     print(f' Class average is {average}')
#
#
# for counter in range(10):
#     print(counter, end = '')

passes = 0
failures = 0
for student in range(10):
    result = int(input('Enter result(1 = pass, 2=fail):'))
    if result ==1:
        passes += passes
        if result ==2:
            failures +=failures
            print('Passed:', passes)
            print('Failed:',failures)
