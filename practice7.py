"""
3-10. Every Function: Think of something you could store in a list. For example,
you could make a list of mountains, rivers, countries, cities, languages, or any-
thing else you’d like. Write a program that creates a list containing these items
and then uses each function introduced in this chapter at least once.

"""
#3-10
good_countries = ['New Zealand','Japon','Germany','UK']
print("Original list : ",good_countries)
print("Sorted list temp :", sorted(good_countries))
good_countries.reverse()
print("Reversed list : ", good_countries)
print(len(good_countries))
test = good_countries[:]
print("Copy list : ",test)
test.pop(1)
print("Using pop to delete an item : " ,test)
test.append("Canada")
print("add a new element with append",test)
