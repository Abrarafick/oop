class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name}")
        print(f"The type of cuisine is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.name} is open for business")



Restora = Restaurant("Surma Hotel", "Chiness")
print(f"The name of the restaurant is {Restora.name}")
print(f"The type of Restaurant is {Restora.cuisine_type}")

Restora.describe_restaurant()
Restora.open_restaurant()

# Exercise 9.2
restaurant1 = Restaurant("Cafe_Longe", "Cafe")
restaurant2 = Restaurant("Jomuna Hotel", "Bangladeshi")
restaurant3 = Restaurant("Bela_Poch", "Italian")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
