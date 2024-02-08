# TfIdf (Классы)
Задачи для базового ООП. Можно потренировать базовую релизацию классов, наследование и композицию. Так же рекоммендуется _не использовать сторонние библиотеки_


## Задание #1: count vectorizer
Напишите класс `CountVectorizer`, реализующий базовую функциональность векторизации текстовых данных.  
Класс должен быть способен преобразовывать набор текстовых документов в матрицу терминов-документов (Term-Document Matrix, TDM)
с использованием подхода "мешка слов" (bag-of-words).
```python
corpus = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]
vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names())
Out: ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro', 
        'fresh', 'ingredients', 'parmesan', 'to', 'taste']

print(count_matrix)
Out:[[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
```

## Задание #2:term frequency
Напишите функцию `tf_transform`, которая принимает на вход матрицу количеств слов в документах (`Count Matrix`) в виде списка списков целых чисел, и возвращает матрицу их частот в виде списка списков чисел с плавающей точкой

```python
count_matrix = [
    [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
]

tf_matrix = tf_transform(count_matrix)

print(tf_matrix)
Out: [[0.14285714285714285, 0.14285714285714285, 0.2857142857142857, 0.14285714285714285, 0.14285714285714285, 0.14285714285714285, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
      [0.0, 0.0, 0.14285714285714285, 0.0, 0.0, 0.0,0.14285714285714285, 0.14285714285714285, 0.14285714285714285, 0.14285714285714285, 0.14285714285714285, 0.14285714285714285]]
```

## Задание #3: inverse document-frequency
Реализуйте функцию `idf_transform`, которая принимает на вход матрицу количеств слов в документах (`Count Matrix`) в виде списка списков целых чисел, и возвращает матрицу их обратных частот (Inverse Document Frequency, IDF) в виде списка списков чисел с плавающей точкой.

```python
count_matrix = [
   [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
   [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
]
idf_matrix = idf_transform(count_matrix)
print(idf_matrix)
Out: [1.4, 1.4, 1.0, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4]
```

## Задание #4: tf-idf transformer
Реализуйте класс `TfidfTransformer`, предоставляющий функциональность по преобразованию матрицы количеств слов в документах в матрицу TF-IDF (Term Frequency-Inverse Document Frequency). Реализуйте метод `fit_transform`, который принимает на вход матрицу количеств слов в документах и возвращает соответствующую матрицу TF-IDF.

```python
count_matrix = [
    [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
]
vector = TfidfTransformer()
idf_matrix = vector.fit_transform(count_matrix)

print(idf_matrix)
Out: [[0.2, 0.2, 0.286, 0.2, 0.2, 0.2, 0, 0, 0, 0, 0, 0]
      [0, 0, 0.143, 0, 0, 0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.21]]
```

## Задание #5: tf-idf vectorizer
Реализуйте класс `TfidfVectorizer`, предоставляющий удобный интерфейс для векторизации текстовых данных с использованием TF-IDF преобразования. Ваш класс должен содержать метод `fit_transform`, который принимает на вход список текстовых документов и возвращает матрицу TF-IDF.

```python
corpus = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names())
Out: ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
    'fresh', 'ingredients', 'parmesan', 'to', 'taste']

print(tfidf_matrix)
Out: [[0.2, 0.2, 0.286, 0.2, 0.2, 0.2, 0, 0, 0, 0, 0, 0],
      [0, 0, 0.143, 0, 0, 0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.21]]
```