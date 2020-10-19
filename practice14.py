"""
info refresh :
pop : delete the last item.
remove : delete by index value.
del : you can use to delete all items in the list.

5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
not empty.

If the list is empty, print the message We need to find some users!

Remove all of the usernames from we are deleting all usersyour list, and make sure the correct
message is printed.
"""
#5-9
user_names = ['admin','carlos','juan','jose','ana','lisa']  #list definition

if(user_names is []):
    print("We need to find some users.")

else:
    del(user_names[:])
    print("username database was delete.")
