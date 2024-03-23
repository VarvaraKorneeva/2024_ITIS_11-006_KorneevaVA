while True:
    # input expression and pars it
    expr = str(input())
    elements = expr.split(' ')

    # get terms dict
    terms = {}
    with open('inverted_index.txt', 'r') as i:
        lines = i.read().splitlines()
    for line in lines:
        if line != '':
            l = line.strip().split(' ')
            terms[l[0]] = l[1:-1]

    # find by index
    with open('../1/index.txt', 'r') as f:
        count = len(f.read().splitlines())
    elm_ind = []
    for e in elements:
        if e != '&' and e != '|':
            if e[0] != '!':
                elm_ind.append(terms[e])
            else:
                elm_ind.append([i for i in range(1, count) if i not in terms[e[1:]]])
        else:
            elm_ind.append(e)
    result = []
    for i, e in enumerate(elm_ind):
        if e == '&':
            elm_ind[i] = [x for x in elm_ind[i-1] if x in elm_ind[i+1]]
            del elm_ind[i+1]
            del elm_ind[i-1]
    for i, e in enumerate(elm_ind):
        if e == '|':
            result.extend(elm_ind[i-1])
            result.extend(elm_ind[i + 1])
    print(*set(result))
