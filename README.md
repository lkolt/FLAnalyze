# FLAnalyze

## Requirements 
**python 3.6**

## Input
All graphs in input must be in Graphviz/DOT format
* Matrix algorithm need grammar in Chomsky normal form (**for example:** data/grammars/Q1_H.dot)
* Bottom_up algorithm need grammar in Graphviz/DOT format (**for example:** data/grammars/Q1_A.dot)
* Top_down algorithm need grammar in Graphviz/DOT format (**for example:** data/grammars/Q1_A.dot)

## Run

`python analyze.py -t <grammar_filename> <graph_filename> <result_filename>(optional)`

Where -t is a type of algorithm what you want to use: 
* `-m` for matrix algorithm 
* `-u` for bottom_up algorithm 
* `-d` for top_down algorithm 

For example: <br> 
`python analyze.py -d data/grammars/Q1_A.dot data/graphs/skos.dot result.txt`

## Unit tests
For run all tests:
<br>
`python -m unittest -v tests`
<br>
All tests are passed for ~3.8 hours (bottom_up is very slow)

For run only quick tests with small data:
<br>
`python -m unittest -v tests.Quick`

For run tests for every algorithm separately:
<br>
`python -m unittest -v tests.Hard.test_matrix`<br>
`python -m unittest -v tests.Hard.test_bottom_up`<br>
`python -m unittest -v tests.Hard.test_top_down`
