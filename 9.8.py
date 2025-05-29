class user:
    def __init__(self,first_name,last_name,batch,age):
        self.first_name = first_name
        self.last_name = last_name
        self.batch=batch
        self.age =age 
        self.login_attemps = 0

class admin(user):
    def __init__(self,first_name,last_name,batch,age,privilages):
        super().__init__(first_name,last_name,batch,age)
        self.privilages =privilages
    
    def show_previlages(self):
        for x in self.privilages :
            print(f"{self.first_name} {self.last_name} {x}")
            
class privilages(admin):
    def __init__(self,first_name,last_name,batch,age,privilages):
        super().__init__(first_name,last_name,batch,age,privilages)
        
    def show_previlages(self):
        for x in self.privilages:
            print(f"{self.first_name} {x}")
            
admin2 = privilages("Md Saad","Abrar",242,25,["can add post","can delet post","can ban user"])
admin2.show_previlages()