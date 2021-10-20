n = int(input())
num_gen = (num for num in range(1, n + 1, 2))

print(*num_gen)
print(type(num_gen))
