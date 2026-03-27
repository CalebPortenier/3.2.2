from post import Post

all_posts_archive = []

post1 = Post("Marie", "this is my first post")
print(post1)
post2 = Post("Nathan", "im a yoshi")
print(post2)
post3 = Post("Hunter", "crunckle uncle")
print(post3)

username = input("What is your Account Name? ")
print("Welcome " + username + " to the social media app!")

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

message = input("Would you like to change your username? (yes/no) ")
if message == "yes":
    new_username = input("What would you like to change your username to? ")
    post4.user_name = new_username
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