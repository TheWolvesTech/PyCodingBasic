"""
5-5. Alien Colors #3: Turn your if- else chain from Exercise 5-4 into an if- elif-
else chain.
If the alien is green, print a message that the player earned 5 points.
If the alien is yellow, print a message that the player earned 10 points.
If the alien is red, print a message that the player earned 15 points.
Write three versions of this program, making sure each message is printed
for the appropriate color alien.

"""
#5-5
alien_quantity = int(input("enter a quantity of alien : "))  #definition with input
i = int(0)   #iteration control
while(i<alien_quantity):
    alien_color = input("enter a color : ")
    if(alien_color == 'green'):
        print("player earned 5 points")  #if way
        i+=1
    elif(alien_color=='yellow'):
        print("player earned 10 points")  #other new way
        i+=1
    elif(alien_color=='red'):
        print("player earned 15 points")  #other new way
        i+=1
    else:
        print("player earned 0 points")  #else way
        i+=1
