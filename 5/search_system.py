import numpy as np

from collections import Counter
import math
import csv


with open('../1/index.txt', 'r') as f:
    D = len(f.read().splitlines())
with open('../3/inverted_index.txt', 'r') as i:
    indexes = i.read().splitlines()
inv_ind = {}
for ind in indexes:
    line = ind.strip().split(' ')
    inv_ind[line[0]] = line[1:]

with open('../4/tf-idf.csv', newline='') as tf_idf_file:
    files_vector = {key: [] for key in range(1, D + 1)}
    reader = csv.DictReader(tf_idf_file, delimiter=' ')
    for row in reader:
        for i in range(1, D + 1):
            files_vector[i].append(float(row[str(i)]))


while True:
    q = str(input()).split(' ')
    q_vector = []
    counts = Counter(q)
    for i in range(len(inv_ind)):
        if list(inv_ind.keys())[i] in q:
            tf = counts[list(inv_ind.keys())[i]] / len(q)
            idf = math.log(D / len(inv_ind[list(inv_ind.keys())[i]]), 2)
            tf_idf = '{:.6f}'.format(tf * idf)
            q_vector.append(tf_idf)
        else:
            q_vector.append(0)

    similarity = {}
    a = np.asarray(q_vector, dtype='float64')
    for i in range(1, D + 1):
        b = np.asarray(files_vector[i], dtype='float64')
        cos_sim = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
        similarity[i] = cos_sim

    # write result to file
    similarity_sort = dict(sorted(similarity.items(), key=lambda x: x[1], reverse=True))
    with open('search_sistem_result.txt', 'a') as f:
        for word in q:
            f.write(f'{word} ')
        f.write('\n')
        for k, v in similarity_sort.items():
            f.write(f'{k} {v}\n')
            print(k, v)
        f.write('\n')
