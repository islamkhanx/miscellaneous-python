## Запуск

<code> python -m pytest -v issue_4/test_issue_4.py</code>

## Результат
```python
  ==================================================================================== test session starts =====================================================================================
  platform darwin -- Python 3.10.9, pytest-7.1.2, pluggy-1.0.0 -- /Users/islamkhanserikbayev/anaconda3/bin/python
  cachedir: .pytest_cache
  rootdir: /Users/islamkhanserikbayev/Documents/HW_test
  plugins: anyio-3.5.0
  collected 4 items                                                                                                                                                                            

  issue_4/test_issue_4.py::test_cities PASSED                                                                                                                                            [ 25%]
  issue_4/test_issue_4.py::test_error PASSED                                                                                                                                             [ 50%]
  issue_4/test_issue_4.py::test_false FAILED                                                                                                                                             [ 75%]
  issue_4/test_issue_4.py::test_name_true PASSED                                                                                                                                         [100%]

  ========================================================================================== FAILURES ==========================================================================================
  _________________________________________________________________________________________ test_false _________________________________________________________________________________________

      def test_false():
          items = ['Isa', 'Aiko', 'Kala', 'IsaEra']
          actual = fit_transform(items)
          expected = [
              ('Isa', [0, 0, 0, 0, 1]),
              ('Aiko', [0, 0, 0, 1, 0]),
              ('Kala', [0, 0, 1, 0, 0]),
              ('IsaEra', [1, 1, 0, 0, 0]),
              ]
          # fake expected
  >       assert actual == expected, 'They are not equal'
  E       AssertionError: They are not equal
  E       assert [('Isa', [0, ...[1, 0, 0, 0])] == [('Isa', [0, ... 1, 0, 0, 0])]
  E         At index 0 diff: ('Isa', [0, 0, 0, 1]) != ('Isa', [0, 0, 0, 0, 1])
  E         Full diff:
  E           [
  E         -  ('Isa', [0, 0, 0, 0, 1]),
  E         ?                   ---
  E         +  ('Isa', [0, 0, 0, 1]),
  E         -  ('Aiko', [0, 0, 0, 1, 0]),...
  E         
  E         ...Full output truncated (11 lines hidden), use '-vv' to show

  issue_4/test_issue_4.py:32: AssertionError
  ================================================================================== short test summary info ===================================================================================
  FAILED issue_4/test_issue_4.py::test_false - AssertionError: They are not equal
  ================================================================================ 1 failed, 3 passed in 0.05s =================================================================================
```