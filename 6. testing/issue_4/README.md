# Запуск doctest

<p>Этот файл README описывает, как запустить тесты с использованием pytest тестов в нашем проекте.</p>

---
## Шаг 1: Установка pytest

Если у вас еще нет **pytest**, вы можете установить его с помощью pip:

```pip install -U pytest```

## Шаг 2: Проверка тестов 
      
```python
from issue_4 import fit_transform
import pytest


def test_cities():
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
    with pytest.raises(TypeError):
        fit_transform()


def test_false():
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


```
- ```from issue_4 import fit_transform``` модуль который тестируем
- ```import pytest``` декоратор в отором тесткейсы
- ```def test_...``` функции для тестирования

### Тесты
| Вход | Ожидаемый выход |
|['Astana', 'New York', 'Astana', 'London']|правильный ответ|
|__ничего__|TypeError|
|['Isa', 'Aiko', 'Kala', 'IsaEra']|неправильный ответ|
|['Isa', 'Aiko', 'Kala', 'IsaEra', 'ErA']|правильный ответ|

- Во втором случае __"ловим исключение"__ 
- В остальных случаях тестируем на равенство 

## Шаг 3: Запуск pytest
<code> python -m pytest -v issue_4/test_issue_4.py </code>

Тут
- ```-m``` флаг который обозначает что это модуль питона
- ```pytest``` имя модуля который мы используем
- ```-v``` флаг который дает детальный результат
- ```issue_4/test_issue_4.py``` путь к файлу где  тест



