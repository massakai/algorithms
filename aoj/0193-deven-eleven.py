import sys

def generate_next_hexes(x, y):
    hexes = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
    if y % 2:
        hexes += [(x - 1, y - 1), (x - 1, y + 1)]
    else:
        hexes += [(x + 1, y - 1), (x + 1, y + 1)]
    hexes = [(a, b) for (a, b) in hexes if 1 <= b <= m and 1 <= b <= n]
    return hexes

def update_map(hex_map, hexes):
    num_updated_hexes = 0
    distance = 0
    while hexes:
        next_hexes = []
        for pos in hexes:
            if pos not in hex_map or distance < hex_map[pos]):
                hex_map[pos] = distance
                num_updated_hexes += 1
                next_hexes += generate_next_hexes(pos[0], pos[1])
        distance += 1
        hexes = next_hexes
    return num_updated_hexes

while True:
    (m, n) = [int(i) for i in sys.stdin.readline().split()]
    if m == n == 0:
        break

    s = int(sys.stdin.readline())
    stores = []
    for i in range(s):
        pos = [int(j) for j in sys.stdin.readline().split()]
        stores.append(tuple(pos))
    hex_map = {}
    update_map(hex_map, stores)

    t = int(sys.stdin.readline())
    candidates = []
    for i in range(t):
        pos = [int(j) for j in sys.stdin.readline().split()]
        candidates.append(tuple(pos))

    max_num_blocks = 0
    for candidate in candidates:
        new_hex_map = hex_map.copy()
        num_blocks = update_map(new_hex_map, [candidate])
        max_num_blocks = max(max_num_blocks, num_blocks)

    print(max_num_blocks)
