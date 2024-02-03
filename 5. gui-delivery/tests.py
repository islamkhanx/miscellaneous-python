import unittest
from unittest.mock import patch
from io import StringIO
from foods import Food
from decorator import bake_fn, delivery_fn, pickup_fn


class TestFoodMethods(unittest.TestCase):
    "Класс с тестами методов Food"

    class FoodFake(Food):
        "Копия Food что бы не заполнять его"
        def __init__(self, name, recipe, size):
            super().__init__(name, recipe, size)

    pepperoni = FoodFake(
        'Pepperoni🍕',
        (
            'mozzarella',
            'pepperoni',
            'tomato sauce',
        ),
        'XL')

    hawaiian = FoodFake(
        'Hawaiian🍍',
        (
            'mozzarella',
            'chicken',
            'tomato sauce',
            'pineapples',
        ),
        'XL')

    def test_food_str(self, hawaiian=hawaiian):
        actual = str(hawaiian)
        expected = 'Hawaiian🍍'
        self.assertEqual(actual, expected)

    def test_food_dict(self, pepperoni=pepperoni):
        actual = pepperoni.dict()
        expected = {'Pepperoni🍕': 'mozzarella, pepperoni, tomato sauce'}
        self.assertEqual(actual, expected)

    def test_food_equal(self, hawaiian=hawaiian, pepperoni=pepperoni):
        actual = (hawaiian == pepperoni)
        expected = False
        self.assertEqual(actual, expected)

    def test_food_equal2(self, hawaiian=hawaiian):
        actual = (hawaiian == 5)
        expected = False
        self.assertEqual(actual, expected)


class TestLogDecorator(unittest.TestCase):
    def setUp(self):
        self.mock_stdout = StringIO()
        patch('sys.stdout', self.mock_stdout).start()

    def tearDown(self):
        patch.stopall()

    def test_bake_fn_log(self):
        with patch('time.sleep', return_value=None):
            bake_fn('Pepperoni')
            output = self.mock_stdout.getvalue().strip()
        self.assertIn('bake_fn(Pepperoni)', output)
        self.assertIn('Приготовили за', output)

    def test_delivery_fn_log(self):
        with patch('time.sleep', return_value=None):
            delivery_fn('Pepperoni')
            output = self.mock_stdout.getvalue().strip()
        self.assertIn('delivery_fn(Pepperoni)', output)
        self.assertIn('Доставили за', output)

    def test_pickup_fn_log(self):
        with patch('time.sleep', return_value=None):
            pickup_fn('Pepperoni')
            output = self.mock_stdout.getvalue().strip()
        self.assertIn('pickup_fn(Pepperoni)', output)
        self.assertIn('Забрали за', output)
