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

def process(sourcecode):
    global accumulator
    accumulator = 0
    for c in sourcecode:
        if c == 'H':command_h()
        if c == 'Q':command_q(sourcecode)
        if c == '9':command_9()
        if c == '+':command_plus()
        

def main():
    sourcecode = read_code()
    process(sourcecode)
        
if __name__ == "__main__":
    main()
