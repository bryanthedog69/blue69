class  car:
     def __init__(self, name,brand,color,price,speed,engine_type,year):
         self.name = name
         self.brand = brand
         self.color = color
         self.price = price
         self.speed = speed
         self.engine_type = engine_type
         self.year = year
         
     def get_name(self):    
         return self.name
     
     def get_brand(self):
         return self.brand
     
     def get_color(self):
         return self.color
     
     def get_speed(self):
         return self.speed
     
     def get_engine_type(self):
         return self.engine_type
     
     def get_year(self):
         return self.year
     
     def change_name(self, name):
         self.name = name
         return self.name 
     def change_brand(self, brand):
         self.brand = brand
         return self.brand
     def change_color(self, color):
         self.color = color
         return self.color
     def change_price(self,price):
         self.price = price
         return self.price
     def change_speed(self, speed):
         self.speed = speed
         return self.speed
     def change_engine_type(self, engine_type):
         self.engine_type = engine_type
         return self.engine_type
     def change_year(self,year):
         self.year = year
         return self.year
     
     def __str__(self):
        return f"name: {self.name} brand: {self.brand} color: {self.color} price: {self.price} speed: {self.speed} engine_type {self.engine_type} year {self.year}"
car1 = car(name="toyota", brand="camry", color="blue", price=750, speed="280kph", engine_type=1.6, year=2004 )
print(car1.change_brand("corolla"))
print(car1)
#print(car1.get_brand())
