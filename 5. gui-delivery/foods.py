class Food():
    """Класс с рецептами"""

    def __init__(self, name: str, recipe: tuple, size: str = 'L'):
        """Функция записывает блюдо в класс
        Аргументы:
            name (str): название пиццы
            recipe (str): ингридиеты пиццы в киде кортежа
            size (str, optional): Размер XL или L. Defaults to 'XL'.
        """
        self.name = name
        self.recipe = recipe
        self.size = size if size in ('XL', 'L') else 'L'

    def dict(self) -> dict[str, str]:
        """Возврашает рецепт пиццы в виде словаря"""
        return {str(self.name): ", ".join(self.recipe)}

    def __str__(self) -> str:
        """Возвращает название пиццы для принта и тд"""
        return self.name

    def __eq__(self, other):
        """Сравнивает два объекта Food по атрибутам"""
        if isinstance(other, Food):
            return (
                self.name == other.name and
                self.recipe == other.recipe and
                self.size == other.size
            )
        return False


margherita = Food(
    'Margherita🧀',
    (
        'mozzarella',
        'tomatoes',
        'tomato sauce',
    ),
    'XL')

pepperoni = Food(
    'Pepperoni🍕',
    (
        'mozzarella',
        'pepperoni',
        'tomato sauce',
    ),
    'XL')

hawaiian = Food(
    'Hawaiian🍍',
    (
        'mozzarella',
        'chicken',
        'tomato sauce',
        'pineapples',
    ),
    'XL')

MENU = [margherita, pepperoni, hawaiian]  # Храним тут доступные интсансы пицц

if __name__ == '__main__':
    print(*list(map(str, MENU)))
    print(pepperoni.dict())
    print(margherita == pepperoni)
