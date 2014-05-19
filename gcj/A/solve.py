# -*- coding: utf-8 -*-

if __name__ == '__main__':
    f = open('data.in')
    case = int(f.readline().strip())
    for i in range(1, case+1):
        row = set([ i for i in range(1, 17) ])
        for j in range(2):
            answer = int(f.readline().strip())
            for k in range(1, 5):
                line = f.readline()
                if answer == k:
                    row = row.intersection(map(int, line.split()))
        if len(row) == 1:
            print('Case #%d: %d' % (i, list(row)[0]))
        elif len(row) > 1:
            print('Case #%d: Bad magician!' % i)
        else:
            print('Case #%d: Volunteer cheated!' %i)
