def counted_operation(operate, elem_list):
    operation_counted_list = [elem_list.copy()]
    for j in range(elem_list.count(operate)):
        operation_counted = []
        operation_check = -1
        for i in range(len(operation_counted_list[j]) - 1):
            if operation_counted_list[j][i + 1] == operate and operation_check == -1:
                if operate == '&':
                    operation_counted.append(
                        [x for x in operation_counted_list[j][i] if x in operation_counted_list[j][i + 2]]
                    )
                elif operate == '|':
                    operation_counted.append(operation_counted_list[j][i] + operation_counted_list[j][i + 2])
                operation_check = i + 1
            elif i != operation_check and i != operation_check + 1:
                operation_counted.append(operation_counted_list[j][i])
        if operation_check != len(operation_counted_list[j]) - 2:
            operation_counted.append(operation_counted_list[j][-1])
        operation_counted_list.append(operation_counted)

    return operation_counted_list[-1]


# get terms dict
terms = {}
with open('inverted_index.txt', 'r') as i:
    lines = i.read().splitlines()
for line in lines:
    if line != '':
        l = line.strip().split(' ')
        terms[l[0]] = [int(i) for i in l[1:]]
with open('../1/index.txt', 'r') as f:
    count = len(f.read().splitlines())


while True:
    # input expression and pars it
    expr = str(input())
    elements = expr.split(' ')

    # find by index
    elm_ind = []
    for e in elements:
        if e != '&' and e != '|':
            if e[0] != '!':
                elm_ind.append(terms[e])
            else:
                elm_ind.append([i for i in range(1, count) if i not in terms[e[1:]]])
        else:
            elm_ind.append(e)

    and_result = counted_operation('&', elm_ind)
    or_result = counted_operation('|', and_result)

    # print result and write it to file
    with open('search_result.txt', 'a') as f:
        for e in elements:
            f.write(f'{e} ')
        f.write('\n')
        if or_result[0]:
            print(*sorted(set(or_result[0])))
            for r in set(or_result[0]):
                f.write(f'{r} ')
        else:
            print('-')
            f.write('-')
        f.write('\n\n')
