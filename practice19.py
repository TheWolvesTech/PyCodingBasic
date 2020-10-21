"""
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings
should automatically be included in the output.

"""

glossary = {
'data type' : 'A category of data.',

'expression' : 'Code with an operador surrounded by two operands.',

'integer' : 'An object with a data type int. its value is a whole number.',

'keyword' : 'A word with a special meaning in python.',

'operator' : 'Symbols used with operands in an expression.',

'programming' : 'Writting instructions for a computer to execute.',

'syntax' : 'The set of rules,principles,and processes that govern the structure of sentences.'
}
print("Glossary.")
for word, meaning in glossary.items():
    print("word : " + word.title())
    print("meaning : "+ meaning)
    print()
