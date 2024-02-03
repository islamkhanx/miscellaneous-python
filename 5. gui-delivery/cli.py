import click
from foods import MENU
from decorator import delivery_fn, pickup_fn, bake_fn


@click.group()
def cli():
    pass


@cli.command()
def menu():
    """Показать меню"""
    click.echo("Наше меню:")
    for pizza in MENU:
        name = pizza.name
        recipe = ''.join(pizza.dict()[name])
        click.echo(f"- {name}: {recipe}")


@cli.command()
@click.argument(
    'pizza_type',
    type=click.Choice(list(map(lambda x: str(x)[:-1], MENU)))
    )
@click.option('--delivery', is_flag=True, default=False)
def order(pizza_type: str, delivery: bool):
    """Заказать пиццу"""
    click.echo(f"Заказываем {pizza_type} pizza...")

    bake_fn(pizza_type)

    if delivery:
        click.echo(delivery_fn(pizza_type))
    else:
        click.echo(pickup_fn(pizza_type))


if __name__ == '__main__':
    cli()
