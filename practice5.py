"""
3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.

3-5. Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.

3-6. Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a
bigger dinner table.
Use insert() to add one new guest to the beginning of your list.
Use insert() to add one new guest to the middle of your list.
Use append() to add one new guest to the end of your list.
"""
guest_list = ['Emili','Grex','Andreina']  #Guest list

print(f'{guest_list[0].title()}, you are an amazing friend.')
print(f'{guest_list[1].title()}. I love how lovely you are.')
print(f'{guest_list[2].title()}. I want to see you again someday.')

guest_list[2] = 'Ana'

print(f'now {guest_list[2].title()}. Is your new guest.')

guest_list.insert(3,'Dan')
guest_list.insert(4,'Rebecca')
guest_list.insert(5,'Nina')
print("upgrade list of guest")
print(guest_list)
mid = len(guest_list)/2
guest_list.insert(int(mid),'Stella')
print(guest_list)
guest_list.append('Gal')
print(guest_list)
