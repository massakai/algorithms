#!/usr/bin/env python
# -*- coding: utf-8 -*-
u"""
Problem A Hanafuda Shuffle
http://www.ehime-u.ac.jp/ICPC/problems/domestic/d2004/A.jp/A.html

Judgement data
http://www.ehime-u.ac.jp/ICPC/problems/domestic/d2004/
"""
import sys

def trace(p, c, x):
    u"""カットされる前の位置を調べる"""
    if 0 <= x < c:
        x += p - 1
    elif c <= x < c + p - 1:
        x -= c
    return x    

if __name__ == '__main__':
    while True:
        (n, r) = [int(i) for i in sys.stdin.readline().split()]
        if n == r == 0:
            break
        shuffle = []
        for i in range(r):
            cut = [int(x) for x in sys.stdin.readline().split()]
            shuffle.append(cut)
        index = 0
        for p, c in reversed(shuffle):
            index = trace(p, c, index)
        hanahuda = range(n, 0, -1)  # 花札(上から格納)
        print hanahuda[index]
