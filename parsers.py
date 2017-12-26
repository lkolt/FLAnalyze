import numpy
from collections import *


def read_graph(filename):
    with open(filename) as f:
        lines = f.readlines()
        size = lines[2].count(';')

        matrix = numpy.zeros((size, size), dtype=numpy.str)

        for line in lines[3:-1]:
            if len(line) > 1:
                split_seq = line.replace('eps', '@').split(' -> ')
                split_br = split_seq[1].split('[')
                split_quot = split_br[1].split('"')

                i = int(split_seq[0])
                j = int(split_br[0])
                label = split_quot[1]

                matrix[i, j] = label

        return matrix


def read_grammar(filename):
    with open(filename) as f:
        lines = f.readlines()
        res = defaultdict(list)

        for line in lines:
            if len(line) > 1:
                split_seq = line.replace(' ', '').replace('\n', '').replace('eps', '@').split('->')
                left = split_seq[0]
                right = split_seq[1].split('|')
                res[left].extend(right)

        return {k: v for k, v in res.items()}
