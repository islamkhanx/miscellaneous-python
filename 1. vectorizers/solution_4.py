import math


class TfidfTransformer():
    """Класс с методами для tdfidf трансформации
    из матрицы количеств слов в документах """

    def fit_transform(self, count_matrix: list[list[int]]) -> list[list[int]]:
        """из матрицы количеств слов в документах возвращает tdidf
        каждого слова в каждом документе"""

        tf_matrix = self.tf_transform(count_matrix)
        idf_matrix = self.idf_transform(count_matrix)
        tfidf_matrix = []

        for sentence in tf_matrix:
            tfidf = []
            for word_ind in range(len(sentence)):
                tfidf.append(round(sentence[word_ind]
                                   * idf_matrix[word_ind], 3))
            tfidf_matrix.append(tfidf)

        return tfidf_matrix

    def tf_transform(count_matrix: list[list[int]]) -> list[list[float]]:
        """Из матриц количеств слов
        возвращает частоту каждого слова в документах"""
        for sentence in count_matrix:
            all_count = sum(sentence)
            for ind in range(len(sentence)):
                sentence[ind] /= all_count
        return count_matrix

    def idf_transform(count_matrix: [list[list[float]]]) -> list[float]:
        """Из матриц количеств слов в документах
        возвращает idf каждого слова"""
        doc_count = []
        for ind in range(len(count_matrix[0])):
            doc_count.append(sum([1 for word in count_matrix
                                  if word[ind] > 0]))

        all_doc = len(count_matrix)
        doc_count = [1 + math.log((1 + all_doc) / (1 + count))
                     for count in doc_count]
        return doc_count


if __name__ == '__main__':
    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    ]
    vector = TfidfTransformer()
    idf_matrix = vector.fit_transform(count_matrix)

    print(idf_matrix)
