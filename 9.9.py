class Battery:
    def __init__(self,battery_size=40):
        self.battery_size = battery_size
    def describe_battery(self):
        printf(f"This car has a {self.battery_size}Kw/h battery")
    
    def get_range(self):
        if self.battery_size == 40:
            range = 260
        elif self.battery_size == 65:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65

class car:
    def __init__(self,maker,model,year):
        self.maker=maker
        self.model = model
        self.year = year
        self.odometer = 0
             
        
class Electric_car(car):
    def __init__(self,maker,model,year):
        super().__init__(maker,model,year)
        self.battery = Battery()   
    def describe_battery(self):
        print(f"This car has {self.battery.battery_size} kWh battery.")
        
Khelna_gari = Electric_car("Tasla","Model X",2020)
Khelna_gari.battery.get_range()
Khelna_gari.battery.upgrade_battery()
Khelna_gari.battery.get_range()        
        
    