"""
basic coding.
4-10. Slices: Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:

Print the message, The first three items in the list are:. Then use a slice to
print the first three items from that program’s list.

Print the message, Three items from the middle of the list are:. Use a slice
to print three items from the middle of the list.

Print the message, The last three items in the list are:. Use a slice to print
the last three items in the list.

4-12. More Loops: All versions of foods.py in this section have avoided using
for loops when printing to save space. Choose a version of foods.py, and
write two for loops to print each list of foods.

"""

#4-10
weapons_list = ['sword','shield','arrow','bow','spear','dagger','axe']
print(f'original list : {weapons_list}')
print(f'the first three items in the list are : {weapons_list[0:3]}')
print(f'middle items : {weapons_list[3:5]}')
print(f'the last three items in thes list are : {weapons_list[4:7]}')

#4-12
foods = ['Meat','Chicken','Cheese','Beans','Sausage']
other_foods = ['Pizza','Rice','Eggs','Hot Dog']
print("Food list with two loop : ")
#first loop:
for food in foods:
    print(food)
#second loop:    
for other_food in other_foods:
    print(other_food)
