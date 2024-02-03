# Запуск doctest

<p>Этот файл README описывает, как запустить тесты с использованием mock тестов в нашем проекте.</p>

---
## Шаг 1: Установка pytest

Если у вас еще нет **coverage**, вы можете установить его с помощью pip:

```pip install -U coverage```

## Шаг 2: Проверка тестов 
      
```python
import unittest
from unittest.mock import Mock, patch
from issue_5 import what_is_year_now
import json


class TestWhatIsYearNow(unittest.TestCase):

    @patch('urllib.request.urlopen')
    def test_what_year_1(self, mock_urlopen):
        mock_resp = mock_urlopen.return_value.__enter__.return_value
        mock_resp.read.return_value = json.dumps(
            {'currentDateTime': '2022-11-15'}).encode('utf-8')
        result = what_is_year_now()
        self.assertEqual(result, 2022)

    @patch('urllib.request.urlopen')
    def test_what_year_2(self, mock_urlopen):
        mock_resp = mock_urlopen.return_value.__enter__.return_value
        mock_resp.read.return_value = json.dumps(
            {'currentDateTime': '2021-11-15'}).encode('utf-8')
        result = what_is_year_now()
        self.assertEqual(result, 2021)

    @patch('urllib.request.urlopen')
    def test_what_year_3(self, mock_urlopen):
        mock_resp = mock_urlopen.return_value.__enter__.return_value
        mock_resp.read.return_value = json.dumps(
            {'currentDateTime': '11.15.2019'}).encode('utf-8')
        result = what_is_year_now()
        self.assertEqual(result, 2019)

    @patch('urllib.request.urlopen')
    def test_what_year_4(self, mock_urlopen):
        mock_resp = mock_urlopen.return_value.__enter__.return_value
        mock_resp.read.return_value = json.dumps(
            {'currentDateTime': '11/15/2019'}).encode('utf-8')
        self.assertRaises(ValueError, what_is_year_now)


```
- ```from issue_5 import what_is_year_now``` модуль который тестируем
- ```import unittest```, ```from unittest.mock import Mock, patch``` инструменты которые используем
- ```def test_...``` функции для тестирования

### Тесты
| Вход | Ожидаемый выход |
|2021-11-15|2021|
|2022-11-15|2022|
|11.15.2019|2019|
|11/15/2019|ValueError|

- Во последнем случае __"ловим исключение"__ 
- В остальных случаях тестируем на равенство 

## Шаг 3: Запуск c coverage
<code> coverage run -m unittest  discover </code>

Тут
- ```-m``` флаг который обозначает что это модуль питона
- ```tunittest``` имя модуля который мы используем
