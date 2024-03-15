def sel_ch(i, m) :
    if i == m :
        make_ch = []
        for l in range(m) :
            if bit[l] == 1 :
                make_ch.append(chicken[l])

        new_chicken.append(make_ch)
        return

    else :
        bit[i] = 1
        sel_ch(i+1, m)
        bit[i] = 0



N, M = map(int, input().split())    # NxN 거리 N / 남아있을 치킨집 개수 M

arr = [list(map(int, input().split())) for _ in range(N)]   # 도시 거리 받기
home = []       # 집이 있는 위치 받기 위한 리스트
chicken = []    # 치킨집이 있는 위치를 받기 위한 리스트
ch_lo = 0       # 치킨 거리를 넣을 변수
bit = [0] * len(chicken)    # 비트를 사용해보자... (선택 때문에)

for i in range(N) :
    for j in range(N) :
        if arr[i][j] == 1 :
            home.append((i,j))
        elif arr[i][j] == 2 :
            chicken.append((i,j))

if len(chicken) <= M :      # 살아남을 치킨집이 지금 있는 치킨집의 개수와 같거나 많다면,

    for hi, hj in home :
        loc = []
        for ci, cj in chicken :
            dis = abs(hi-ci) + abs(hj-cj)
            loc.append(dis)

        ch_lo += min(loc)

else :      # 살아남을 치킨이 지금 있는 치킨집의 개수보다 작을 경우,
    new_chicken = []
    sel_ch(0,M)

    print(new_chicken)