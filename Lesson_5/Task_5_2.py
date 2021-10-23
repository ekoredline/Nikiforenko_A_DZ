
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
src_1 = []

for i in src:
    b = 0
    for j in src:
        if i == j:
            b += 1
    if b == 1:
        src_1.append(i)

print(src_1)
