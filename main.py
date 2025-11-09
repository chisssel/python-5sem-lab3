from abc import abstractmethod, ABC


class Static:
    @staticmethod
    def is_six(number):
        return number == 6

print(Static.is_six(2))
print(Static.is_six(6), "\n")


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
print(counter.get_value(), "\n")


class Student:
    def __init__(self, first_name, second_name, age, year_institute):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.year_institute = year_institute

    def info(self):
        return f"Студент: {self.first_name} {self.second_name} Возраст: {self.age}, Курс: {self.year_institute}"

student = Student("Петр", "Ивашкин", 22, 3)
print(student.info(), "\n")




class ShippingStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, weight, distance):
        pass


class StandardShipping(ShippingStrategy):
    def calculate_cost(self, weight, distance):
        return weight * 0.5 + distance * 0.1


class ExpressShipping(ShippingStrategy):
    def calculate_cost(self, weight, distance):
        return weight * 1.0 + distance * 0.3 + 10


class FreeShipping(ShippingStrategy):
    def calculate_cost(self, weight, distance):
        return 0


class Order:
    def __init__(self, items, shipping_strategy: ShippingStrategy):
        self.items = items
        self.shipping_strategy = shipping_strategy

    def calculate_total(self):
        items_cost = sum(cat['price'] for cat in self.items)
        total_weight = sum(cat['weight'] for cat in self.items)
        shipping_cost = self.shipping_strategy.calculate_cost(total_weight, 100)

        return items_cost + shipping_cost


items = [
    {'name': 'Книга', 'price': 15, 'weight': 0.5},
    {'name': 'Футболка', 'price': 25, 'weight': 0.3}
]

standard_order = Order(items, StandardShipping())
express_order = Order(items, ExpressShipping())
free_order = Order(items, FreeShipping())

print(f"Итог со стандартной доставкой: ${standard_order.calculate_total()}")
print(f"Итог с экспресс доставкой: ${express_order.calculate_total()}")
print(f"Итог с бесплатной доставкой: ${free_order.calculate_total()}")