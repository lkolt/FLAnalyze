from parsers import *
from utils import *


def top_down(grammar, graph):
    queue = set()
    size = graph.shape[0]
    for left in range(size):
        for i in grammar.starts:
            for j in grammar.starts[i]:
                queue.add((left, (i, left), j))

    was = set()
    used = defaultdict(list)
    gss = defaultdict(lambda: defaultdict(set))
    result = set()
    while len(queue) > 0:
        cur = queue.pop()
        if cur not in was:
            was.add(cur)
            left, node, right = cur
            if [right] in grammar.finals.values():
                for i in gss[node]:
                    for j in gss[node][i]:
                        queue.add((left, i, j))

                result.add((node, left))
                used[node].append(left)

            for i in range(len(grammar.matrix[right])):
                for j in range(len(graph[left])):
                    for term in grammar.matrix[right][i]:
                        if term not in grammar.terminals:
                            new_node = (term, left)
                            gss[new_node][node].add(i)
                            for nterm in grammar.starts[term]:
                                queue.add((left, new_node, nterm))
                            if new_node in used:
                                for v in used[new_node]:
                                    queue.add((v, node, i))
                        else:
                            for label_graph in graph[left][j]:
                                if term == label_graph:
                                    queue.add((j, node, i))

    return [(right, S, r) for ((S, right), r) in result]


def run(grammar_filename, graph_filename):
    result = top_down(read_grammar_automaton(grammar_filename), read_graph(graph_filename))
    res_str = res_to_str(result)

    print(count_control_number(result))

    return res_str


grammar_in = 'data/grammars/Q1_A.gr'
graph_in = 'data/graphs/skos.dot'

res = run(grammar_in, graph_in)
