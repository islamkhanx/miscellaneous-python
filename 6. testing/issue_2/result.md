## Запуск
<code>python -m pytest -v issue_2/test_issue_2.py</code>

## Результат
```bash
======================================================================================================= test session starts =======================================================================================================
platform darwin -- Python 3.10.9, pytest-7.1.2, pluggy-1.0.0 -- /Users/islamkhanserikbayev/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/islamkhanserikbayev/Documents/HW_test
plugins: anyio-3.5.0
collected 3 items                                                                                                                                                                                                                 

issue_2/test_issue_2.py::test_morse_decode[ -.-. .... . . ... .-CHEESE] PASSED                                                                                                                                              [ 33%]
issue_2/test_issue_2.py::test_morse_decode[-.-. .- - / .. ...-cat is] FAILED                                                                                                                                                [ 66%]
issue_2/test_issue_2.py::test_morse_decode[.-. .- .. -.-RAIN] PASSED                                                                                                                                                        [100%]

============================================================================================================ FAILURES =============================================================================================================
__________________________________________________________________________________________ test_morse_decode[-.-. .- - / .. ...-cat is] ___________________________________________________________________________________________

source_string = '-.-. .- - / .. ...', result = 'cat is'

    @pytest.mark.parametrize(
        'source_string, result',
        [
            (' -.-. .... . . ... .', 'CHEESE'),
            ('-.-. .- - / .. ...', 'cat is'),
            ('.-. .- .. -.', 'RAIN'),
        ],
    )
    def test_morse_decode(source_string, result):
>       assert decode(source_string) == result

issue_2/test_issue_2.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
issue_2/issue_2.py:31: in decode
    decoded_letters = [
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

.0 = <list_iterator object at 0x1023f7b80>

    decoded_letters = [
>       MORSE_TO_LETTER[letter] for letter in morse_message.split()
    ]
E   KeyError: '/'

issue_2/issue_2.py:32: KeyError
===================================================================================================== short test summary info =====================================================================================================
FAILED issue_2/test_issue_2.py::test_morse_decode[-.-. .- - / .. ...-cat is] - KeyError: '/'
=================================================================================================== 1 failed, 2 passed in 0.04s ===================================================================================================

```