import pytest
from issue_4 import fit_transform


def test_cities():
    """Функция тестирует функцию fit_transform"""
    items = ['Astana', 'New York', 'Astana', 'London']
    actual = fit_transform(items)
    expected = [
        ('Astana', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Astana', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert actual == expected, 'They are not equal'


def test_error():
    """Функция тестирует функцию fit_transform"""
    with pytest.raises(TypeError):
        fit_transform()


def test_false():
    """Функция тестирует функцию fit_transform"""
    items = ['Isa', 'Aiko', 'Kala', 'IsaEra']
    actual = fit_transform(items)
    expected = [
        ('Isa', [0, 0, 0, 0, 1]),
        ('Aiko', [0, 0, 0, 1, 0]),
        ('Kala', [0, 0, 1, 0, 0]),
        ('IsaEra', [1, 1, 0, 0, 0]),
        ]
    # fake expected
    assert actual == expected, 'They are not equal'


def test_name_true():
    items = ['Isa', 'Aiko', 'Kala', 'IsaEra', 'ErA']
    actual = fit_transform(items)
    expected = [
        ('Isa', [0, 0, 0, 0, 1]),
        ('Aiko', [0, 0, 0, 1, 0]),
        ('Kala', [0, 0, 1, 0, 0]),
        ('IsaEra', [0, 1, 0, 0, 0]),
        ('ErA', [1, 0, 0, 0, 0])
        ]
    assert actual == expected, 'They are not equal'


if __name__ == '__main__':
    pass
