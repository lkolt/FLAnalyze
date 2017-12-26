import parsers
import numpy
from string import *
from collections import *


def check_term(c):
    return c in ascii_lowercase + digits


def grammar_closure(grammar, matrix):
    temp_n = defaultdict(str)
    temp_t = defaultdict(list)
    for key, value in grammar.items():
        for item in value:
            if check_term(item):
                temp_t[item] += [key]
            else:
                temp_n[item] += key

    nterm_grammar = {k: v for k, v in temp_n.items()}
    term_grammar = {k: v for k, v in temp_t.items()}

    n = matrix.shape[0]
    mtx = numpy.empty((n, n), dtype=list)
    for i in range(n):
        for j in range(n):
            mtx[i, j] = term_grammar[matrix[i, j]].copy() if matrix[i, j] in term_grammar.keys() else []

    work = True
    while work:
        work = False
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    fst = mtx[i, k]
                    snd = mtx[k, j]

                    pr = []
                    for q in fst:
                        for w in snd:
                            pr += [q + w]

                    for nterm_pair in pr:
                        if nterm_pair in nterm_grammar:
                            res = nterm_grammar[nterm_pair]
                            if res not in mtx[i, j]:
                                mtx[i, j] += res
                                work = True
    ans = []
    for i in range(n):
        for j in range(n):
            for nonterm in mtx[i, j]:
                ans.append((i, nonterm, j))
    return ans


def run(grammar_filename, graph_filename):
    res = grammar_closure(parsers.read_grammar(grammar_filename), parsers.read_graph(graph_filename))
    res_str = ''
    for i, nterm, j in res:
        res_str += str(i) + ',' + nterm + ',' + str(j) + '\n'

    print(len([nterm for _, nterm, _ in res if 'S' == nterm]))

    return res


grammar_in = 'data/grammars/Q1_H.gr'
graph_in = 'data/graphs/skos.dot'

res = run(grammar_in, graph_in)
