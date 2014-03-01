# -*- coding: utf-8 -*-
u"""ACM International Collegiate Programming Contest Japan Domestic, 2004-07-02
Problem B: Red and Black
"""

class Solver(object):
    u"""問題を解くクラス"""
    BLACK = "."
    RED   = "#"
    START = "@"
    
    def __init__(self, filename):
        self.dataset_file = open(filename)

    def __del__(self):
        self.dataset_file.close()
        
    def solve(self, x, y):
        u"""問題を解く。"""
        if self.dataset[y][x] == self.RED:
            return 0
        # 探索済みの印としてREDにする
        # self.dataset[y][x] = self.RED （文字列の変更はできないため）
        self.dataset[y] = self.dataset[y][:x] + self.RED + self.dataset[y][x+1:]
        
        return 1 + self.solve(x-1, y) + self.solve(x+1, y) + self.solve(x, y-1) + self.solve(x, y+1)

    def load_dataset(self):
        u"""次のデータセットを読む。"""
        (w, h) = map(int, self.dataset_file.readline().split())
        if w == 0 and h == 0:
            return None

        wall = self.RED * (w + 2)
        dataset = [ wall ]
        for i in range(1, h+1):
            line = self.RED + self.dataset_file.readline().strip() + self.RED
            index = line.find(self.START)
            if index != -1:
                self.start_x = index
                self.start_y = i
            dataset.append(line)
        dataset.append(wall)
        
        self.dataset = dataset
        return dataset

def read_args(argv):
    u"""実行引数を読み込む。"""
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', nargs=1, help="Input file")
    
    args = parser.parse_args(argv)
    ret = {'input': args.input[0]}
    
    return ret

if __name__ == "__main__":
    import sys

    args = read_args(sys.argv[1:])
    solver = Solver(args['input'])
    while solver.load_dataset() is not None:
        print(solver.solve(solver.start_x, solver.start_y))
