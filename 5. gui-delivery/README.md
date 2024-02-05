# pizza.py
Cli система заказа и доставки пиццы, по крайней мере подражает)

## Используем ООП
- опишем рецепты классами
- пусть будет два размера: `L` и `XL`
- метод `dict()` выводит рецепт в виде
словаря
- реализуйте пицц `__eq__()` для сравнения

### Рецепты

|Margherita 🧀 | Pepperoni 🍕 | Hawaiian 🍍|
|---|---|---|
tomato sauce|tomato sauce| tomato sauce
mozzarella|mozzarella| mozzarella 
tomatoes|pepperoni| chicken
||| pineapples

## Консоль (cli)
Для этого нам понадобится пакет `click`
```bash
$ pip install click
```


> [Click](https://pypi.org/project/click/) is a Python package for creating beautiful command line inter-faces in a composable way with as little code as necessary. It’s the “Command Line Interface Creation Kit”.


Для начала две команды:
- `order` — готовит пиццу, отправляет курьера
- `menu` — выводит меню

### Пример `order`
```bash
$ python cli.py order pepperoni -–delivery   
Приготовили за 2с!
🛵 Доставили за 1с!
```
Команда готовит пиццу, флаг –—delivery передает ее с курьером.

### Пример `menu`
Команда отображает доступное меню.
```bash
$ python cli.py menu
- Margherita 🧀 : tomato sauce, mozzarella, tomatoes
- Pepperoni 🍕 : ...
```
> **Бонус**: наши маркетологи утверждают, что пицца продается в два раза лучше, если у нее есть красивая иконка.

## Используйте ФП
Напишем декоратор, который выводит имя функции и время выполнения - `randint()`
```python
@log
def bake(pizza):
    """Готоит пиццу"""
    bake(Margherita())
    'bake - 2с'
```
Так же: декоратор принимает шаблон, в который подставляется время.

```python
@log('🛵 Доставили за {}c')
def delivery(pizza):
    """Доставляет пиццу"""

@log('🏠 Забрали за {}c')
def pickup(pizza):
    """Самовывоз"""

# delivery(Margarita)
# 🛵 Доставили за 2 c
```

## Требования 
- Тесты
- Аннотации
- Докстринги
- pep