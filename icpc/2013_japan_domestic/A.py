#!/usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Problem A Integral Rectangles
http://sparth.u-aizu.ac.jp/icpc2013/d_problems.php#section_A

Judgement data
http://sparth.u-aizu.ac.jp/icpc2013/contest/domjdata2013.zip
"""
import sys
import operator

def generate_table():
    table = []
    for h in range(1, 150):
        for w in range(h + 1, 151):
            table.append((h, w, h * h + w * w))
    return [(h, w) for (h, w, d) in sorted(table, key=operator.itemgetter(2))]

if __name__ == "__main__":
    table = generate_table()
    for line in sys.stdin:
        (h, w) = [int(i) for i in line.split()]
        if h == w == 0:
            break
        bigger = table[table.index((h, w)) + 1]
        print "%d %d" % bigger
