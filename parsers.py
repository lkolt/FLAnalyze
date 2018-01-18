import numpy
from utils import *


def check_digraph(line):
    if line.lower().count('digraph'):
        return True
    return False


def read_graph(filename):
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()

        if not check_digraph(lines[0]):
            print('Not digraph in input')

        size = lines[2].count(';')

        matrix = numpy.empty((size, size), dtype=list)
        for i in range(size):
            for j in range(size):
                matrix[i][j] = []

        for line in lines[3:-1]:
            if len(line) > 1:
                split_seq = line.replace('eps', '@').split(' -> ')
                split_br = split_seq[1].split('[')
                split_quot = split_br[1].split('"')

                i = int(split_seq[0])
                j = int(split_br[0])
                label = split_quot[1]

                matrix[i, j].append(label)

        return matrix


def read_grammar(filename):
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        res = defaultdict(list)

        for line in lines:
            if len(line) > 1:
                split_seq = line.replace(' ', '').replace('\n', '').replace('eps', '@').split('->')
                left = split_seq[0]
                right = split_seq[1].split('|')
                res[left].extend(right)

        return {k: v for k, v in res.items()}


def read_grammar_automaton(filename):
    grammar = GrammarAutomaton()
    with open(filename, 'r', encoding="utf-8-sig") as f:
        lines = f.readlines()

        if not check_digraph(lines[0]):
            print('Not digraph in input')

        size = lines[2].count(";")

        grammar.matrix = numpy.empty((size, size), dtype=list)
        for i in range(size):
            for j in range(size):
                grammar.matrix[i][j] = []

        for line in lines[3:]:
            line = line.replace(' ', '')
            if line.count('label='):
                take = False
                split = line.split('[')
                state = split[0]
                label = ''
                for s in split[1].split('"'):
                    if take:
                        label = s
                        break
                    take = 'label=' in s
                if line.count('color="green"'):
                    grammar.starts[label].append(int(state))
                if line.count('shape="doublecircle"'):
                    grammar.finals[label].append(int(state))
                if line.count('->'):
                    split_s = state.split('->')
                    i = split_s[0]
                    j = split_s[1]

                    grammar.matrix[int(i)][int(j)] += [label]
                    if not label.isupper():
                        grammar.terminals.add(label)
    if len(grammar.starts) == 0:
        print("Incorrect type of grammar automaton!")

    return grammar
