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
    mtx = numpy.empty((size, size), dtype=set)
    for i in range(size):
        for j in range(size):
            mtx[i, j] = set()
            for label in matrix[i, j]:
                if label in term_grammar.keys():
                    for lbl in term_grammar[label]:
                        mtx[i, j].add(lbl)

    print('Pre-accounting: Done')

    iteration = 0
    work = True
    while work:
        print('Current iteration = ' + str(iteration))
        iteration += 1
        print('Starting Floyd...')

        work = False
        for k in range(size):
            for i in range(size):
                for j in range(size):

                    fst = mtx[i, k]
                    snd = mtx[k, j]

                    pr = set()
                    for q in fst:
                        for w in snd:
                            pr.add(q + w)

                    for nterm_pair in pr:
                        if nterm_pair in nterm_grammar:
                            res = nterm_grammar[nterm_pair]
                            for lbl in res:
                                if lbl not in mtx[i, j]:
                                    mtx[i, j].add(lbl)
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
