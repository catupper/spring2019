# 言語処理系

**言語処理系** というのはプログラミング言語を受け取って、何らかの処理をしてくれるソフトウェアのことである。Processing, Python, C/C++など様々な言語があるが、人間が書いたソースコードが無事にプログラムとして実行されるまでには、言語処理系が間に挟まって、ソースコードの解釈や、機械語への変換を行っている。
本テーマでは、いろいろなタイプの言語処理系を作ってみて、最終的にはひとつ言語を自作するなどしてもらう。

このページではサンプルコードは全てPython3で書かれているが、受講者が好きな言語を使ってもらって構わない。

## インタプリタとコンパイラ

言語処理系は**インタプリタ型**と**コンパイラ型**に大別される。

インタプリタ型言語は、ソースコードを機械語に翻訳せずに実行する言語処理系である。Python, Rubyなどがインタプリタ型言語の例である。プログラムを上から順番に読んでいって逐一実行するだけ、という実装が多いので、対話型コンソールとの相性がよい。

それに対して、コンパイラ型言語は、ソースコードを一度機械語に変換してからプログラムを実行する。一般には機械語に変換するところまでがコンパイラ型言語処理系の仕事である。例えばC言語でプログラムをコンパイルするとa.exeなどと言った実行ファイルが出来上がるが、これがソースコードが機械語に翻訳されたものである。
機械語に変換するまでに時間がかかるが、その後の実行速度はインタプリタ型と比較すると速くなる。

コンパイル型原碁を自作する場合は機械語の知識が必要で、少し難しいので、今回はインタプリタ型言語を作成することにする。

## HQ9+

