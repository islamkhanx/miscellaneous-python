# Запуск doctest

<p>Этот файл README описывает, как запустить тесты с использованием параметрческих тестов в нашем проекте.</p>

---
## Шаг 1: Установка pytest

Если у вас еще нет **pytest**, вы можете установить его с помощью pip:

```pip install -U pytest```

## Шаг 2: Проверка тестов 
      
```python
from issue_2 import decode
import pytest


@pytest.mark.parametrize(
    'source_string, result',
    [
        (' -.-. .... . . ... .', 'CHEESE'),
        ('-.-. .- - / .. ...', 'cat is'),
        ('.-. .- .. -.', 'RAIN'),
    ],
)
def test_morse_decode(source_string, result):
    assert decode(source_string) == result

```
- ```from issue_2 import decode``` модуль который тестируем
- ```@pytest.mark.parametrize``` декоратор в отором тесткейсы
- ```def test_morse_decode``` функция для тестирования

### Тесты
| Вход | Ожидаемый выход |
|------|-----------------|
|-.-. .... . . ... .|CHEESE|
|-.-. .- - / .. ...|cat is|
|.-. .- .. -.|RAIN|

- В предпоследнем случае, слово "cat is" вернет нам KeyError что мы и ожидаем от теста потому мы не можем переводить "/"


## Шаг 3: Запуск pytest
<code> python -m pytest -v issue_2/test_issue_2.py </code>

Тут
- ```-m``` флаг который обозначает что это модуль питона
- ```pytest``` имя модуля который мы используем
- ```-v``` флаг который дает детальный результат
- ```issue_2/test_issue_2.py``` путь к файлу где  тест



