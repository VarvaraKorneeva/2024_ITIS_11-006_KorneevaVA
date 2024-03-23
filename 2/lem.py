import pymorphy2
from nltk.corpus import stopwords


def lem():
    morph = pymorphy2.MorphAnalyzer()
    stop_words_ru = stopwords.words('russian')
    with open('../1/index.txt', 'r') as f:
        lines = f.read().splitlines()

    for i in range(1, len(lines) + 1):
        with open(f'../1/pages/{i}.txt', 'r') as c:
            str_words = c.read()
            words = str_words.strip().split(' ')
            for word in words:
                p = morph.parse(word.lower())[0]
                lemma = p.normal_form
                if lemma not in stop_words_ru:
                    with open(f'pages_lem/{i}.txt', 'a') as l:
                        l.write(f'{lemma} ')


lem()
