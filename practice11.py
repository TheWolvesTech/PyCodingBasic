"""
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

Write an if statement to test whether the alien’s color is green. If it is, print
a message that the player just earned 5 points.

Write one version of this program that passes the if test and another that
fails.

"""
#5-3
alien_quantity = int(input("enter a quantity of alien : "))  #definition with input
i = int(0)   #iteration control
while(i<alien_quantity):
    alien_color = input("enter a color : ")
    if(alien_color == 'green'):
        print("player earned 5 points")  #if way
        i+=1
    else:
        print("player earned 0 points")  #else way
        i+=1
