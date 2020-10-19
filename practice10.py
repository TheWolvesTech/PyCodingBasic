"""
5-2. More Conditional Tests: You don’t have to limit the number of tests you
create to 10. If you want to try more comparisons, write more tests and add
them to conditional_tests.py. Have at least one True and one False result for
each of the following:

Test whether an item is in a list
Test whether an item is not in a list
Tests using the and keyword and the or keyword
Tests using the lower() function

"""

heroes_list = ['Spiderman','Batman','Flash','Superman','Captain America','Professor X','Falcon']

#Test whether an item is in a list
'''item in list.'''
if("Spiderman" in heroes_list):
    print("Spidy greetings : Hi everyone!!")

#Test whether an item is not in a list
'''item not in list.'''
if("Wonder woman" not in heroes_list):
    print("The warriors never die !!")

#Tests using the and keyword and the or keyword
'''testing keywords'''
if("wonder woman" not in heroes_list and "batman".capitalize() in heroes_list):
    print("We are justice!!")

if("Batman" not in heroes_list or "Flash" in heroes_list):
    print("The faster man alive...")

#Tests using the lower() function
if(heroes_list[0] == "Spiderman"):
    print()
    print("heroes in lowercase : ")
    for heroe in heroes_list:
        print(heroe.lower())
