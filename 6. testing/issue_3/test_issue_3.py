import unittest
from issue_3 import fit_transform


class TestFitTransform(unittest.TestCase):
    """Класс который тестирует функцию fit_transform"""
    def test_cities(self):
        items = ['Astana', 'New York', 'Astana', 'London']
        actual = fit_transform(items)
        expected = [
            ('Astana', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Astana', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_error(self):
        self.assertRaises(TypeError, fit_transform)

    def test_false(self):
        items = ['Isa', 'Aiko', 'Kala', 'IsaEra']
        actual = fit_transform(items)
        expected = [
            ('Isa', [0, 0, 0, 0, 1]),
            ('Aiko', [0, 0, 0, 1, 0]),
            ('Kala', [0, 0, 1, 0, 0]),
            ('IsaEra', [1, 1, 0, 0, 0]),
            ]
        # fake expected
        self.assertEqual(actual, expected)

    def test_name_true(self):
        items = ['Isa', 'Aiko', 'Kala', 'IsaEra', 'ErA']
        actual = fit_transform(items)
        expected = [
            ('Isa', [0, 0, 0, 0, 1]),
            ('Aiko', [0, 0, 0, 1, 0]),
            ('Kala', [0, 0, 1, 0, 0]),
            ('IsaEra', [0, 1, 0, 0, 0]),
            ('ErA', [1, 0, 0, 0, 0])
            ]
        self.assertGreaterEqual(actual, expected)


if __name__ == '__main__':
    TestFitTransform().test_name_true()
