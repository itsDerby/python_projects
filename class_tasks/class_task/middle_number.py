import statistics

ls = [10, 20, 15, 25, 5, 30, 35, 20, 10, 20]
for i in range(len(ls)):
    for j in range(i + 1, len(ls)):
        if ls[i] > ls[j]:
            print(ls)
            ls[i], ls[j] = ls[j], ls[i]

print(ls)
l= len(ls)

if l % 2 ==1:
    m1 =ls[l // 2]
    m2 = ls[(l // 2) - 1]
    mid = (m1 + m2) /2
    print(f"The median is", mid)
else:
    mid = ls[l//2]
    print(f"The median is", mid)

mean1 = len(ls) / 10
print(f"The mean is", mean1)

mean = statistics.mean(ls)
print(mean)


