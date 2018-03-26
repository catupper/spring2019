def read():
    n = int(input())
    d = []
    for i in range(n):
        d.append(list(map(int, input().split())))
    return n,d

def solve(n, d):
    dp = [[10**10]*n for i in range(1<<n)]
    dp[1][0] = 0

    for v in range(2,1<<n):
        for i in range(1,n):
            if (v & (1<<i))== 0:
                continue
            for j in range(n):
                if i == j or (v & (1 << j)) == 0:
                    continue
                dp[v][i] = min(dp[v][i], dp[v - (1<<i)][j] + d[j][i])

    res = 10**10
    for i in range(1,n):
        res = min(res, dp[(1<<n)-1][i] + d[i][0])

    print("dist", res)
            

def main():
    n,d = read()
    solve(n,d)
    
main()
        
