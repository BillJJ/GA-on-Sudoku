import time

with open("puzzle.txt", "r") as f:
    a = list(map(list, f.read().split()))

stk = []
for i in range(9):
    for j in range(9):
        if a[i][j] == '.':
            stk.append((i, j))
boxes = [[(0,0) for i in range(9)] for j in range(9)]
for i in range(9):
    for j in range(9):
        boxes[(i//3)*3 + j//3][int(i%3)*3 + int(j%3)] = (i,j)

global idx
idx = 0
def f():
    global idx
    if idx == len(stk):
        print(*a, sep='\n')
        return 1

    x, y = stk[idx]
    vis = [0 for i in range(9)]
    for i in range(9):
        if a[x][i] != '.': vis[ord(a[x][i])-ord('1')] = 1
        if a[i][y] != '.': vis[ord(a[i][y])-ord('1')] = 1
    for i,j in boxes[(x//3)*3 + y//3]:
        if a[i][j] != '.': vis[ord(a[i][j])-ord('1')] = 1

    idx += 1
    for i in range(9):
        if vis[i]: continue
        a[x][y] = chr(i+ord('1'))
        f()
        a[x][y] = '.'
    idx -= 1
    return

f()


if __name__ == '__main__':
    start = time.time()
    f()
    print(time.time() - start)
