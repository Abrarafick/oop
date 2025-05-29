class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name}")
        print(f"The type of cuisine is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.name} is open for business")

class iceCreamStand(Restaurant):
    def __init__(self,name,cuisine_type,flavors):
        super().__init__(name, cuisine_type)
        self.flavors =flavors 
        
    def display_flavors(self):
        print(f"Available flavors at {self.name}:")
        for flavor in self.flavors:
            print(f" * {flavor}")


my_shop = iceCreamStand("Wow", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry"])


my_shop.display_flavors()
    



        
    
    
    