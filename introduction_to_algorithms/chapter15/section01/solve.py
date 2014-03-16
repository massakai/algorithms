# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # 問題
    num = 6
    a1 = (7, 9, 3, 4, 8, 4)
    a2 = (8, 5, 6, 4, 5, 7)
    e1 = 2
    e2 = 4
    t1 = (2, 3, 1, 3, 4)
    t2 = (2, 1, 2, 2, 1)
    x1 = 3
    x2 = 2

    # 初期設定
    f1 = [ e1 + a1[0] ]
    f2 = [ e2 + a2[0] ]

    # 部分問題を解く
    for i in range(1, num):
        s1 = min(f1[-1], f2[-1]+t2[i-1]) + a1[i]
        s2 = min(f2[-1], f1[-1]+t1[i-1]) + a2[i]
        f1.append(s1)
        f2.append(s2)

    # 解を求める
    ans = min(f1[-1]+x1, f2[-1]+x2)

    print ans

