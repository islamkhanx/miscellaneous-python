def tf_transform(count_matrix: list[list[int]]) -> list[list[float]]:
    """Из матрицы количеств слов в документах выдает матрицу их частот"""
    for sentence in count_matrix:
        all_count = sum(sentence)
        for ind in range(len(sentence)):
            sentence[ind] /= all_count
    return count_matrix


if __name__ == '__main__':
    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    ]

    tf_matrix = tf_transform(count_matrix)

    print(tf_matrix)
