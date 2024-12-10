# Add a display_timeline(self) method to the class that prints the user's name along with a list of posts. 
# Number the list items. Then write a program that creates a user 'johndoe'. 
# Add the following posts. Print the user's name and posts.

#Hello, world!
#Had a great day at the park!
#What's up, Natalie? How are you?

class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

def display_timeline():
    sm1 = SocialMediaProfile("johndoe")
    user = sm1.username
    print(user)
    post1 = sm1.add_post("Hello, world!")
    post2 = sm1.add_post("Had a great day at the park!")
    post3 = sm1.add_post("What's up, Natalie? How are you?")


if __name__ == "__main__":
    display_timeline()



