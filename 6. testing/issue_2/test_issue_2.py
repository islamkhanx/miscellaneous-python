import pytest
from issue_2 import decode


@pytest.mark.parametrize(
    'source_string, result',
    [
        (' -.-. .... . . ... .', 'CHEESE'),
        ('-.-. .- - / .. ...', 'cat is'),
        ('.-. .- .. -.', 'RAIN'),
    ],
)
def test_morse_decode(source_string, result):
    """Функция тестирует функцию decode"""
    assert decode(source_string) == result


if __name__ == '__main__':
    pass
