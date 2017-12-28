# FLAnalyze

## Requirements 
**python 3.6**

## Input
All graphs in input must be in Graphviz/DOT format
* Matrix algorithm need grammar in Chomsky normal form (**for example:** data/grammars/Q1_H.dot)
* Bottom_up algorithm need normal grammar (**for example:** data/grammars/Q1_N.dot)
* Top_down algorithm need grammar in Graphviz/DOT format (**for example:** data/grammars/Q1_A.dot)

## Run

`python analyze.py -t <grammar_filename> <graph_filename> <result_filename>(optional)`

Where -t is a type of algorithm what you want to use: 
    <li> `-m` for matrix algorithm </li>
    <li> `-u` for bottom_up algorithm </li>
    <li> `-d` for top_down algorithm </li>

For example: <br> 
`python analyze.py -d data/grammars/Q1_A.dot data/graphs/skos.dot result.txt`

## Unit tests
Using standard library unittest:
<br>
`python -m unittest -v tests`

All tests are passed for ~2.5 hours (bottom_up is very slow)

For run tests for only one algorithm:
<br>
`python -m unittest -v tests.UnitTesting.test_matrix`<br>
`python -m unittest -v tests.UnitTesting.test_bottom_up`<br>
`python -m unittest -v tests.UnitTesting.test_top_down`
