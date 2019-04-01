[gimmick: math]()
# 計算困難問題


## 計算困難問題とは

計算困難問題(hard computing problem)は、計算にとても時間がかかる問題である。
まずは、計算にかかる時間という概念をもう少し厳密に扱うために、計算量という概念を説明しよう。


### 計算量
計算量というのは、ある問題を解くときにプログラムが実行する計算の回数を示す量である。

例えば1から100までの整数の総和を求めるとしよう。
最も単純な方法として、素直に99回足し算を行う方法がある。文字通り99回の計算が行われる。
それに対して、等差数列の和の公式((初項 + 末項)×項数 ÷2)を利用すれば、たかだか3回の計算で総和を求めることができる。
もしこれが100までではなくて \\( n \\) までだとしたらどうなるだろうか。
素直に全部足し合わせる方法だと計算回数は\\(n-1\\)回になり、公式を使う場合だと、どんな\\(n\\)に対しても3回となる。
この \\(n-1\\)や3がそれぞれのアルゴリズムの計算量である。
計算量を表す際は細かい数字より、最も支配的な項だけを抜き出すために、Ω記法やO記法を使う。

### Θ記法,O記法
**Θ記法**は関数の種類を表す記法である。\\(f(x) = Θ(g(x))\\)と書くことによって、f(x)はg(x)と同等のスケールで大きくなる関数だ、ということを表す。ここで、「同等のスケール」というのは、xを無限に大きくしていった時に、f(x)とg(x)の比が0に収束せず、また有る定数を超えることがない、ということを表す。
以下の例を見て、Θ記法のイメージを掴んで欲しい。

- \\(x^2+2x+4 = Θ(x^2) \\)
- \\(500x^3 + 10x- 2000000 + 1/x = Θ(x^3) \\)
- \\((x+4)^10 = Θ(x^{10}) \\)
- \\(2^x + x^3 = Θ(2^x) \\)
- \\(0.8^x + x^3 - \sin(x) = Θ(x^3) \\)

**O記法**はΩ記法の仲間である。\\(f(x) = O(g(x))　\\)と書くことによって、f(x)はg(x)と同等かそれより小さいスケールで大きくなることを表す。\\(f(x) < h(x), h(x) = Θ(g(x)) \\)となる\\(h(x)\\)が存在するなら、\\(f(x)=O(g(x)) \\)である。
Θ記法が「イコール」に対応するなら、O記法は「小なりイコール」に対応すると考えてもらって良い。

### 多項式時間、指数時間
ある種類の問題を解くアルゴリズムが、問題に出てくるデータのサイズに対してどれくらいの計算量がかかるか、というのが計算機科学の興味である。
たとえば、「整数がN個与えられて、その総和を求める愚直なアルゴリズムの計算量は\\(O(N)\\)である」とか「整数がN個与えられて、和が0になる3つ組が存在するかどうかは\\(O(N^2)\\)の計算量で判定できる」というふうにアルゴリズムの計算量を議論する。

ある問題を解くアルゴリズムが、問題のサイズNに対して、ある多項式f(N)が存在して、\\(O(f(N))\\)の時間で動作するとき、そのアルゴリズムは**多項式時間アルゴリズム**と呼ぶ。
また、f(N)が指数関数の時は**指数時間アルゴリズム**と呼ぶ。

### 計算困難問題
これから扱っていく計算困難問題は、**指数時間アルゴリズム**は見つかっているが、**多項式時間アルゴリズム**は見つかっていない、あるいは無いと予想されている問題である。
代表的な問題として充足可能性問題(SAT)や巡回セールスマン問題(TSP)などがある。
まずは、多項式時間では解けないとされている問題の中でも特に有名な**巡回セールスマン問題**を見ていこう。



## 巡回セールスマン問題

巡回セールスマン問題(travelling salesman problem)とは以下の形式の問題である。

「\\(N\\)個の街がある。\\(i\\)番目の街と\\(j\\)番目の街は距離\\(d_{i,j}\\)の道で結ばれている。0番目の街から開始して、全ての街をちょうど1回ずつ通ってもう一度０0目の街に帰ってくるルートのうち、総移動距離が最小のものを求めよ。」

まずはこの問題の様々な解法を実装して速さを比べてみよう。

### 入力形式

