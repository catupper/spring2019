from random import randint as rr
def make_input(filename, n, w, maxw):
    with open(filename, "w") as f:
        f.write("{} {}\n".format(n, w))
        for i in range(n):
            f.write("{} {}\n".format(rr(1, 100), rr(1, max(10, maxw))))

            
make_input("knapsack_in1.txt", 20, 100, 25)
make_input("knapsack_in2.txt", 1000, 1000, 50)
make_input("knapsack_in3.txt", 10000, 1000, 50)
