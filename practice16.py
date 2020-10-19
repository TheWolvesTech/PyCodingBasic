"""
5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.

Store the numbers 1 through 9 in a list.

Loop through the list.

Use an if- elif- else chain inside the loop to print the proper ordinal end-
ing for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
7th 8th 9th", and each result should be on a separate line.

"""

numbers_list = [1,2,3,4,5,6,7,8,9]
print("Ordinal numbers : ")
for number in numbers_list:
    if(number == 1 or number == 2 or number == 3):
        print(f"{number}st")
    elif(number == 4 or number == 5 or number == 6 or number == 7 or number == 8 or number == 9):
        print(f"{number}th")
