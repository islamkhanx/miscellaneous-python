from solution_1 import CountVectorizer
from solution_4 import TfidfTransformer


class TfidfVectorizer(CountVectorizer):
    """Класс с методами для tdfidf трансформации
    из листа документов"""

    def fit_transform(self, sentences: list[str]) -> list[list[int]]:
        """из листа документов создает список слов который сохраняает
        а частоты в списке слов превращает в tfidf матрицу"""
        count_matrix = super().fit_transform(sentences)
        tfidf_matrix = TfidfTransformer().fit_transform(count_matrix)
        return tfidf_matrix


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = TfidfVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names())
    print(count_matrix)
