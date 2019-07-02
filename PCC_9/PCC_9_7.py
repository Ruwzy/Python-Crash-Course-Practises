class User():
    '''build a class named user'''

    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender


    def describe_user(self):
        '''print the user's info'''
        print("Your first name is: " + self.first_name.title() + ".")
        print("Your last name is: " + self.last_name.title() + ".")
        print("Your age is: " + self.age.title() + ".")
        print("Your gender is: " + self.gender.title() + ".")
  
    
    def greet_user(self):
       '''say hello to the user'''
       print("Hello, " + self.first_name.title() + " " + self.last_name.title() + ", nice to see you here. Hope you have a good time today!")


class Admin(User):

    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.user_privileges = []

    def show_privileges(self):
        print("The admin's privileges are: ")
        for user_privilege in self.user_privileges:
            print("-" + user_privilege.title())

first_admin = Admin("Roger", "Tim", "44", "male")
first_admin.describe_user()
first_admin.greet_user()
first_admin.user_privileges = ["can add post", "can delete post", "can ban user"]
first_admin.show_privileges()

