"""
TRY IT YOURSELF
Make a function that
Calculate distance between two points.
"""
import math


def dist(x1, x2, y1, y2):
    d1 = (x2-x1)**2
    d2 = (y2-y1)**2
    d = math.sqrt(d1 + d2)
    return d

#entryPoint
if __name__ == '__main__':
    access = True
    prompt = '\nPress Enter.'
    prompt += '\nEnter "quit" to finish : '
    while True:
        exit = input(prompt).title().strip()
        if(exit == "Quit"):
            break
        else:
            try:
                n1 = float(input("enter value x1 : "))
                n2 = float(input("enter value y1 : "))
                n3 = float(input("enter value x2 : "))
                n4 = float(input("enter value y2 : "))
                print("Distance between p1(x1,y1) and p2(x2,y2) : ", dist(n1, n2, n3, n4))
            except:
                print("Invalid Value.")
