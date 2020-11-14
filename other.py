""" 
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of 
pizza toppings until they enter a 'quit' value . As they enter each topping, 
print a message saying you’ll add that topping to their pizza .
"""
prompt = '\n Enter a Pizza topping to add.'
prompt += '\nEnter "quit" to finish : '


active = True

while active:
    topping = input(prompt)
    if topping == "quit":
        active = False
    else:
        print(f'you add {topping} to your pizza.')
