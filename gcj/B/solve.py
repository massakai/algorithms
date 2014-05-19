#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def calc_best_seconds(C, F, X):
    cookies_per_seconds = 2.0 
    seconds = 0.0 # 工場を買う時間
    while X / (cookies_per_seconds + F) < (X - C) / cookies_per_seconds:
        seconds += C / cookies_per_seconds
        cookies_per_seconds += F
    return seconds + X / cookies_per_seconds

if __name__ == '__main__':
    case = int(sys.stdin.readline().strip())
    for i in range(1, case+1):
        (C, F, X) = [ float(item) for item in sys.stdin.readline().split() ]
        print("Case #%d: %.7f" % (i, calc_best_seconds(C, F, X)))
