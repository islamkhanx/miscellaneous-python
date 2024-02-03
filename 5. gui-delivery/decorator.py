from functools import wraps
from numpy.random import randint
import time


def log(template='{}'):
    """Логирует время запросов
    все что мы пишем внутрь функции он отображает
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            execution_time = randint(1, 4)
            time.sleep(execution_time)
            print(f'\n{func.__name__}({"".join(args)})')
            print(f'{template.format(execution_time)}')
            return result
        return wrapper
    return decorator


@log('- Приготовили за {}с!🧑‍🍳')
def bake_fn(pizza: str):
    """Готовит пиццу"""
    pass


@log('- Доставили за {}с! 🛵 ')
def delivery_fn(pizza: str) -> str:
    """Доставляет пиццу"""
    return f"\nДоставили {pizza} ✅"


@log('- Забрали за {}с!🏠')
def pickup_fn(pizza: str) -> str:
    """Самовывоз"""
    return f"\nЗабрали {pizza} ✅"


if __name__ == '__main__':
    pizza_type = 'Pepperoni'
    result = delivery_fn(pizza_type)
    print(result)
