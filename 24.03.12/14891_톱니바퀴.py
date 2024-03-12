# N극은 0 / S극은 1
# 시계방향 1 / 반시계 방향 -1
from collections import deque   # 덱을 써보자!

gear_1 = list(input())
gear_2 = list(input())
gear_3 = list(input())
gear_4 = list(input())

g1 = deque()
g2 = deque()
g3 = deque()
g4 = deque()

g1.append(2)
g2.append(2)
g3.append(2)
g4.append(2)

N = int(input())        # 톱니바퀴를 회전시키는 횟수

for _ in range(N) :
    num, dir = map(int, input().split())    # 돌릴 톱니바퀴 번호 num / 돌릴 방향 dir

    if num == 1 :
        p1 = g1.popleft()
        p2 = g2.popleft()

        if gear_1[p1] != gear_2[p2+4] :
            if dir == 1 :   # 돌릴 방향이 시계방향이라면,
                n_p1 = p1 - 1
                n_p2 = p2 + 1
                if n_p1 == 8 :
                    n_p1 = 0
                elif n_p1 == -1 :
                    n_p1 = 7

                if n_p2 == 8 :
                    n_p2 = 0
                elif n_p2 == -1 :
                    n_p2 = 7

                g1.append(n_p1)
                g2.append(n_p2)
            else:
                n_p1 = p1 + 1
                n_p2 = p2 - 1
                if n_p1 == 8:
                    n_p1 = 0
                elif n_p1 == -1:
                    n_p1 = 7

                if n_p2 == 8:
                    n_p2 = 0
                elif n_p2 == -1:
                    n_p2 = 7

                g1.append(n_p1)
                g2.append(n_p2)
        else :
            g1.append(p1)
            g2.append(p2)
            continue

