def my_reduce(func, iterable, initializer=None):
    it = iter(iterable)

    if initializer is None:
        value = next(it)
    else:
        value = initializer

    for element in it:
        value = func(value, element)
    return value


numbers = [1, 2, 3, 4, 5]
total = my_reduce(lambda x, y: x + y, numbers)
print(f"Сумма чисел {numbers} = {total}")


max_number = my_reduce(lambda x, y: x if x > y else y, numbers)
print(f"Максимальное число в {numbers} = {max_number}")