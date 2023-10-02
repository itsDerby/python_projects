binary = input("Enter a binary number: ")
decimal = 0

for i in range(len(binary)):
    digit = int(binary[i])
    decimal += digit * 2**(len(binary)-1-i)

print("Decimal equivalent:", decimal)