まずは[HQ9+](https://ja.wikipedia.org/wiki/HQ9%2B)というプログラミング言語の処理系を作ってみよう。
HQ9+はほとんど何もできないジョーク言語だが、処理系を作る練習として選ぶには良い言語である。

### HQ9+ の仕様
HQ9+の仕様を以下に挙げる。

- ソースコードを先頭から順に読んでいくインタプリタ型言語である。
- ソースコードを読んでいき'H'が出てきたら、'Hello, World!'を出力する。
- ソースコードを読んでいき'Q'が出てきたら、ソースコードを出力する。
- ソースコードを読んでいき'9'が出てきたら、"99 Bottles of Beer"の[歌詞](http://99-bottles-of-beer.net/lyrics.html)を出力する。
- ソースコードを読んでいき'+'が出てきたら、アキュムレータの値を1増やす。
- それ以外の文字が出てきた場合は、何もしない。

ここでアキュムレータというのは、プログラムの裏側にある変数だと思ってもらえれば良い。プログラム開始時にはアキュムレータは0に初期化されている。
このアキュムレータの値を出力することはないので、実際にアキュムレータを実装する必要はないのだが、練習のために今回は実装してみよう。

### HQ9+ の実装

まず雛形としてソースコードを読み取る関数`read_code`を作ってみよう。
コマンドライン引数からソースコードのパスを読み取り、その内容を返す関数である。
コマンドライン引数の個数がおかしかったり、与えられたパスが存在しなかった場合も適切にエラー処理をする。
`sys.argv` はコマンドライン引数の配列である。
`python hoge.py fuga piyo`というふうに`hoge.py`を実行したならば`sys.argv`は`["hoge.py", "fuga", "piyo"]`となる。

```python:read.py
import sys
import os.path

argvs = sys.argv
argc = len(argvs)

def read_code():
    if argc == 1:
        print("no source file")
        exit()
    if argc > 2:
        print("too many arguments")
        exit()

    filename = argvs[1]

    if not os.path.exists(filename):
        print("no such file:{}".format(filename))
        exit()

    with open(filename, "r") as f:
        sourcecode = f.read()
    return sourcecode
```

この雛形は他の言語を作るときにも利用するのでローカルに名前を付けて保存しておくと良いだろう。

次に、ソースコードを順に読み、コマンドを実行していく関数`process(sourcecode)`を書こう。各コマンドの処理はまだ具体的に書かず、関数の形で置いておく。

```python:process.py
def process(sourcecode):
    accumulator = 0
    for c in sourcecode:
        if c == 'H':command_h()
        if c == 'Q':command_q(sourcecode)
        if c == '9':command_9()
        if c == '+':command_plus()
```

あとは、それぞれのコマンドを実装するだけである。ここではHと+の実装例を示すので、残りの2コマンドは自分で実装してみてほしい。

```python:commands.py
def command_h():
    print("Hello, World!")

def command_plus():
    global accumulator
    accumulator += 1
    
def command_9():
    #自分で実装する
    pass

def command_q(sourcecode):
    #自分で実装する
    pass
```


### 演習:自作機能を追加してみよう

HQ9+は見ての通り低機能なプログラミング言語である。ここに自分の好きなコマンドを追加してみよう。以下に挙げるのは講師が思いついた例であるが、ここにないものでもよい。

- Fコマンド: 1から100までのFizzBuzzを出力する
- Oコマンド：アキュミュレータの値を出力する
- -コマンド：アキュミュレータの値を1減らす

## BrainF**k

次に、HQ9+より高機能な**BrainF\*\*k**の実装をしてみよう。BrainF\*\*kはチューリング完全といって、チューリングマシンと同等の処理能力が有るプログラミング言語である。C/C++やPythonのような、いわゆる「なんでもできるプログラミング言語」だと考えてもらって構わない。

### BrainF**kの仕様
BrainF**kの仕様を以下に挙げる。

- ソースコードを先頭から順に読んでいくインタプリタ型言語である。
- '>'が出てきたら、ポインタをインクリメントする。
- '<'が出てきたら、ポインタをデクリメントする。
- '+'が出てきたら、ポインタが指している値をインクリメントする。
- '-'が出てきたら、ポインタが指している値をデクリメントする。
- '.'が出てきたら、ポインタが指す値の文字コードを持つ文字を出力する。
- ','が出てきたら、入力から1文字読み込んで、その文字コードの値をポインタが指す先に代入する。
- '['が出てきたら、ポインタが指す値が0なら対応する']'にジャンプする。
- ']'が出てきたら、ポインタが指す値が0でないなら、対応する'['にジャンプする。
- それ以外の文字が出てきた場合は、何もしない。

仕様に出てきた「ポインタ」という単語について説明しよう。
HQ9+ではアキュムレータという変数のようなものがあったが、BrainF**kでは無限に長い一次元配列が裏にあると考えてもらってよい。
はじめ、その配列の値は全て0で初期化されており、ポインタがある要素を指している。
ポインタがインクリメントされると、そのひつ次の要素を指すようになり、デクリメントすると、その一つ前の要素を指すようになる。
ポインタが指す要素の値を変えたいならば'+'や'-'を使って値を書き換える。

また、'.',','でポインタの指す値の文字コードに対応する文字がないとうまく動かないので、'+'や'-'コマンドは256で割ったあまりを動くとする。つまり255をインクリメントすると0, 0をデクリメントすると255になる仕様であるとする。

### BrainF**kの実装

`read_code`はHQ9+と同じものを使って構わない。
HQ9+のときはアキュミュレータをグローバル変数として実装したが、実際にはこのような実装はあまり美しくない。今回はBFクラスを作成して、各コマンドや内部環境をそのクラスのインスタンスとして実装しよう。
実際に無限に長い配列を用意することはできないので、十分長い配列としてサイズ1000の配列を用意して、初めポインタは500番目の要素を指していることにしよう。

pythonで1文字単位の標準入出力をするときは`sys.stdin.read`, `sys.stdout.write`を使おう。
以下にBFクラスの実装を挙げる。いくつかの機能を未実装に済ませているので、そこは各自で実装してみよう。

```python:bf.py
class BF:
    def __init__(self, sourcecode):
        self.src = sourcecode
        self.reader = 0 #今ソースコードの何文字目を見ているか
        self.memory = [0] * 1000
        self.pointer = 500

    def run(self):
        while self.reader < len(self.src):
            c = self.src[self.reader]
            if c == '>':self.right()
            if c == '<':self.left()
            if c == '+':self.plus()
            if c == '-':self.minus()
            if c == '.':self.dot()
            if c == ',':self.comma()
            if c == '[':self.bra()
            if c == ']':self.cket()
            self.reader += 1

    def right(self):
        self.pointer += 1

    def left(self):
		#自分で実装する
		pass
    
    def plus(self):
        self.memory[self.pointer] += 1
        
    def minus(self):
		#自分で実装する
		pass
    
    def dot(self):
        sys.stdout.write(chr(self.memory[self.pointer]))        
    
    def comma(self):
		#自分で実装する
		pass

    def bra(self):
        if self.memory[self.pointer] != 0:return
        bracket = 1
        while self.reader < len(self.src) and bracket > 0:
            self.reader += 1
            if self.src[self.reader] == '[':
                bracket += 1
            if self.src[self.reader] == ']':
                bracket -= 1
        if bracket != 0:
            print("bracket is broken")
            exit(0)
            
    def cket(self):
		#自分で実装する
		pass
```

以下のBrainF**kのコードはHello Worldを出力するプログラムである。
実行して、インタプリタがしっかり動いているか確かめてみよう。

```text
>+++++++++[<++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.[-]>++++++++[<++++>-]<.>+++++++++++[<+++++>-]<.>++++++++[<+++>-]<.+++.------.--------.[-]>++++++++[<++++>-]<+.[-]++++++++++.
```

もし余力があったら、BrainF**kで入力された数字の和を出力するプログラムなどを作ってみよう。とても難しいことがわかる。


## 構文解析
HQ9+もBrainF**kも大して難しい構文解析は行わなかった。人間が読みやすいプログラミング言語は、多少高度な構文解析を行わなければコード解釈ができない。
構文解析の練習として以下の機能を持つ対話型シェルを作ってみよう。

- 四則演算が処理できる。ただし左から順に計算する優先順位である。括弧には対応していない
- 変数に対応している。
- 数式を1行入力してエンターを押すと、それを計算し、成功すれば結果を出力し、失敗すればエラーを吐く
- `x = 3`というふうに`(変数名) = (値)` とすると変数を宣言したり、値を設定したりできる。

ここで、どのような入力が構文として正しいいのかを示すために、BNFという表記を導入する。これから実装する言語の正当な1行の命令に対応するBNFは以下のようになる。

```
<command> ::= <substitute> | <formula>

<substitute> ::= <variable> '=' <formula>

<formula> ::= 　　<number> '+' <formula>
	      | <number> '*' <formula>
	      | <number> '-' <formula>
	      | <number> '/' <formula>
	      | <number>

<number> ::= <constant> | <variable>

<variable> ::= <alphabet> | <alphabet> <variable>

<alphabet> ::= 'a' | 'b' | .. | 'z'

<constant> ::= <digit> | <digit> <constant>

<digit> ::= '0' | '1' | '2' | .. | '9'

```

BNFの記法は `::=`の左のパターンが右に書いたパターンとマッチするということを定義している。

たとえば最後の一行は、<digit>は'0'や'1'などの一文字の数字にマッチすることを表している。
最後から二行目は<number>は<digit>単体もしくは<digit>のあとに<number>が来るものとマッチすることを表している。
これはつまり<digit>が1つ以上並んだものが<number>であることを表している。

上のBNF記法で書かれた文法の仕様に則って、まずは構文解析器を作ってみよう。

### 構文解析の実装
まずは文字列が与えられた時に、先頭の整数だけ取り出して、残りと分離する関数を実装してみよう。

```python:read_constant.py
DIGITS = "0123456789"
def read_constant(string):
    i = 0
    while i < len(string) and string[i] in DIGITS:
        i += 1
    return int(string[:i]), string[i:]
```
一文字目から順番に見ていって、数字ではなくなるところまで全部取って、整数として読み込みというコードである。

次に`<number>`を処理する関数を実装しよう。`read_number(string)`とすると'string'の先頭から、整数もしくは変数を読み取って、残りと分離する関数である。

```python:read_number.py
def error(message):
    print(message)
    exit(0)

def read_number(string):
    string = string.strip()
    if string == "":error("syntax_error")
    
    if string[0] in DIGITS:
        return read_constant(string)

    if string[0] in ALPHABETS:
        return read_variable(string)

    error("syntax_error")
```

この次は`<formula>`を処理する関数を実装しよう。`read_formula(string)`とすると`string`を式として解釈してその計算結果を返すようにしよう。

```python:read_formula.py
env = {}
def read_formula(string):
    string = string.strip()
    num, rest = read_number(string)
    if type(num) == str:
        if num not in env:error("no such variable {}".format(num))
        num = env[num]
    if rest == "":
        return num
    rest = rest.strip()

    if rest[0] == '+':
        return num + read_formula(rest[1:])
    if rest[0] == '*':
        #自分で実装する
        pass
    if rest[0] == '-':
        #自分で実装する
        pass
    if rest[0] == '/':
        #自分で実装する
        pass
    error("syntax_error")
```

ここで,`env`は連想配列で、将来的には変数名をキーとして、その変数の値を格納するものである。envはenvironment(環境)の略で、現在の変数の状況を管理しているものと考えてもらって良い。

最後に、commandを実装すれば変数を使わず代入もせず足し算しかできないインタプリタが完成するはずだ。

```python:read_command.py
def read_command(string):
    if '=' in string:
        var = read_substitute(string)
        print("set {}".format(var))
    else:
        print(read_formula(string))


while True:
    read_command(input())
```
ここでは'='が含まれていれば代入分で、そうでなければただの式だと判定している。

ここまでのものと、これから実装しなければならないものをまとめると以下のようになる。

```python:syntax.py
DIGITS = "0123456789"
ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
env = {}

def error(message):
    print(message)
    exit(0)


def read_number(string):
    string = string.strip()
    if string == "":error("syntax_error")
    
    if string[0] in DIGITS:
        return read_constant(string)

    if string[0] in ALPHABETS:
        return read_variable(string)

    error("syntax_error")

def read_constant(string):
    i = 0
    while i < len(string) and string[i] in DIGITS:
        i += 1
    return int(string[:i]), string[i:]


def read_variable(string):
    #自分で実装する
    pass

def read_formula(string):
    string = string.strip()
    num, rest = read_number(string)
    if type(num) == str:
        if num not in env:error("no such variable {}".format(num))
        num = env[num]
    if rest == "":
        return num
    rest = rest.strip()

    if rest[0] == '+':
        return num + read_formula(rest[1:])
    if rest[0] == '*':
        #自分で実装する
        pass
    if rest[0] == '-':
        #自分で実装する
        pass
    if rest[0] == '/':
        #自分で実装する
        pass
    error("syntax_error")

def read_substitute(string):
    string.strip()
    var, rest = read_variable(string)
    rest = rest.strip()
    if rest[0] != '=':error("syntax_error")
    env[var] = read_formula(rest[1:])
    return var

def read_command(string):
    if '=' in string:
        var = read_substitute(string)
        print("set {}".format(var))
    else:
        print(read_formula(string))


while True:
    read_command(input())
```

このままでは足し算しかできないので、`#自分で実装する`と書いてある場所を埋めて、変数や他の演算子に対応しているようにしよう。

