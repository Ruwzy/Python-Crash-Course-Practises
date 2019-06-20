class Restaurant():
    ''' build a class call Restaurant'''

    def __init__(self, restaurant_name, cuisine_type):
        '''initial the restaurant's name and the cuisine's type'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        '''print the restaurant's name and the cuisine's type'''
        print("The restaurant's name is " + self.restaurant_name.title() + ".")
        print("\nIt's cuisine's type is " + self.cuisine_type.title() + ".")

    
    def open_restaurant(self):
        '''print the opening info'''
        print(self.restaurant_name.title() + " is now opening.")


restaurant = Restaurant("Ruby's Corner", "Thai")

print("The restaurant's name is " + restaurant.restaurant_name.title() + ".")
print("\nIt's cuisine's type is " + restaurant.cuisine_type.title() + ".")

restaurant.describe_restaurant()
restaurant.open_restaurant()