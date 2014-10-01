# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    while True:
        (n, l) = map(int, sys.stdin.readline().split())
        if n == 0 and l == 0:
            break
        data = []
        farthest_ant = None  # 出口まで一番遠い蟻
        max_time = 0         # 出口までの最長時間
        for i in range(1, n + 1):
            (d, p) = sys.stdin.readline().split()
            p = int(p)
            time = p if d == 'L' else l - p
            ant = dict(id=i, direction=d, position=p, time=time)
            data.append(ant)

            if time >= max_time:
                farthest_ant = ant
                max_time = time

        # 衝突が発生しない蟻を取り除く
        data = [ ant for ant in data if ant['position'] % 2 == farthest_ant['position'] % 2]

        opposites = [ant for ant in data if ant['direction'] != farthest_ant['direction']]
        if opposites:
            if farthest_ant['direction'] == 'L':
                opposite_ant = opposites[0]
                candidates = [ant for ant in data if opposite_ant['position'] <= ant['position'] <=firthest_ant['position']]
            else:
                opposite_ant = opposites[-1]
                candidates = [ant for ant in data if firthest_ant['position'] <= ant['position'] <= opposite_ant['position']]
            # TODO
            candidates = [ant for ant in data if 
            [ant for ant in data if ant['position']
            
        else:
            last_ant = farthest_ant
        # この時点でわかっていること
        # (1) last_ant は右の方向からトンネルを出る
        # (2) last_ant がトンネルから出る秒数は max_time になる
        # (3) last_ant は偶数位置にいる

        print '{seconds} {id}'.format(seconds=max_time, id=last_ant['id'])
