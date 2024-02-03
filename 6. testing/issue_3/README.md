# Запуск doctest

<p>Этот файл README описывает, как запустить тесты с использованием юнит тестов в нашем проекте.</p>

---
## Шаг 1: Установка 

Unittest идет вместе с пакетом питона поэтому он должно быть уже есть у вас

## Шаг 2: Проверка тестов 
      
```python
from issue_3 import fit_transform
import unittest


class TestFitTransform(unittest.TestCase):
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


```
- ```from issue_3 import fit_transform``` модуль который тестируем
- ```class TestFitTransform(unittest.TestCase):``` класс наследуется от ```unittest.TestCase``` и в котором тесткейсы 
- ```def test_...``` функции для тестирования

### Тесты
| Вход | Ожидаемый выход |
|['Astana', 'New York', 'Astana', 'London']|правильный ответ|
|__ничего__|TypeError|
|['Isa', 'Aiko', 'Kala', 'IsaEra']|неправильный ответ|
|['Isa', 'Aiko', 'Kala', 'IsaEra', 'ErA']|правильный ответ|

- В первом и третьем случае тестируем на равенство ```assertEqual```
- Во втором случае __"ловим исключение"__ ```assertRaises```
- В четвертом случае тестируем больше или равно ```assertGreaterEqual``` что может быть немного бессмысленно


## Шаг 3: Запуск unittest
<code> python -m unittest -v test_issue_3.py </code>

Тут
- ```-m``` флаг который обозначает что это модуль питона
- ```unittest``` имя модуля который мы используем
- ```-v``` флаг который дает детальный результат
- ```test_issue_3.py``` путь к файлу где тест



