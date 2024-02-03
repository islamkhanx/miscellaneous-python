class CountVectorizer:
    """Создаем векторы из предложений"""

    def __init__(self):
        """Инициализация списка слов"""

        self.words = {}

    def fit_transform(self, sentences: list[str]) -> list[list[int]]:
        """Из предложений берем слова которых в списке слов нету,
        считаем из этого листа колво слов в каждом предложении"""

        count_matrix = []
        format_sentences = [sentence.lower().split() for sentence in sentences]
        # пополняем список слов
        for sentence in format_sentences:
            [self.words.update({word: 0}) for word in sentence
             if word not in self.words]

        # сверяем предложения со списком слов
        for sentence in format_sentences:
            # в словаре для этого предложения ключ -- количество слов из words
            word_dic = self.words.copy()
            for word in sentence:
                word_dic[word] += 1
            count_matrix.append(list(word_dic.values()))

        return count_matrix

    def get_feature_names(self) -> list[str]:
        """Выводим список слов"""
        return list(self.words.keys())


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names())
    print(count_matrix)
