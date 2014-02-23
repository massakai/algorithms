# -*- coding: utf-8 -*-

import argparse
import sys

class Solver(object):
    u''''''

    def __init__(self):
        self.clear_cache()

    def clear_cache(self):
        u'''キャッシュを消す。'''
        self.__cache = {}

    def solve(self, n, elements):
        u'''正整数nを表現するために必要な要素数を出力する。'''
        if n in self.__cache:
            return self.__cache[n]

        if n in elements:
            answer = 1
        else:
            answer = min([ self.solve(n - number, elements) for number in sorted(elements, reverse=True) if n > number ]) + 1

        self.__cache[n] = answer
        return answer

def generate_tetrahedral_number_list(n):
    u'''n以下の正四面体数リストを生成する。'''
    result_list = []

    for i in range(1, n + 1):
        value = tetrahedral_number(i)
        if value > n:
            break
        result_list.append(value)

    return result_list

def tetrahedral_number(n):
    u'''n番目の四面体数を出力する。'''
    return n * (n + 1) * (n + 2) / 6

def execute(path):
    u'''ファイルから入力を読み込んで解を求める。'''
    solver  = Solver()
    solver2 = Solver() # 奇数用
    with open(path) as f:
        for line in f:
            n = int(line)
            if n == 0:
                break
            elements = generate_tetrahedral_number_list(n)
            odd_elements = [ element for element in elements if element % 2 != 0 ]
            print '%d %d' % (solver.solve(n, elements), solver2.solve(n, odd_elements))

def read_args(argv):
    u'''実行引数を読み込む。'''
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', nargs=1, help='Input file')

    args = parser.parse_args(argv)
    ret = {'input': args.input[0]}

    return ret

if __name__ == '__main__':
    args = read_args(sys.argv[1:])
    execute(args['input'])
