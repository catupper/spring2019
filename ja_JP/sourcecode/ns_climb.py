from random import randint

raw_input = input

INF = 10**10

def read():
    n,W = map(int, raw_input().split())
    vs = []
    ws = []
    for i in range(n):
        v,w = map(int, raw_input().split())
        vs.append(v)
        ws.append(w)

    return n, W, vs, ws

def brute_force(n, W, vs, ws):
    ans = 0
    snacks = 0
    for i in range(1 << n):
        vsum = 0
        wsum = 0
        used = []
        for j in range(n):
            if (i & (1 << j)) == 0:continue
            vsum += vs[j]
            wsum += ws[j]
            used.append(j)
        if wsum > W:continue
        if ans < vsum:
            ans = vsum
            snacks = used[:]
    print ("value", ans)
    print ("snacks", snacks)

def dynamic_programming(n, W, vs, ws):
    dp = [0] * (W+1)
    for i in range(n):
        for j in range(W, ws[i]-1, -1):
            dp[j] = max(dp[j], dp[j-ws[i]] + vs[i])

    print("value", max(dp))
        
def climb(n, W, vs, ws, trial = 1000000):
    snacks = list(range(n))
    knapsack = []
    vsum = 0
    wsum = 0
    for _ in range(trial):
        cand = randint(0, len(snacks) - 1)
        snack = snacks[cand]
        if W - wsum >= ws[snack]:
            knapsack.append(snack)
            vsum += vs[snack]
            wsum += ws[snack]
            del snacks[cand]
            continue

        tw = wsum
        tv = vsum
        tk = knapsack[:]
        go_back = []
        while W - tw < ws[snack]:
            tmp = randint(0, len(tk) - 1)
            ts = tk[tmp]
            go_back.append(ts)
            del tk[tmp]
            tw -= ws[ts]
            tv -= vs[ts]
        tw += ws[snack]
        tv += vs[snack]
        tk.append(snack)

        if tv > vsum:
            vsum = tv
            wsum = tw
            knapsack = tk[:]
            snacks += go_back
            del snacks[cand]
            
    print("value", vsum)
    print("snacks", sorted(knapsack))


def anealing(n, W, vs, ws, trial = 1000000):
    snacks = list(range(n))
    knapsack = []
    vsum = 0
    wsum = 0
    ans = 0
    ansknapsack = []
    for _ in range(trial):
        cand = randint(0, len(snacks) - 1)
        snack = snacks[cand]
        if W - wsum >= ws[snack]:
            knapsack.append(snack)
            vsum += vs[snack]
            wsum += ws[snack]
            del snacks[cand]
            continue

        tw = wsum
        tv = vsum
        tk = knapsack[:]
        go_back = []
        while W - tw < ws[snack]:
            tmp = randint(0, len(tk) - 1)
            ts = tk[tmp]
            go_back.append(ts)
            del tk[tmp]
            tw -= ws[ts]
            tv -= vs[ts]
        tw += ws[snack]
        tv += vs[snack]
        tk.append(snack)

        if tv > vsum or randint(0,trial) < (trial/_):
            vsum = tv
            wsum = tw
            knapsack = tk[:]
            snacks += go_back
            del snacks[cand]

        if ans < vsum:
            ans = vsum
            ansknapsack = knapsack[:]
    print("value", ans)
    print("snacks", sorted(ansknapsack))


def main():
    n, w, vs, ws = read()
    #brute_force(n, w, vs, ws)
    dynamic_programming(n, w, vs, ws)
    #climb(n, w, vs, ws)
    #anealing(n, w, vs, ws)

main()
    
