"""
TRY IT YOURSELF.
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.

"""
#6-2 Dicctionary
favorite_numbers = {
'taylor'  : '31',
'alisson' : '3',
'luther'  : '1',
'ben'     : '6',
'diego'   : '2'
}
print("Friends favorite numbers.")
print(f"Taylor's favorite number is : {favorite_numbers['taylor']}")
print(f"Alisson's favorite number is : {favorite_numbers['alisson']}")
print(f"Luther's favorite number is : {favorite_numbers['luther']}")
print(f"Ben's favorite number is : {favorite_numbers['ben']}")
print(f"Diego's favorite number is : {favorite_numbers['diego']}")
print()
#Extra coding
favorite_languages = {
'Ana'   : 'python',
'Walter': 'ruby',
'Maria' : 'cobol'
}
print("Extra coding.")
print("Favorite languages.")
for name, language in favorite_languages.items():
    if(language=="cobol"):
        print("Language :" + language.upper()+"\n")
    else:
        print("Language :" + language.title()+"\n")
        print("Name : "  + name.title())
