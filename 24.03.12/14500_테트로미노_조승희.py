# 메모리 37584 KB / 시간 1340 ms


N, M = map(int, input().split())        # 세로 N 가로 M
arr = [list(map(int, input().split())) for _ in range(N)]   # 점수들 받기
max_v = 0   # 최댓값을 저장하기 위한 변수 생성

# 1) 일자 먼저 확인하기 // 일자 같은 경우, 가로로 쭉 or 세로로 쭉 두가지이다.
for i in range(N) :
    for j in range(M-3) :
        cnt = 0
        cnt = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i][j+3]

        if max_v < cnt :
            max_v = cnt

for j in range(M) :
    for i in range(N-3) :
        cnt = 0
        cnt = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+3][j]

        if max_v < cnt :
            max_v = cnt

# 2) 네모네모 확인하기
for i in range(N-1) :
    for j in range(M-1) :
        cnt = 0
        cnt = arr[i][j] + arr[i+1][j] + arr[i][j+1] + arr[i+1][j+1]

        if max_v < cnt :
            max_v = cnt


# 가로(M)가 2, 세로(N)가 3일 때
for i in range(N-2) :
    for j in range(M-1) :
        all = 0
        all = arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1]

        v1 = all - arr[i][j+1] - arr[i+1][j+1]
        v2 = all - arr[i][j] - arr[i+1][j]
        v3 = all - arr[i+1][j+1] - arr[i+2][j+1]
        v4 = all - arr[i+1][j] - arr[i+2][j]
        v5 = all - arr[i][j+1] - arr[i+2][j]
        v6 = all - arr[i][j] - arr[i+2][j+1]
        v7 = all - arr[i][j] - arr[i+2][j]
        v8 = all - arr[i][j+1] - arr[i+2][j+1]

        cnt = max(v1, v2, v3, v4, v5, v6, v7, v8)

        if max_v < cnt :
            max_v = cnt

# 4) 가로(M)가 3, 세로(N)가 2
for i in range(N-1) :
    for j in range(M-2) :
        all = 0
        all = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j] + arr[i+1][j+1] + arr[i+1][j+2]

        v1 = all - arr[i][j+1] - arr[i][j+2]
        v2 = all - arr[i][j] - arr[i][j+1]
        v3 = all - arr[i+1][j+1] - arr[i+1][j+2]
        v4 = all - arr[i+1][j] - arr[i+1][j+1]
        v5 = all - arr[i][j+2] - arr[i+1][j]
        v6 = all - arr[i][j] - arr[i+1][j+2]
        v7 = all - arr[i][j] - arr[i][j+2]
        v8 = all - arr[i+1][j] - arr[i+1][j+2]

        cnt = max(v1, v2, v3, v4, v5, v6, v7, v8)

        if max_v < cnt:
            max_v = cnt

print(max_v)