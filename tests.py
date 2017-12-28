import unittest
import bottom_up
import matrix
import top_down
from utils import *

data_graphs = 'data/graphs/'
graphs_names = ['skos', 'generations', 'travel', 'univ-bench', 'atom-primitive', 'biomedical-mesure-primitive',
                'foaf', 'people_pets', 'funding']
extension_graphs = '.dot'

data_grammars = 'data/grammars/'
grammars_names = ['Q1', 'Q2']
extension_matrix_grammars = '_H.dot'
extension_bottom_up_grammars = '_N.dot'
extension_top_down_grammars = '_A.dot'

answers = [[810, 2164, 2499, 2540, 15454, 15156, 4118, 9472, 17634],
           [1, 0, 63, 81, 122, 2871, 10, 37, 1158]]


class UnitTesting(unittest.TestCase):
    def test_matrix(self):
        for i, grammar in enumerate(grammars_names):
            for j, graph in enumerate(graphs_names):
                grammar_name = data_grammars + grammar + extension_matrix_grammars
                graph_name = data_graphs + graph + extension_graphs
                res = matrix.run(grammar_name, graph_name)
                self.assertEqual(count_control_number(res), answers[i][j],
                                 'Error in ' + grammar_name + ' and ' + graph_name)
                print(grammar_name + ' and ' + graph_name + ' OK')

    def test_bottom_up(self):
        for i, grammar in enumerate(grammars_names):
            for j, graph in enumerate(graphs_names):
                grammar_name = data_grammars + grammar + extension_bottom_up_grammars
                graph_name = data_graphs + graph + extension_graphs
                res = bottom_up.run(grammar_name, graph_name)
                self.assertEqual(count_control_number(res), answers[i][j],
                                 'Error in ' + grammar_name + ' and ' + graph_name)
                print(grammar_name + ' and ' + graph_name + ' OK')

    def test_top_down(self):
        for i, grammar in enumerate(grammars_names):
            for j, graph in enumerate(graphs_names):
                grammar_name = data_grammars + grammar + extension_top_down_grammars
                graph_name = data_graphs + graph + extension_graphs
                res = top_down.run(grammar_name, graph_name)
                self.assertEqual(count_control_number(res), answers[i][j],
                                 'Error in ' + grammar_name + ' and ' + graph_name)
                print(grammar_name + ' and ' + graph_name + ' OK')
