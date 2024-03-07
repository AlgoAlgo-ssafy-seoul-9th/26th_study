N, M = map(int, input().split())
jewel = []
for _ in range(N):
    w, v  = map(int, input().split())
    jewel.append((v/w, w, v))

jewel.sort(reverse=True) # 무게당 가치가 높은 것부터

total_v = 0
total_w = 0
for i in range(N):
    if (total_w + jewel[i][1])>M:   # i를 다 담을 수 없으면
        total_v += (M-total_w)*jewel[i][0] # 남은 용량 만큼 잘라서 담음
        break
    else:
        total_w += jewel[i][1]  #
        total_v += jewel[i][2]
print(f'{total_v:.3f}')
