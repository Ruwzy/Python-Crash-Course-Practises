class Restaurant():
    ''' build a class call Restaurant'''

    def __init__(self, restaurant_name, cuisine_type):
        '''initial the restaurant's name and the cuisine's type'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        '''print the restaurant's name and the cuisine's type'''
        print("The restaurant's name is " + self.restaurant_name.title() + ".")
        print("It's cuisine's type is " + self.cuisine_type.title() + ".\n")

    
    def open_restaurant(self):
        '''print the opening info'''
        print(self.restaurant_name.title() + " is now opening.")

restaurant_one = Restaurant("Hope", "Sichuan")
restaurant_one.describe_restaurant()

restaurant_two = Restaurant("Tilan", "india")
restaurant_two.describe_restaurant()

restaurant_three = Restaurant("Happy Sushi", "Japanese")
restaurant_three.describe_restaurant()