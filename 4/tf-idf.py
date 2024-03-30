import math
from collections import Counter
import csv


def calculate_tf_idf():
    with open('../1/index.txt', 'r') as f:
        D = len(f.read().splitlines())
    terms = {}
    with open('../3/inverted_index.txt', 'r') as i:
        lines = i.read().splitlines()
    for line in lines:
        l = line.split(' ')
        terms[l[0]] = l[1:]

    with open('tf.csv', 'w', newline='') as tf_file, open('idf.csv', 'w', newline='') as idf_file, \
            open('tf-idf.csv', 'w', newline='') as tf_idf_file:
        tf_fieldnames = ['term'] + list(range(1, D + 1))
        tf_writer = csv.writer(tf_file, delimiter=' ')
        tf_writer.writerow(tf_fieldnames)
        idf_fieldnames = ['term', 'idf']
        idf_writer = csv.writer(idf_file, delimiter=' ')
        idf_writer.writerow(idf_fieldnames)
        tf_idf_writer = csv.writer(tf_idf_file, delimiter=' ')
        tf_idf_writer.writerow(tf_fieldnames)

        for term in terms:
            # calculate idf
            idf = round(math.log(D / len(terms[term]), 2), 6)
            idf_writer.writerow([term, idf])

            # calculate tf and tf-idf
            terms_tf = [term]
            terms_tf_idf = [term]
            for i in range(1, D + 1):
                if str(i) in terms[term]:
                    with open(f'../2/pages_lem/{i}.txt', 'r') as c:
                        words = c.read().strip().split(' ')
                        counts = Counter(words)
                        tf = round(counts[term] / len(words), 6)
                        terms_tf.append(tf)
                        tf_idf = '{:.6f}'.format(tf * idf)
                        terms_tf_idf.append(tf_idf)
                else:
                    terms_tf.append(0)
                    terms_tf_idf.append(0)
            tf_writer.writerow(terms_tf)
            tf_idf_writer.writerow(terms_tf_idf)


calculate_tf_idf()
