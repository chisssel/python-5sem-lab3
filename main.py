class Static:
    @staticmethod
    def is_six(number):
        return number == 6

print(Static.is_six(2))
print(Static.is_six(6))


class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def get_value(self):
        return self.value

counter = Counter()
counter.increment()
counter.increment()
counter.decrement()
print(counter.get_value())



class Student:
    def __init__(self, first_name, second_name, age, year_institute):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.year_institute = year_institute

    def info(self):
        return f"Студент: {self.first_name} {self.second_name} Возраст: {self.age}, Курс: {self.year_institute}"

student = Student("Петр", "Ивашкин", 22, 3)
print(student.info())