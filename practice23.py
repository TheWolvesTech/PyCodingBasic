"""
8-2. Favorite Book: Write a function called favorite_book() that accepts one 
parameter, title . The function should print a message, such as One of my 
favorite books is Alice in Wonderland . Call the function, making sure to 
include a book title as an argument in the function call .
"""


def favorite_book(mybook):
    # great books
    print(f"One of my favorite books is {mybook}. ")


if __name__ == "__main__":
    access = True
    prompt = '\n Enter your favorite book.'
    prompt += '\nEnter "quit" to finish : '
    while access:
        title = input(prompt)
        if title == "quit":
            print("closing program.")
            access = False
        else:
            favorite_book(title)
