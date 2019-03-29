INF = 10**10
def read():
    n = int(input())
    d = []
    for i in range(n):
        d.append(list(map(int, input().split())))
    return n,d


def distance(route, d):
    ret = 0
    for i in range(len(route)-1):
        ret += d[route[i]][route[i+1]]
    return ret


def solve(n, d):
    route = [0]
    used = [False] * n
    used[0] = True
    dist = d[0]
    neighb = [0] * n
    for i in range(n-1):
        nxt = -1
        td = INF
        for j in range(n):
            if used[j]:continue
            if td > dist[j]:
                nxt = j
                td = dist[j]

        ne = neighb[nxt]
        ind = route.index(ne)
        route = route[:ne] + [nxt] + route[ne:]
        used[nxt] = True
        for j in range(n):
            if used[j]:continue
            if dist[j] > d[nxt][j]:
                dist[j] = d[nxt][j]
                neighb[j] = nxt

    ind = route.index(0)
    route = route[ind:] + route[:ind]
    print("dist", distance(route + [0], d))
    print("route", route+[0])


def main():
    n,d = read()
    solve(n,d)
    
main()
        
