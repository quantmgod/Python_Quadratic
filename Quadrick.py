import math

def main():
    print ("Enter the coefficients of:")
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    d = b*b-4*a*c

    if d < 0:
        print ("This equation has no real solution")

    if d >= 0:
        x1 = (-1 * b + math.sqrt(d))/(2*a)
        x2 = (-1 * b - math.sqrt(d))/(2*a)
        if d == 0:
            print ("This equation has one solutions for x: ", x1)
        elif d > 0:
            print ("This equation has two solutions for x: ", x1, " and", x2)
    q = input("Do you want to solve another (Y=Yes/N=No)?: ")

    if ((q == "Y") | (q == "y")):
        main()
    else:
        print("Thanks for playing!")
        exit()
main()