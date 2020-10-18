# No Starch Press - First Practice.
"""
TRY IT YOURSELF
3-1) Names: Store the names of a few of your friends in a list called names. Print
each person’s name by accessing each element in the list, one at a time.

3-2) Greetings: Start with the list you used in Exercise 3-1, but instead of just
printing each person’s name, print a message to them. The text of each mes-
sage should be the same, but each message should be personalized with the
person’s name.

3-3) Your Own List: Think of your favorite mode of transportation, such as a
motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as “I would like to own a
Honda motorcycle.”


"""
#3-1
friends_list = ['dany','raul','emili','sara','william']  #we are define a list with friend names.
print(friends_list[0].title())  #printing with format.
print(friends_list[1].title())  #printing with format.
print(friends_list[2].title())  #printing with format.
print(friends_list[3].title())  #printing with format.
print(friends_list[4].title())  #printing with format.

#3-2
print(f"Hey {friends_list[0].title()}, how are you today ?")  #personalized message per friends in list.
print(f"Hey {friends_list[1].title()}, how are you today ?")
print(f"Hey {friends_list[2].title()}, how are you today ?")
print(f"Hey {friends_list[3].title()}, how are you today ?")
print(f"Hey {friends_list[4].title()}, how are you today ?")

#3-3
vehiculs_list =['skateboard','plane','car','bycicle']
print(f"I like use my {vehiculs_list[0]} to go to my apartament.")
print(f"I wanna take a {vehiculs_list[1]} to go to New York.")
