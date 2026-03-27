# This line of code tells the Python interpreter that it needs to 
# reference the post.py file in order to run the rest of the code 
# in this file.
from post import Post

# How will you save the posts you will create? Review the for loop 
# near the end of this code for an answer.
all_posts_archive = []

# What is the user name they want to use?
username = input("What is your Account Name? ")

# Welcome user to the program 
print("Welcome " + username + " to the social media app!")

# Store initial user input in a variable identified by user_input
# You may need to use this statement again to complete the activity.
user_input = input(""" What would you like to do?
"add" - Add a post to the archive
"remove" - Remove a post from the archive
"change user" - Change the user name associated with any future posts
"print" - Display the current up to date list of all posts
"quit" - End the program

""")

# This while loop ensures that the program will continue executing 
# statements at the next indentation level until the user types "quit" 
# in response to the prompt.
while user_input != "quit":
    if user_input == "change user":
        username = input("What would you like to change your username to? ")
    elif user_input == "add":
        pass
    elif user_input == "remove":
        pass
    elif user_input == "print":
        pass
    else:
        pass

    # code for adding a post here
    # code for removing a post here
    # code for changing the current user here
    # code to display all posts, you can use the code in comments below
    """
	# this for loop will print the list
	# and the element itself
    for post in all_posts_archive: 
        print (post)
    """
    # code to inform the user that their input was not valid here
    
    # code that will allow the user to make a new selection
    user_input = input(""" What would you like to do?
"add" - Add a post to the archive
"remove" - Remove a post from the archive
"change user" - Change the user name associated with any future posts
"print" - Display the current up to date list of all posts
"quit" - End the program

""")







message = input("What would you like to post? ")
post4 = Post(username, message)
print(post4)

message = input("Would you like to edit your post? (yes/no) ")
if message == "yes":
    new_message = input("What would you like to change your post to? ")
    post4.set_message(new_message)
    print(post4)
    if message == "no":
        print("Okay, have a nice day!")


message = input("Would you like to see your post history? (yes/no) ")
if message == "yes":
    print("Here is your post history:")
    for post in all_posts_archive:
        print(post)
    if message == "no":
        print("Okay, have a nice day!")
       
message = input("Would you like to quit the program? (yes/no) ")
if message == "yes":
    print("Goodbye!")
    if message == "no":
        print("Okay, have a nice day!")
while (username != "quit"):
    username = input("What is your Account Name? ")
    print("Welcome " + username + " to the social media app!")

    message = input("What would you like to post? ")
    post = Post(username, message)
    all_posts_archive.append(post)
    print(post)