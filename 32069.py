# L=도로 길이
# N=가로등 갯수
# K=출력해야될 갯수
L,N,K=map(int,input().split())
A=list(map(int,input().split()))
darkness=[]

for x in range(L+1):
    diff=L
    for i in range(N): diff=min(diff,abs(x-A[i]))
    darkness.append(diff)
    darkness.sort()
    if diff==darkness[0] and len(darkness)>=K+1:
        darkness.pop(-1)

for j in range(K):
    print(darkness[j])