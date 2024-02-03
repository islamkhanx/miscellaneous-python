## Запуск
<code>python -m doctest -v issue_1/issue_1.py</code>

## Результат
```bash
Trying:
    encode('ISLAMKHAN')
Expecting:
    '.. ... .-.. .- -- -.- .... .- -.'
ok
Trying:
    encode('AVITO ACADEMY')
Expecting:
    '.- ...- .. - --- ....... .- -.-. .- -.. . -- -.--'
**********************************************************************
File "/Users/islamkhanserikbayev/Documents/HW_test/issue_1/issue_1.py", line 34, in issue_1.encode
Failed example:
    encode('AVITO ACADEMY')
Expected:
    '.- ...- .. - --- ....... .- -.-. .- -.. . -- -.--'
Got:
    '.- ...- .. - ---   .- -.-. .- -.. . -- -.--'
Trying:
    encode('SOS')
Expecting:
    '... --- ...'
ok
Trying:
    encode('Error')
Expecting:
    Traceback (most recent call last):
    ...
    KeyError: 'r'
ok
Trying:
    encode('Fail')
Expecting:
    'some random stuf'
**********************************************************************
File "/Users/islamkhanserikbayev/Documents/HW_test/issue_1/issue_1.py", line 42, in issue_1.encode
Failed example:
    encode('Fail')
Exception raised:
    Traceback (most recent call last):
      File "/Users/islamkhanserikbayev/anaconda3/lib/python3.10/doctest.py", line 1350, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest issue_1.encode[4]>", line 1, in <module>
        encode('Fail')
      File "/Users/islamkhanserikbayev/Documents/HW_test/issue_1/issue_1.py", line 45, in encode
        encoded_signs = [
      File "/Users/islamkhanserikbayev/Documents/HW_test/issue_1/issue_1.py", line 46, in <listcomp>
        LETTER_TO_MORSE[letter] for letter in message
    KeyError: 'a'
1 items had no tests:
    issue_1
**********************************************************************
1 items had failures:
   2 of   5 in issue_1.encode
5 tests in 2 items.
3 passed and 2 failed.
***Test Failed*** 2 failures.
```