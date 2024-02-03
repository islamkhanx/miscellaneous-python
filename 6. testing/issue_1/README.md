# Запуск doctest

<p>Этот файл README описывает, как запустить тесты с использованием doctest в нашем проекте.</p>

---
## Шаг 1: Установка doctest

Если у вас еще нет doctest, вы можете установить его с помощью pip:

```pip install doctest```

## Шаг 2: Проверка докстрингов 
      
```python
def encode(message: str) -> str:
    """
    Кодирует строку в соответсвие с таблицей азбуки Морзе


    # doctest: +ELLIPSIS
    >>> encode('ISLAMKHAN')
    '.. ... .-.. .- -- -.- .... .- -.'
    >>> encode('AVITO ACADEMY')
    '.- ...- .. - --- ....... .- -.-. .- -.. . -- -.--'
    >>> encode('SOS')
    '... --- ...'
    >>> encode('Error')
    Traceback (most recent call last):
    ...
    KeyError: 'r'
    >>> encode('Fail')
    'some random stuf'
    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)

```

### Тесты
| Вход | Ожидаемый выход |
|------|-----------------|
|ISLAMKHAN|.. ... .-.. .- -- -.- .... .- -.|
|AVITO ACADEMY|.- ...- .. - --- ....... .- -.-. .- -.. . -- -.--|
|SOS|... --- ...|
|Error|KeyError: 'r'|
|Fail|some random stuf|

- В предпоследнем случае, слово "Error" вернет нам KeyError что мы и ожидаем от теста потому мы можем перевести только заглавные буквы
- В последнем мы ожидаем от него что то _('some random stuf')_ , но он выдаст KeyError и тест будет _исключенем_

## Шаг 3: Запуск doctest
<code> python -m doctest -v  issue_1/issue_1.py </code>

Тут
- ```-m``` флаг который обозначает что это модуль питона
- ```doctest``` имя модуля который мы используем
- ```-v``` флаг который дае детальный результат
- ```issue_1/issue_1.py``` путь к файлу модули которого будут тестироваться


##### Так же, важно отметить что мы используем директиву

В самом докскрипте функции ```encode``` мы написали ```# doctest: +ELLIPSIS```, что и позволяет нам использовать троеточие как здесь:
```python
>>> encode('Error')
    Traceback (most recent call last):
    ...
    KeyError: 'r'
```
