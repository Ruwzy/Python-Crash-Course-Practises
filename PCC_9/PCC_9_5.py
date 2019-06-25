class User():
    '''build a class named user'''

    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0


    def describe_user(self):
        '''print the user's info'''
        print("Your first name is: " + self.first_name.title() + ".")
        print("Your last name is: " + self.last_name.title() + ".")
        print("Your age is: " + self.age.title() + ".")
        print("Your gender is: " + self.gender.title() + ".")
  
    
    def greet_user(self):
       '''say hello to the user'''
       print("Hello, " + self.first_name.title() + " " + self.last_name.title() + ", nice to see you here. Hope you have a good time today!")


    def increment_login_attempts(self, add_num):
        self.login_attempts += add_num


    def show_attempts(self):
        print("You have tried " + str(self.login_attempts) + " times.")


    def reset_login_attempts(self):
        self.login_attempts = 0


user_one = User("Ribon", "Woo", "18", "female")
user_one.describe_user()
user_one.greet_user()

user_two = User("Jack", "Jones", "23", "male")
user_two.describe_user()
user_two.greet_user()

user_three = User("Rebecca", "Cai", "98", "female")
user_three.describe_user()
user_three.greet_user()

user_four = User("Tina", "Faye", "56", "female") 
user_four.describe_user()
user_four.greet_user()

user = User("Jack", "Tim", "34", "male")

user.increment_login_attempts(1)
user.increment_login_attempts(1)
user.show_attempts()

user.increment_login_attempts(1)
user.increment_login_attempts(1)

user.show_attempts()
user.reset_login_attempts()
user.show_attempts()
