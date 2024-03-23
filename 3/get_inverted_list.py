def find_inverted_index():
    all_words = []
    with open('../1/index.txt', 'r') as f:
        lines = f.read().splitlines()

    # read all files and get all words
    for i in range(1, len(lines) + 1):
        with open(f'../2/pages_lem/{i}.txt', 'r') as c:
            words = c.read().strip().split(' ')
            for word in words:
                if word not in all_words:
                    all_words.append(word)

    unique_term = set(all_words)
    term_with_inv_index = {k: [] for k in unique_term}
    # get inverted index for each words
    for i in range(1, len(lines) + 1):
        with open(f'../2/pages_lem/{i}.txt', 'r') as c:
            words = c.read().strip().split(' ')
            # for each term check to have in file
            for term in unique_term:
                if term in words:
                    term_with_inv_index[term].append(i)

    # sorted and save it to file
    sorted_term = dict(sorted(term_with_inv_index.items()))
    with open('inverted_index.txt', 'w') as i:
        for k, values in sorted_term.items():
            i.write(f'{k} ')
            for v in values:
                i.write(f'{v} ')
            i.write('\n')


find_inverted_index()
