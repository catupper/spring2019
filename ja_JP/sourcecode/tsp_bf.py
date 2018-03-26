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

def next_permutation(l):
    n = len(l)
    
    i = n-2
    while i >= 0 and l[i] >= l[i+1]:
        i -= 1

    if i == -1:
        return False

    j = i + 1
    while j < n and l[j] > l[i]:
        j += 1
    j -= 1

    l[i],l[j] = l[j], l[i]

    left = i+1
    right = n-1

    while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1

    return True

def solve(n, d):
    route =list(range(1,n))
    min_dist = 10**9
    min_route = None

    while True:
        tmp = distance([0] + route + [0], d)
        if tmp < min_dist:
            min_dist = tmp
            min_route = route[:]
        if not next_permutation(route):
            break
    print("dist", min_dist)
    print("route", [0]+min_route+[0])


def main():
    n,d = read()
    solve(n,d)
    
main()
        
