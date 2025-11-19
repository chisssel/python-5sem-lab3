def filter_data_from_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            number = int(line.strip())
            if number % 2 == 0:
                yield number

for num in filter_data_from_file("numbers.txt"):
    print(num, end=' ')