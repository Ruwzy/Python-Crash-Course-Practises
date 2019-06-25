class Restaurant():
    ''' build a class call Restaurant'''

    def __init__(self, restaurant_name, cuisine_type):
        '''initial the restaurant's name and the cuisine's type'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        '''print the restaurant's name and the cuisine's type'''
        print("The restaurant's name is " + self.restaurant_name.title() + ".")
        print("\nIt's cuisine's type is " + self.cuisine_type.title() + ".")

    
    def open_restaurant(self):
        '''print the opening info'''
        print(self.restaurant_name.title() + " is now opening.")


    def people_served(self):
        print("The restaurant has served " + str(self.number_served) + " people.")

    
    def set_number_served(self, cus_input):
        self.number_served = cus_input


restaurant = Restaurant("Ruby's Corner", "Thai")

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.people_served()

restaurant.number_served = 5
restaurant.people_served()

restaurant.set_number_served(10)
restaurant.people_served()

