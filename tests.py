import unittest

from main import Counter, Student, StandardShipping, ExpressShipping, FreeShipping


class TestStudent(unittest.TestCase):
    def test_info(self):
        student = Student("Анна", "Петрова",22, 4)
        self.assertEqual(student.info(), "Студент: Анна Петрова, Возраст: 22, Курс: 4")

class TestCounter(unittest.TestCase):
    def test_increment(self):
        counter = Counter()
        counter.increment()
        self.assertEqual(counter.get_value(), 1)

    def test_decrement(self):
        counter = Counter()
        counter.decrement()
        self.assertEqual(counter.get_value(), -1)

class TestPricingStrategy(unittest.TestCase):
    def test_standard_shipping_calculation(self):
        strategy = StandardShipping()
        cost = strategy.calculate_cost(1.0, 100)
        expected = 1.0 * 0.5 + 100 * 0.1
        self.assertEqual(cost, expected)

    def test_express_shipping_calculation(self):
        strategy = ExpressShipping()
        cost = strategy.calculate_cost(1.0, 100)
        expected = 1.0 * 1.0 + 100 * 0.3 + 10
        self.assertEqual(cost, expected)

    def test_free_shipping_calculation(self):
        strategy = FreeShipping()
        cost = strategy.calculate_cost(100, 100)
        self.assertEqual(cost, 0)