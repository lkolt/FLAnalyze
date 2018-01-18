from parsers import *
from queue import *
from utils import *


def top_down(grammar, graph):
    print('Reading input: Done')
    queue = Queue()
    was = set()
    size = graph.shape[0]
    for left in range(size):
        for i in grammar.starts:
            for j in grammar.starts[i]:
                cur = (left, (i, left), j)
                queue.put(cur)
                was.add(cur)
                # adding to was while adding to queue gives memory (and speed) optimization, but makes code ugly

    print('Pre-accounting: Done')
    print('Starting dynamic with memorization...')

    used = defaultdict(list)
    gss = defaultdict(lambda: defaultdict(set))
    result = set()
    iteration = 0
    while queue.qsize() > 0:
        if iteration % 1500 == 0:
            print('Current iteration: ' + str(iteration) + ' and in queue ' + str(queue.qsize()) + ' elements more')
        iteration += 1

        cur = queue.get()
        left, node, right = cur

        for finals in grammar.finals.values():
            if right in finals:
                for i in gss[node]:
                    for j in gss[node][i]:
                        nd = (left, i, j)
                        if nd not in was:
                            queue.put(nd)
                            was.add(nd)

                result.add((node, left))
                used[node].append(left)

        for i in range(len(grammar.matrix[right])):
            for j in range(len(graph[left])):
                for term in grammar.matrix[right][i]:
                    if not check_term(term):
                        new_node = (term, left)
                        gss[new_node][node].add(i)
                        for nterm in grammar.starts[term]:
                            nd = (left, new_node, nterm)
                            if nd not in was:
                                queue.put(nd)
                                was.add(nd)
                        if new_node in used:
                            for v in used[new_node]:
                                nd = (v, node, i)
                                if nd not in was:
                                    queue.put(nd)
                                    was.add(nd)
                    else:
                        for label_graph in graph[left][j]:
                            if term == label_graph:
                                nd = (j, node, i)
                                if nd not in was:
                                    queue.put(nd)
                                    was.add(nd)

    return [(right, S, r) for ((S, right), r) in result]


def run(grammar_filename, graph_filename):
    print('Starting top_down algorithm on grammar ' + grammar_filename + ' and graph ' + graph_filename + '...')
    return top_down(read_grammar_automaton(grammar_filename), read_graph(graph_filename))
