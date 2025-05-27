class user:
    def __init__(self,first_name,last_name,batch,age):
        self.first_name = first_name
        self.last_name = last_name
        self.batch=batch
        self.age =age 
        self.login_attemps = 0
        
    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Batch: {self.batch}")
        print(f"Age: {self.age}")
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")
        print(f"i Have came to know that you are a student of batch {self.batch}")
        print(f"I have also informed that you are {self.age} years old")
    
    


Hooman1=user("Saad","Abrar",242,21)
Hooman1.describe_user()
Hooman1.greet_user()

print(f"Now print yourself afer")

for x in range (3):
    a=input()
    b=input()
    c=int(input())
    d=int(input())
    Hooman2=user(a,b,c,d)
    print(f"Print info for the number {x+1} person")
    Hooman2.describe_user()
    Hooman2.greet_user()
    
