total = 0
count = 1
product = 1

while count < 4:
    numbers = int(input("Enter the number:"))
    total = total + numbers
    product = product * numbers
    count += 1
average = total/count
largest = numbers
smallest = 0
if numbers > largest:
    largest = numbers
if numbers < smallest:
    smallest = numbers
print("average = ", average)
print("total = ", total)
print("Product = ", product)
print("Largest = ", largest)
print("Smallest = ", smallest)