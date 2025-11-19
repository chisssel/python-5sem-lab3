numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Исходный список:", numbers)
print("Чётные числа:", even_numbers)