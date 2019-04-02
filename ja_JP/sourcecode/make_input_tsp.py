from random import randint as rr
def dist(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

def make_input(filename, n, maxx=800):
    points = set()
    while len(points) < n:
        points.add((rr(0,maxx), rr(0,maxx)))
    points = list(points)

    with open(filename, "w") as f:
        f.write("{}\n".format(n))
        for i in range(n):
            for j in range(n):
                f.write("{} ".format(dist(points[i], points[j])))
            f.write("\n")

#make_input("tsp_input1.txt", 10, 10)
#make_input("tsp_input2.txt", 20)
#make_input("tsp_input3.txt", 50)

def make_euclide_input(filename, n):
    points = set()
    while len(points) < n:
        points.add((rr(50,750), rr(50,550)))
    points = list(points)

    with open(filename, "w") as f:
        f.write("{}\n".format(n))
        for i in range(n):
            for j in range(n):
                f.write("{} ".format(dist(points[i], points[j])))
            f.write("\n")

    with open("point_" + filename, "w") as f:
        for i in range(n):
            f.write("{} {}\n".format(points[i][0], points[i][1]))

make_euclide_input("euclid_input1.txt", 10)
make_euclide_input("euclid_input2.txt", 20)
make_euclide_input("euclid_input3.txt", 50)
make_euclide_input("euclid_input4.txt", 100)
