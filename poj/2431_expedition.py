# -*- coding: utf-8 -*-
u"""POJ#2431 Expedition http://poj.org/problem?id=2431"""
import heapq
import sys


def solve():
    u"""solve a problem"""
    n = int(sys.stdin.readline())
    gas_stations = []
    for _ in range(n):
        (a, b) = [int(j) for j in sys.stdin.readline().split()]
        gas_stations.append((a, b))
    gas_stations.sort(key=lambda gas_station: gas_station[0])
    (l, p) = [int(j) for j in sys.stdin.readline().split()]

    count = 0
    queue = []
    while p < l:
        while gas_stations and gas_stations[-1][0] >= p:
            _, b = gas_stations.pop()
            # max-heap にするため -b をキーにする
            heapq.heappush(queue, (-b, b))
        try:
            _, b = heapq.heappop(queue)
        except IndexError:
            return -1
        p += b
        count += 1
    return count


if __name__ == "__main__":
    print(solve())
