from string import *


def check_term(s):
    for c in s:
        if c not in ascii_lowercase + digits:
            return False
    return True


def res_to_str(res):
    res_str = ''
    for i, nterm, j in res:
        res_str += str(i) + ',' + nterm + ',' + str(j) + '\n'
    return res_str


def count_control_number(res):
    return len([nterm for _, nterm, _ in res if 'S' == nterm])
