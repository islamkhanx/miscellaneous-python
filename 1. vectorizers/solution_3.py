import math


def idf_transform(count_matrix: [list[list[float]]]) -> list[float]:
    """Из матриц количеств слов в документах возвращает idf каждого слова"""
    doc_count = []
    for ind in range(len(count_matrix[0])):
        doc_count.append(sum([1 for word in count_matrix if word[ind] > 0]))

    all_doc = len(count_matrix)
    doc_count = [1 + math.log((1 + all_doc) / (1 + count))
                 for count in doc_count]
    return doc_count


if __name__ == '__main__':
    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    ]

    idf_matrix = idf_transform(count_matrix)

    print(idf_matrix)
