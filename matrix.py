import parsers
import numpy
from utils import *


def grammar_closure(grammar, matrix):
    print('Reading input: Done')

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

    size = matrix.shape[0]
    mtx = numpy.empty((size, size), dtype=list)
    for i in range(size):
        for j in range(size):
            mtx[i, j] = term_grammar[matrix[i, j]].copy() if matrix[i, j] in term_grammar.keys() else []

    print('Pre-accounting: Done')

    iteration = 0
    work = True
    while work:

        iteration += 1
        print('Starting Floyd...')

        work = False
        for i in range(size):
            for j in range(size):
                for k in range(size):
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

            # printing
            if i % 50 == 0:
                print('>Done: ' + str(100 * i / size) + '%')

    print('Collecting results...')
    ans = []
    for i in range(size):
        for j in range(size):
            for nonterm in mtx[i, j]:
                ans.append((i, nonterm, j))
    return ans


def run(grammar_filename, graph_filename):
    print('Starting matrix algorithm on grammar ' + grammar_filename + ' and graph ' + graph_filename + '...')
    return grammar_closure(parsers.read_grammar(grammar_filename), parsers.read_graph(graph_filename))
