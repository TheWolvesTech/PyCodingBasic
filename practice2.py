# No Starch Press - First Practice.
"""
TRY IT YOURSELF
2-4) Name Cases: Store a person’s name in a variable, and then print that per-
son’s name in lowercase, uppercase, and titlecase.

2-5) Famous Quote: Find a quote from a famous person you admire. Print the
quote and the name of its author. Your output should look something like the
following, including the quotation marks:
Albert Einstein once said, “A person who never made a
mistake never tried anything new.”

2-7) Stripping Names: Store a person’s name, and include some whitespace
characters at the beginning and end of the name. Make sure you use each
character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the nformatame using each of the three stripping functions, lstrip(),
rstrip(), and strip().

"""
#2-4
person_name = input("please enter your name : ")  #Store the person name in a varible.
print(person_name.lower())  #printing person name in lowercase, using lower().
print(person_name.upper())  #printing person name in uppercase, using upper().
print(person_name.title())  #printing person name in format title, using title().

#2-5
person_quote = 'Steve Jobs once said, "Your time is limited, so don’t waste it living someone else’s life.""'
print(person_quote)

#2-7
other_name = "     r3izer     "
#cleaning whitespaces.
print(other_name.strip())  #clean the whitespaces
print(other_name.rstrip())
print(other_name.lstrip())
