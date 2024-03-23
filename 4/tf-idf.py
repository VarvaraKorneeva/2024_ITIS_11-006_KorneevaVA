import math
from collections import Counter


def calculate_tf_idf():
    with open('../1/index.txt', 'r') as f:
        D = len(f.read().splitlines())
    terms = {}
    with open('../3/inverted_index.txt', 'r') as i:
        lines = i.read().splitlines()
    for line in lines:
        l = line.split(' ')
        terms[l[0]] = l[1:-1]

    for i in range(1, D + 1):
        with open(f'pages_tf_idf/{i}.txt', 'w') as t:
            t.write(f'термин tf idf tf-idf\n')
        with open(f'../2/pages_lem/{i}.txt', 'r') as c:
            words = c.read().strip().split(' ')
            counts = Counter(words)
            for word in set(words):
                tf = round(counts[word] / len(words), 6)
                idf = round(math.log(D / len(terms[word]), 2), 6)
                tf_idf = '{:.6f}'.format(tf * idf)
                with open(f'pages_tf_idf/{i}.txt', 'a') as t:
                    t.write(f'{word} {tf} {idf} {tf_idf}\n')


calculate_tf_idf()
