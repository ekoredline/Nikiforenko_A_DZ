#Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield

n = int(input())
num_gen = (num for num in range(1, n + 1, 2))

print(*num_gen)
print(type(num_gen))