この先、巡回セールスマン問題を解くアルゴリズムをいくつか紹介し、実装もする。それにあたって、どのような形式で問題が与えられるかを決めておかないと不便である。
全ての実装において、標準入力から、以下の形式で問題を受け取るということにする。

```
N
d_0,0 d_0,1 d_0,2 .. d_0,N-1
d_1,0 d_1,1 d_1,2 .. d_1,N-1
:
d_N-1,0 d_N-1,1 d_N-1,2 .. d_N-1,N-1

```

つまり、最初の1行には巡回する街の個数が書かれており、続く\\(N\\)行にはそれぞれ\\(N\\)個の数字が書かれており、\\(i\\)行\\(j\\)列目は街\\\(i\\)と街\\(j\\)の距離が書かれている。

また、以下の制約も課すことにする。

- \\( d_{i,j} \\)　は非負整数
- \\( d_{i,i} = 0 \\)
- iとjの距離はjとiの距離と等しい
- 入力や答えは\\(10^{10}\\)を超えない


以下に入力を受け取って、二次元配列dに各街の間の距離を格納する関数のpythonでの実行を挙げる。他の言語を使っている人は適宜実装しなおしてほしい。

```python:read.py
def read():
    n = int(input())
    d = []
    for i in range(n):
        d.append(list(map(int, input().split())))
    return d
```

この部分はどのアルゴリズムでも使用するので、どこかに別名で保存しておくと良いだろう。

### 全探索
まずは、最もシンプルな全探索アルゴリズムを見ていこう。これは街をめぐる順序を全通り試すというものである。
0番目以外の街を何らかの順番で1回ずつ通るルートは全部で\\( (N-1)! \\) 通りある。うまい具合にこれらを列挙して、その中で最も距離が短いものを返せば、巡回セールスマン問題は解ける。
ルートを一つ決めたとき、そのルートの総移動距離はO(N)で求まるので、このアルゴリズムの計算量はO(N!)となる。これは指数時間アルゴリズムですらなく、とても遅いアルゴリズムになるが、実装は簡単で、正当性が明らかなので、試しに実装するにはちょうどよい。

以下に全探索プログラムを挙げる。
```python:bf.py
INF = 10**10 #無限大の代わり
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
    min_dist = INF
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
```

`next_permutation(l)`関数はリストlを受け取って、lをひとつ次の順列に変換する関数である。戻り値は、変換に成功したかどうかである。
ｌを昇順にソートされたリストとして、`next_permutation(l)`に順次かけていくと、全ての順列を経由した後に、降順にソートされて終了する。
`next_permutation`の実装はとても難解なので、よく読んで理解しよう。

実装ができたら試しに、以下の入力で動作を確認すると良い。

```
4
0 1 1 2
1 0 2 3
1 2 0 4
2 3 4 0
```
うまく動けば以下のルートが得られるはずだ
```
dist 8
route [0, 2, 1, 3, 0]
```

### 動的計画法
全探索をすると、計算量が指数どころか階乗になってしまい、とても遅い。まずは代表的な指数時間アルゴリズムである動的計画法を実装してみよう。

動的計画法のアイデアは、「頂点0から出発して、頂点集合Vを経由し、頂点iに来るときの最短経路を求める」という部分問題を解くということである。

上のカギカッコで囲まれた部分の答えとなる値をdp[V][i]としよう。このときiはVに含まれるとする。
Vからiを取り除いた頂点集合をWとしよう。すると

\\(dp[V][i] = min_{j \in W} {dp[W][j] + d[j][i]} \\)

が、成立する。これはiに訪れる一つ前の頂点について全探索していることになる。
Vのサイズが小さい順にdp配列を埋めていけば、全ての要素がO(N)で求めることができる。
dp配列のサイズはO(N2^N)なので、全部でO(N^2 2^N)でこのアルゴリズムは動作する。

以下にその実装を示す。
```python
INF = 10**10 #無限大の代わり
def solve(n, d):
    dp = [[INF]*n for i in range(1<<n)]
    dp[1][0] = 0

    for v in range(2,1<<n):
        for i in range(1,n):
            if (v & (1<<i))== 0:
                continue
            for j in range(n):
                if i == j or (v & (1 << j)) == 0:
                    continue
                dp[v][i] = min(dp[v][i], dp[v - (1<<i)][j] + d[j][i])

    res = INF
    for i in range(1,n):
        res = min(res, dp[(1<<n)-1][i] + d[i][0])

    print("dist", res)


def main():
    n,d = read()
    solve(n,d)

main()
```

