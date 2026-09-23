# class Product:
#     count = 0
#     def __init__(self,name,price):
#         self.Name = name
#         self.Price = price
#         Product.count += 1
    
#     def get_info(self):
#         print(f"price of {self.Name} is {self.Price}")
#     @classmethod
#     def get_count(cls):
#         print(f"total products are {cls.count}")
#     @staticmethod
#     def calculate_discount(total_price,percentage):
#         print(f"discounted_price = {total_price - (total_price * percentage / 100)}") 
   

# p1 = Product("iphone","12000")
# p2 = Product("iphone","12000")
# p3 = Product("iphone","12000")
# p4 = Product("iphone","12000")
# p5 = Product("iphone","12000")
# p6 = Product("iphone","12000")
# p1.get_info()
# Product.get_count()
# p1.calculate_discount(p1.Price,12)


# Q1
# class BankAccount:
#     def __init__(self,account_number,owner_name,balnace):
#         self.account_number = account_number
#         self.owner_name = owner_name
#         self.balance = balance

#     def deposit(self,deposit):
#         self.balance += deposit
    
#     def  withdraw(self,balance):
#         self.balance -= balance 
    
#     def check_balance(self):
#         print("current balance : ",self.balance)


# Q3
# class student:
#     def __init__(self,name,roll_no,marks):
#         self.__name = name
#         self.__roll_no = roll_no
#         self.__marks = marks

#     def get_name(self):
#         print(self.__name)
#     def set_name(self,name):
#         if name == "":
#             print("enter valid name")
#             return
#         self.__name = name
#     def get_name(self):
#         return self.__name

#     def set_roll_no(self,roll_no):
#         if roll_no < 1 or roll_no > 100:
#             print("wrong roll no ")
#             return
#         self.__roll_no
    
#     def set_marks(self,mark):
#         if mark < 0:
#             self.__marks = mark
#         self.__marks = mark
   
# s1 = student("Ali",12,90)
# s1.set_name("Majid")
# s1.set_roll_no(111)
# print(s1.get_name())


# Q5
# class Vehicles:
#     def __init__(self,brand , model):
#         self.brand = brand
#         self.model = model


# class car(Vehicles):
#     def __init__(self,seat,brand,model):
#         super().__init__(brand,model)
#         self.seats = seats

# class bike(Vehicles):
#     def __init__(self,engine,brand,model):
#         super().__init__(brand,model)
#         self.engine = engine
# b1 = bike("V8","honda",2026)
# print(b1.engine,b1.model,b1.brand)


# Q6
# import abc from ABC,abstractmethod
# class employee(ABC):
#     @abstractmethod
#     def cal_salary(self):
#         pass



# # Q8
# class Player:
#     count = 0
#     def __init__(self,name,level):
#         self.name = name
#         self.level = level
#         Player.count +=1

# s1 = Player("majid",1)
# s2 = Player("majid",1)
# print(Player.count)


# Q9

# class herbivoce:
#     def __init__(self):
#         print("i am herbivoce")

# class carnivoce:
#     def __init__(self):
#         print("i am carnivoce")
        
# class Omnivoce:
#     def __init__(self):
#         print("i am omniivoce")

# class Bear(herbivoce,carnivoce,Omnivoce):
#     def __init__(self):
#         super().__init__()
#         carnivoce.__init__(self)
#         Omnivoce.__init__(self)
#         print("i am bear")

# b1 = Bear()


# Q10







