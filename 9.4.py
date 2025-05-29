class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served =0
        

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name}")
        print(f"The type of cuisine is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.name} is open for business")
    def restaurant(self):
        print(f"the number of total customer serverd in a day are :{self.number_served}")
        
    def set_number_served(self,s_number):
        self.number_served = s_number
        
    def increment_number_served(self,in_number):
        self.number_served += in_number
        
        

my_hotel = Restaurant("Joy Bangla","Banglai")
my_hotel.restaurant()
my_hotel.number_served =20
my_hotel.restaurant()
my_hotel.set_number_served(45)
my_hotel.restaurant()
my_hotel.increment_number_served(100)
my_hotel.restaurant()
