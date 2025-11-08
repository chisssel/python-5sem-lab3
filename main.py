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