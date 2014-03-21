# -*- coding: utf-8 -*-

from copy import deepcopy

def solve(graph, start, goal):
    n = len(graph)
    nodes = {}
    for i in range(n):
        nodes[i] = 9999 # 9999は最大累積コスト

    current = start
    nodes[start] = 0
    while current != goal:
        # 確定したノード周りのコストを更新
        for j in range(n):
            if j not in nodes:
                continue
            if nodes[j] > nodes[current] + graph[current][j]:
                nodes[j] = nodes[current] + graph[current][j]
        del nodes[current]

        # 最小コストのノードを探索
        current = min(nodes.items(), key=lambda x: x[1])[0]
    
    return nodes[current]

if __name__ == '__main__':
    with open('A.in') as f:
        graph = None # 隣接行列
        while True:
            values = map(int, f.readline().split())
            if len(values) == 2:
                if graph is not None:
                    print solve(graph, s, g)
                    graph = None
                (n, m) = values
                graph = [ [9999] * n for i in range(n) ] # 9999は最大コスト
                if n == 0 and m == 0:
                    break
                (s, g) = map(int, f.readline().split())
            elif len(values) == 3:
                (i, j, c) = map(int, values)
                graph[i][j] = c
