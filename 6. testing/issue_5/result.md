## Запуск
Почему то пришлость перейти в директорий с тестом <code>cd issue_5</code>

Теперь запускаем, логируя каверадж
<code>coverage run -m unittest discover</code>
Просмотрим результаты кавераджа в терминале
<code>coverage report -m</code>
Сохраним результаты кавераджа в html
<code>coverage html</code>

## Результат
```python
{'currentDateTime': '2022-11-15'}
.{'currentDateTime': '2021-11-15'}
.{'currentDateTime': '11.15.2019'}
.{'currentDateTime': '11/15/2019'}
.
----------------------------------------------------------------------
Ran 4 tests in 0.004s

OK
```

```python
Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
issue_5.py           20      0   100%
test_issue_5.py      28      0   100%
-----------------------------------------------
TOTAL                48      0   100%

```

```python
Wrote HTML report to htmlcov/index.html
```