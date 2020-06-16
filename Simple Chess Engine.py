import os
import sys

knight = [(-1, -2), (-2, -1), (-1, 2), (-2, 1), (1, -2), (2, -1), (1, 2), (2, 1)]
rook = [(-1, 0), (1, 0), (0, -1), (0, 1)]
bishop = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
queen = rook + bishop

pieces = {'N': knight, 'B': bishop, 'R': rook, 'Q': queen}

def initializr(player, opponent, x, y):
    if not (0 <= x <= 3 and 0 <= y <= 3):
        return -1, -1
    for i in range(len(opponent)):
        zz, xx, yy = opponent[i]
        if zz != ' ' and xx == x and yy == y:
            return (2 if zz == 'Q' else 1), i
    for zz, xx, yy in player:
        if zz != ' ' and xx == x and yy == y:
            return -1, -1
    return 0, -1

def game(player, opponent, xx, yy, direction):
    if direction == knight:
        for dx, dy in direction:
            x = xx + dx
            y = yy + dy
            k, i = initializr(player, opponent, x, y)
            if k >= 0:
                yield x, y, k, i
    else:
        for dx, dy in direction:
            x = xx
            y = yy
            while True:
                x = x + dx
                y = y + dy
                k, i = initializr(player, opponent, x, y)
                if k < 0:
                    break
                yield x, y, k, i
                if k > 0:
                    break

def calculate(player, opponent, moves):
    res = -2
    for num in range(len(player)):
        zz, xx, yy = player[num]
        if zz != ' ':
            for x, y, k, i in game(player, opponent, xx, yy, pieces[zz]):
                if k == 2:
                    return 1
                if moves > 1:
                    if i >= 0:
                        temp = opponent[i][0]
                        opponent[i][0] = ' '
                    player[num][1:] = [x, y]
                    rr = -calculate(opponent, player, moves - 1)
                    if i >= 0:
                        opponent[i][0] = temp
                    player[num][1:] = [xx, yy]
                    res = max(rr, res)
                    if res == 1:
                        return 1
    return 0 if res == -2 else res


def simplifiedChessEngine(whites, blacks, moves):
    if moves % 2 == 0:
        moves -= 1
    for a in [whites, blacks]:
        for b in a:
            b[1] = ord(b[1]) - ord('A')
            b[2] = ord(b[2]) - ord('1')
    return 'YES' if calculate(whites, blacks, moves) == 1 else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        wbm = input().split()

        w = int(wbm[0])

        b = int(wbm[1])

        m = int(wbm[2])

        whites = []

        for _ in range(w):
            whites.append(list(map(lambda x: x[0], input().rstrip().split())))

        blacks = []

        for _ in range(b):
            blacks.append(list(map(lambda x: x[0], input().rstrip().split())))

        result = simplifiedChessEngine(whites, blacks, m)
        fptr.write(result + '\n')

    fptr.close()