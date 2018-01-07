import numpy
import parsers
from queue import *
from utils import *


def bottom_up(grammar, graph):
    print('Reading input: Done')
    print('Pre-accounting...')

    graph_size = graph.shape[0]
    grammar_size = grammar.matrix.shape[0]

    check = numpy.empty((grammar_size, graph_size, grammar_size, graph_size), dtype=list)
    for i in range(grammar_size):
        for j in range(graph_size):
            for k in range(grammar_size):
                for l in range(graph_size):
                    check[i][j][k][l] = []

    edges = defaultdict(list)
    for i in range(grammar_size):
        for j in range(grammar_size):
            for label in grammar.matrix[i][j]:
                edges[label].append((i, j))

    for graph_from in range(graph_size):
        for graph_to in range(graph_size):
            for label in graph[graph_from][graph_to]:
                for grammar_from, grammar_to in edges[label]:
                    if label not in check[grammar_from][graph_from][grammar_to][graph_to]:
                        check[grammar_from][graph_from][grammar_to][graph_to].append(label)

    print('Pre-accounting: Done')

    iteration = 0
    while True:
        print('Current iteration = ' + str(iteration))
        iteration += 1

        queue_iter = 0
        new_edges = []
        for nterm in grammar.starts:
            for grammar_from in grammar.starts[nterm]:
                for graph_from in range(graph_size):
                    used = numpy.zeros((grammar_size, graph_size), dtype=bool)

                    queue = Queue()
                    queue.put((grammar_from, graph_from))
                    used[grammar_from][graph_from] = True
                    while queue.qsize() > 0:
                        grammar_to, graph_to = queue.get()

                        if nterm not in graph[graph_from][graph_to] and grammar_to in grammar.finals[nterm]:
                            graph[graph_from][graph_to].append(nterm)
                            new_edges.append((graph_from, graph_to, nterm))

                        for i in range(grammar_size):
                            for j in range(graph_size):
                                if not used[i][j] and check[grammar_to][graph_to][i][j]:
                                    queue.put((i, j))
                                    used[i][j] = True

                        queue_iter += 1
                        if queue_iter % 1500 == 0:
                            print('Current queue iteration: ' + str(queue_iter) + ' and in queue ' + str(queue.qsize())
                                  + ' elements more')

        if len(new_edges) == 0:
            break

        for graph_from, graph_to, label in new_edges:
            for grammar_from, grammar_to in edges[label]:
                if label not in check[grammar_from][graph_from][grammar_to][graph_to]:
                    check[grammar_from][graph_from][grammar_to][graph_to].append(label)

    print('Collecting results...')
    ans = []
    for i in range(graph_size):
        for j in range(graph_size):
            for label in graph[i][j]:
                if not check_term(label):
                    ans.append((i, label, j))
    return ans


def run(grammar_filename, graph_filename):
    print('Starting bottom_up algorithm on grammar ' + grammar_filename + ' and graph ' + graph_filename + '...')
    return bottom_up(parsers.read_grammar_automaton(grammar_filename), parsers.read_graph(graph_filename))
