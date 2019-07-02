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


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_icecream_flavor(self):
        print("The icecream's flavor is: ")
        for flavor in self.flavors:
            print("-" + flavor.title())


my_icecream = IceCreamStand("Ruby's Corner", "Thai")
my_icecream.flavors = ["vanilla", "chocolate", "berry"]
my_icecream.describe_restaurant()
my_icecream.show_icecream_flavor()