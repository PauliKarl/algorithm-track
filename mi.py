M, K, N = 2,3,2
A=[[1,2,3],[1,2,3]]
B=[[1,1],[1,1],[1,1]]

C = [[0 for i in range(N)] for j in range(M)]

for i in range(M):
    for j in range(N):
        for k in range(K):
            C[i][j] = C[i][j] + A[i][k]*B[k][j]
for t in range(M):
    for n in range(N):
        print(C[t][n], end="")
        if n<N-1:
            print(end = " ")
    if t<M-1:
        print(end="\n")