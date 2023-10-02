scores = []
for number in range (1,11):
    scores = int(input(f"Enter scores{number}: "))
    scores.append(scores)
largest_score = max(scores)
print(f"The largest score is: {largest_score}")
print()