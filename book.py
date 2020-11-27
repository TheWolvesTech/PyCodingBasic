"""
10-4. Guest Book: Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.
"""

#Entry point
if __name__ == "__main__":
    file_name = "guest_book.txt"
    access = True
    prompt = '\n Enter guest name.'
    prompt += '\nEnter "quit" to finish : '
    while access:
        name = input(prompt).lower()
        if name == "quit":
            print("closing program.")
            access = False
        else:
            with open(file_name, "a") as file_object:
                print("Thank you for coming," + name.title())
                file_object.write(str(name).title() + "\n")