これも、全探索にある入力例で動作確認をすると良いだろう。

####演習
上の実装では最短経路の距離しか表示されない。その距離を実現する最短経路も一緒に表示するように改変してみよ。
(Hint:dp[V][i]が最後に更新された時のjを覚えておくと良い)

## ナップザック問題

ナップザック問題(Knapsack problem)とは以下の形式の問題である。

「\\(N\\)個のお菓子と重量制限\\(W\\)のナップザックがある。\\(i\\)番目のお菓子の価値は\\(V_i\\)で重さは\\(W_i\\)である。重さの総和が\\(W\\)を超えないようにナップザックにお菓子を詰め込むとき、ナップザックの中のお菓子の価値の総和を最大化せよ。」
この問題も全探索と、動的計画法で解いてみよう。

### 入力形式

ナップザック問題は、全ての実装において、標準入力から、以下の形式で問題を受け取るということにする。

```
N　W
v_0 w_0
v_1 w_1
:
v_N-1 w_N-1

```

つまり、最初の1行にはスナックの個数が書かれており、続く\\(N\\)行にはそれぞれ\\(i\\)番目のスナックの価値と重さが書かれている。

また、以下の制約も課すことにする。

- \\( v_i, w_i \\)　は非負整数
- 入力や答えは\\(10^{18}\\)を超えない


以下に入力を受け取って、二次元配列dに各街の間の距離を格納する関数のpythonでの実行を挙げる。他の言語を使っている人は適宜実装しなおしてほしい。

```python:read.py
def read():
    n,W = map(int, input().split())
    vs = []
    ws = []
    for i in range(n):
        v,w = map(int, input().split())
        vs.append(v)
        ws.append(w)

    return n, W, vs, ws

```

この部分はどのアルゴリズムでも使用するので、どこかに別名で保存しておくと良いだろう。

###全探索アルゴリズム

まずは、どのお菓子を使って、どのお菓子を使わないかの組み合わせを全通り試す全探索を実装しよう。
お菓子の組み合わせは巡回セールスマン問題と同様に二進数を使って表そう。

```python:bruteforce.py
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


def main():
    n, w, vs, ws = read()
    brute_force(n, w, vs, ws)

main()
```

この前探索のアルゴリズムは、iに関するfor文が\\(O(2^N)\\)回ループし、中のjに関するfor文が\\(O(N)\\)回ループするので、\\(O(NN^2)\\)の計算量である。
これは指数時間アルゴリズムである。

###動的計画法

ナップザック問題における動的計画法のアイデアは、「\\(i\\)番目のお菓子までの中からいくつかを選んで重さの総和が\\(j\\)になる組わせの価値の総和の最大値は何か」という部分問題を解くことである。

上のカギカッコで囲まれた部分の答えとなる値をdp[i][j]としよう。すると

\\(dp[i][j] = max(dp[i-1][j], dp[i-1][j-w_i] + v_i) \\)

が、成立する。iが小さい順にdp配列を埋めていけば、全ての要素がO(1)で求めることができる。
dp配列のサイズはO(NW)なので、全部でO(NW)でこのアルゴリズムは動作する。

一見これは多項式時間アルゴリズムに見えるが、Wは入力のサイズとは関係ない値なので（強いて言うならばその桁数が入力のサイズとなるので、指数オーダーで大きくなる値)、多項式時間アルゴリズムではない。
これは**擬多項式時間アルゴリズム**である。

以下に実装を示す

```python:dp.py
def dynamic_programming(n, W, vs, ws):
    dp = [0] * (W+1)
    for i in range(n):
        for j in range(W, ws[i]-1, -1):
            dp[j] = max(dp[j], dp[j-ws[i]] + vs[i])

    print("value", max(dp))

def main():
    n, w, vs, ws = read()
    dynamic_programming(n, w, vs, ws)

main()
```

####演習
上の実装では最適解が表示されるだけで、ナップサックに入れるお菓子は表示されない。表示されるように書きなおしてみよ。


## 計算困難問題に対するアルゴリズム
巡回セールスマン問題でもナップサック問題でも、動的計画法は全探索よりは速く動いたがそれでも指数時間アルゴリズムなので大きなサイズの問題を解くのには時間がかかりすぎてしまう。
しかし、必ず正しい最短巡回路長を返すアルゴリズムで多項式時間であるものは未だに見つかっていない。そのようなものは存在しないという予想さえある。

