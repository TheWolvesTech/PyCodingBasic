"""
TRY IT YOURSELF

3-8. Seeing the World: Think of at least five places in the world you’d like to
visit.
Store the locations in a list. Make sure the list is not in alphabetical order.

"""
good_places = sorted(['new zealand','canada','japon','usa','america'])  #Using sorted() --> temporaly sort()
print(good_places)
good_places.sort()  #Using sort() --> permanently sort.
print(good_places)
good_places2 = ['NY','UK','Germany']
for good_place in good_places2:
    print(good_place.title())
