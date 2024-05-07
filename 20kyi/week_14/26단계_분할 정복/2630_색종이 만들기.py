# 하얀색으로 칠해진 칸은 0, 파란색으로 칠해진 칸은 1
# 첫째 줄에는 잘라진 햐얀색 색종이의 개수를 출력하고,
# 둘째 줄에는 파란색 색종이의 개수를 출력한다.

import sys

input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
result = []


def solution(x, y, n):
    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:
                solution(x, y, n // 2)
                solution(x, y + n//2, n // 2)
                solution(x + n//2, y, n // 2)
                solution(x + n//2, y + n//2, n // 2)
                return
    if color == 0:  # 하얀색
        result.append(0)
    else:  # 파란색
        result.append(1)


solution(0, 0, n)
print(result.count(0))
print(result.count(1))
