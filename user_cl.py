"""
9-3. Users: Make a class called User. Create two attributes called first_name 
and last_name, and then create several other attributes that are typically stored 
in a user profile. Make a method called describe_user() that prints a summary 
of the user’s information. Make another method called greet_user() that prints 
a personalized greeting to the user.
"""


class User():

    def __init__(self, first_name, last_name, age):
        """Initialize name, last name and age attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # METHODS
    def description(self):
        print("User personal information.")
        print("Name : " + " "+self.first_name.title())
        print("Last Name : "+" "+self.last_name.title())
        print("Age : "+" " + str(self.age))

    def greet_user(self):
        print("Welcome again,"+""+ self.last_name + " " + self.first_name + ".")


# Entry point
if __name__ == "__main__":
    quantity = int(input("Quantity of user : "))
    i = 0
    while i < quantity:
        f_name = input("Enter your name : ")
        l_name = input("Enter your last name : ")
        age = int(input("Enter your age : "))
        test_user = User(f_name, l_name, age)  # create an instance maybe.
        test_user.description()
        test_user.greet_user()
        i += 1
