"""
Try It Yourse lf
4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.

Use a for loop to print each food the restaurant offers.

The restaurant changes its menu, replacing two of the items with different
foods. Add a block of code that rewrites the tuple, and then use a for
loop to print each of the items on the revised menu.

"""

#4-13
print("Main Menu")
basic_foods = ('Pancakes','Hamburger','Pan Sauce','Omelets','Scrambled Eggs')  #tuple definition
for food in basic_foods:
    print(food)
basic_foods = ('Pizza','Hamburger','Pan Sauce','Cheese Burguer','Scrambled Eggs')  #re definition tuple
print("New Menu")
for rfood in basic_foods:
    print(rfood)