ここで、最適解より少し悪いかもしれないが、そんなに悪くない解を出すことが保証されていたり、経験的にわかっていたりするアルゴリズムをいくつか紹介する。

### 山登り法

山登り法は、最適ではないかもしれない解から出発して、解が改善するように小さな変化をつけていく、これ以上どう変化させても解は改善しないという状態まで持っていくアルゴリズムである。
ナップザック問題の場合、「適当にお菓子を詰め込んだ後、まだ詰め込んでないものをひとつ選んで、それを詰め込めるように別のお菓子を適当に取り出す。この詰め替えでお菓子の価値の和が増えるなら、この詰替えを実施し、そうでないなら実施しない」というのを何度もやることは山登り法になる。
以下に山登り法でナップザック問題を解くpythonプログラムを示す。
```python:climb.py
def climb(n, W, vs, ws, trial = 100000):
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

def main():
    n, w, vs, ws = read()
    climb(n, w, vs, ws)

main()

```
山登り法は、最適解の到着するまで動かし続ければ良いのだが、最適解じゃないところにとどまってしまったり、そもそも最適解かどうかの判定が難しかったりするので、通常は何回ループを回すかを指定して動かすことが多い。
そのため、最適解が得られる保証は無いが、プログラムが走る時間を自由に調節することができる。

####演習(興味があれば)
巡回セールスマン問題を山登り法で解くアルゴリズムを実装してみよ。
巡回セールスマン問題における山登りの例として、適当な2つの街の訪れる順序の入れ替えを、経路長が改善されたら実施し、そうでないなら実施しないというのを何回も行うものである。

### 焼きなまし法
焼きなまし法は、山登り法を改良したものである。山登り法は、とにかく解が良くなる方向に進み続ける方針であるが、局所的に最適だが、全体としては最適ではない解にとどまってしまうことが有る。
そこで、低確率で解が悪くなる方向にも進むようにするというのが焼きなまし法である。実装はほとんど山登り法と同じだが、変更を加えるか加えないかの判断の条件式が少し増える。

```python:anealing.py
from random import randint
def anealing(n, W, vs, ws, trial = 100000):
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
    climb(n, w, vs, ws)

main()

```
ナップサック問題の場合、探索空間に置いて近傍が広いため、焼きなまし法と山登り法であまり結果に差がつかない。
近傍がそんなに多くない山登り法を使う巡回セールスマン問題などでは、焼きなまし法に変更することで結果が良くなることが見込める。

####演習問題
様々なサイズのナップサック問題を用意して、それぞれのアルゴリズムのスピードと、解答の精度を比べてみよ。


##近似アルゴリズム

近似アルゴリズムは多項式時間アルゴリズムのなかで、最適からそんなに離れていない解を返すことが保証されているアルゴリズムである。
たとえば、最小値の2倍よりは小さい値を返すことが保証されてるアルゴリズムは近似アルゴリズムの例であり、2-近似アルゴリズムと呼ばれる。
以下では、巡回セールスマン問題の2近似アルゴリズムを紹介する。
ただし、これらのアルゴリズムは三角不等式が成り立つことが前提となっている。

###最近挿入法
最近挿入法は、街0だけからなる巡回路に、いまの巡回路に近い街から順にひとつずつ巡回路に挿入していく方法である。

厳密には以下のようなアルゴリズムになる。

1. S=[0]とする
1. Sに含まれる街と、それ以外の街の距離の中で、最も短いものを見つけてくる。Sに含まれる方をu, 含まれない方をvとする。
1. Sのなかでuの直後にvを挿入する。
1. 全ての街がSに含まれたなら終了し、そうでないなら2に戻る。

実際に実装すると以下のようになる
```python:nearest.py
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
```
####演習問題
自分でテストケースを作ってみて最近挿入法を試してみよ。小さいケースでは動的計画法が返す最適解と比較して、2近似になっていることを確かめよ。

####演習問題
2次元平面上のN点の最短巡回路をもとめて可視化してみよ。javascriptやPILやgnuplotを使っても良いが、Processingが書けるならば、Processingのコードを出力するプログラムを作るのが一番楽だろう。

###大きめな入出力例
https://github.com/catupper/spring2019/tree/gh-pages/ja_JP/sourcecode
このページに大きめな入出力例がある。試してみよう。
