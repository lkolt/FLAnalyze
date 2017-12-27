import numpy
import parsers
from utils import *


def dfs(size, matrix, start, cur, s, dct, depth):
    for l, r in dct.items():
        if s == l:
            matrix[start, cur].update(r)

    if depth == 0:
        return

    for i in range(size):
        if matrix[cur, i] != set():
            symbols = matrix[cur, i].copy()
            for symbol in symbols:
                dfs(size, matrix, start, i, s + symbol, dct, depth - 1)


def get_res_set(size, res_mat):
    res_set = set()
    for i in range(size):
        for j in range(size):
            for t in res_mat[i, j]:
                res_set.add((i, t, j))
    return res_set


def run_dfs(size, res_mat, dct, length):
    for i in range(size):
        dfs(size, res_mat, i, i, '', dct, length)

        # printing
        if i % 50 == 0:
            print('>Done: ' + str(100 * i / size) + '%')


def bottom_up(grammar, matrix):
    print('Reading input: Done')
    size = matrix.shape[0]

    mtx = numpy.empty((size, size), dtype=set)
    for i in range(size):
        for j in range(size):
            mtx[i][j] = set(matrix[i][j])

    dict_t = {}
    dict_n = {}
    len_t = 0
    len_l = 0
    for nterm, lines in grammar.items():
        for prod in lines:
            if check_term(prod):
                if prod not in dict_t:
                    dict_t[prod] = set()
                dict_t[prod].add(nterm)
                len_t = max(len(prod), len_t)
            else:
                if prod not in dict_n:
                    dict_n[prod] = set()
                dict_n[prod].add(nterm)
                len_l = max(len(prod), len_l)

    print('Pre-accounting: Done')
    print('Starting dfs for terminals...')

    run_dfs(size, mtx, dict_t, len_t)
    result = get_res_set(size, mtx)

    print('Dfs for terminals: Done')

    iteration = 0
    while True:
        print('Current iteration = ' + str(iteration))
        iteration += 1
        print('Starting one more dfs for nonterminals...')

        run_dfs(size, mtx, dict_n, len_l)
        update = get_res_set(size, mtx)
        if result == update:
            break
        result = update.copy()
        print('One more iteration...')

    print('Collecting results...')
    ans = []
    for l, S, r in result:
        if not check_term(S):
            ans.append((l, S, r))
    return ans


def run(grammar_filename, graph_filename):
    print('Starting bottom_up algorithm on grammar ' + grammar_filename + ' and graph ' + graph_filename + '...')
    return bottom_up(parsers.read_grammar(grammar_filename), parsers.read_graph(graph_filename))
