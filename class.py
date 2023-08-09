import math

# Students
print("\n== Students ==\n")
class student:
    def __init__(self):
        self.fname = "No-First-Name-Specified"
        self.lname = "No-Last-Name-Specified"
        self.gender = "No-Gender-Specified"
        self.age = 99 # default no age value specified
        self.major = "No-Major-Specified"
        self.gpa = 1.0 # default no gpa value specified

# add first student 
first_student = student()
first_student.fname = "Abby"
first_student.lname = "Anny"
first_student.gender = "Female"
first_student.age = 20
first_student.gpa = 3.5
print("= 1st Student =")
print(first_student.fname)
print(first_student.lname)
print(first_student.gender)
print(first_student.age)
print(first_student.major)
print(first_student.gpa)

# add second student
student_two = student()
student_two.fname = "Adam"
student_two.lname = "Angel"
student_two.age = 21
student_two.major = "Sociology"
student_two.gpa = 3.0
print("\n = 2nd Student =")
print(student_two.fname)
print(student_two.lname)
print(student_two.gender)
print(student_two.age)
print(student_two.major)
print(student_two.gpa)


# add third student
student_three = student()
student_three.fname = "Luka"
student_three.lname = "Djon"
student_three.age = 19
student_three.major = "Criminology"
student_three.gpa = 3.5
print("\n3rd Student")
print(student_three.fname)
print(student_three.lname)
print(student_three.gender)
print(student_three.age)
print(student_three.major)
print(student_three.gpa)

# Restaurant Order
print("\n== Restaurant Order ==\n")
class Order:
    def __init__(self, food, spice_level, price, quantity):
        self.food = food
        self.spice_level = spice_level #  1- 5 - 5 being the spiciest
        self.price = price
        self.quantity = quantity

first_order = Order("Vietnamese Pho", 5,12.50,1)
second_order = Order("Spice Waala",3,10.99,2)
third_order = Order("Korean BBQ",4,13.10,3)

print("= 1st Food Order =")
print(f"Food : {first_order.food}")
print(f"Spice Level: {first_order.spice_level}")
print(f"Price: {first_order.price}")
print(f"Quantity: {first_order.quantity}")

print("\n= 2nd Food Order =")
print(f"Food : {second_order.food}")
print(f"Spice Level: {second_order.spice_level}")
print(f"Price: {second_order.price}")
print(f"Quantity: {second_order.quantity}")

print("\n= 3rd Food Order =")
print(f"Food : {third_order.food}")
print(f"Spice Level: {third_order.spice_level}")
print(f"Price: {third_order.price}")
print(f"Quantity: {third_order.quantity}")


# Shoe Store
print("\n== Shoe Store ==\n")
class Shoe:
    def __init__(self, brand, price, quantity, in_stock):
        self.brand = brand
        self.price = price 
        self.quantity = quantity
        self.in_stock = in_stock

    # update price based on quantity
    def price_n_quantity(self):
        self.price = self.price * self.quantity
    
    #on-sale price reduction
    def on_sale_by_percentage(self,percentage):
        self.price = math.trunc(self.price * ( 1 - percentage)) # math.trunc(num) - throws away reminder to 2 number after comma

    # price tax
    def add_tax(self, tax):
        return math.trunc(tax + self.price)

# ex: change 0.1 to 10% for display purpose
def convert_to_percentage(sale_val = 0):
    return sale_val * 100

# 1st shoes
tax_value = 6
sale_percentage = 0.2
print("= 1st Shoe Order =")
shoe_one = Shoe("Nike",55.10,2,True)
print(f"Brand: {shoe_one.brand}")
print(f"Price per pairs: ${shoe_one.price}")
shoe_one.price_n_quantity() # call this method/function to update price based on quantity
print(f"Price for {shoe_one.quantity} pairs: ${shoe_one.price}")
shoe_one.on_sale_by_percentage(sale_percentage) # call this method/function to update price based on sale percentage
print(f"Price after {convert_to_percentage(sale_percentage)}% sale: ${shoe_one.price}")
print(f"Price Total (after tax ${tax_value}): ${shoe_one.add_tax(tax_value)}")

# 2nd shoes
tax_value = 4
sale_percentage = 0.1
print("\n= 2nd Shoe Order =")
shoe_two = Shoe("Vans",50.40, 3, True)
print(f"Brand: {shoe_two.brand}")
print(f"Price per pairs: ${shoe_two.price}")
shoe_two.price_n_quantity() # update price
print(f"Price for {shoe_two.quantity} pairs: ${shoe_two.price}")
shoe_two.on_sale_by_percentage(sale_percentage) # update price with sale percentage
print(f"Price after {convert_to_percentage(sale_percentage)}% sale: ${shoe_two.price}")
print(f"Price Total (after tax ${tax_value}): ${shoe_two.add_tax(tax_value)}")

# 3rd shoes
tax_value = 8
sale_percentage = 0.3
print("\n= 3rd Shoe Order =")
shoe_three = Shoe("Adidas",80.59,4,True)
print(f"Brand: {shoe_three.brand}")
print(f"Price per pairs: ${shoe_three.price}")
shoe_three.price_n_quantity() # update price
print(f"Price for {shoe_three.quantity} pairs: ${shoe_three.price}")
shoe_three.on_sale_by_percentage(sale_percentage) # update price with sale percentage
print(f"Price after {convert_to_percentage(sale_percentage)}% sale: ${shoe_three.price}")
print(f"Price Total (after tax ${tax_value}): ${shoe_three.add_tax(tax_value)}")


print("\n== Summer Camp ==\n")
# Summer Camp
class SummerCamper:
    def __init__(self,fname,lname,role,school_status):
        self.fname = fname
        self.lname = lname
        self.role = role # participant or mentor
        self.school_status= school_status # freshman, sophomore, etc 
        self.registered = False # default value whether somebody is registered
        self.num_absence_permit = 0 # number of absence participants get to skip class/activity

    # display campers information
    def display_info(self):
        print("\n")
        print(f"First name: {self.fname}")
        print(f"Last name: {self.lname}")
        print(f"Role: {self.role}")
        print(f"Number absence permit: {self.num_absence_permit}")
        print(f"School status: {self.school_status}")
        print("\n")
        return self
    
    # enroll participants before camp
    def enroll(self):
        if(self.registered):
            print(f"{self.fname} is already enrolled!")
        else:
            self.registered = True
            print(f"{self.fname} is just enrolled!")
            self.num_absence_permit = 3
        return self
    
    # permission to skip class based on number of absence permit
    def skip_class(self):
        if(self.num_absence_permit <= 0):
            print(f"{self.fname}, You may not skip class!")
        else:
            self.num_absence_permit -= 1
            print(f"{self.fname}, You may take the day off! (absence permit: {self.num_absence_permit})")
        return self

# 1st campers
camper_one = SummerCamper("Ally","Abby","Mentor","Senior")
camper_one.display_info().enroll().display_info().skip_class() # this is chaining method

# 2nd campers
camper_two = SummerCamper("Benny","Bulls","Mentor","Senior")
camper_two.display_info().enroll().display_info().skip_class().skip_class()

# 3rd campers
camper_three = SummerCamper("Celina","Zion","Mentor","Senior")
camper_three.display_info().enroll().display_info().skip_class().skip_class().skip_class()

# 4th campers
camper_four = SummerCamper("Dan","Russ","Participants", "Freshman")
camper_four.display_info().enroll().display_info().skip_class().skip_class()

# 5th campers
camper_five = SummerCamper("Lady","Bun","Participant","Sophomore")
camper_five.display_info().enroll().display_info().skip_class().skip_class().skip_class()

# 6th campers
camper_six = SummerCamper("Lina","Pedro","Participant","Sophomore")
camper_six.display_info().enroll().display_info().skip_class().skip_class()

# Bank Account
print("\n= Bank Account =\n")
class Bank:
    num_of_account = 0
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        Bank.num_of_account += 1
    
    def display_account(self):
        print(f"Name: {self.name}\nBalance: ${self.balance}\n")
        return self

    def deposit(self,amount):
        self.balance += amount
        print(f"${amount} is deposited to {self.name}'s account!\n")
        return self
    
    def withdraw(self,amount):
        if(self.balance > amount):
            self.balance -= amount
            print(f"${amount} is withdrawn from {self.name}'s account!\n")
        else:
            print(f"Withdraw ${amount} from {self.name}'s account canceled - Insufficient Balance!\n")
        return self
    
    @classmethod
    def sum_of_account(cls):
        print(f"{cls.num_of_account} account/s registered")
    
    @staticmethod
    def is_millionaire(balance):
        if(balance > 100000):
            print("\nYou are a millionaire!!")
        else:
            print("\nYou are not a millionaire yet!")
        
# create new accounts   
account_one = Bank("Lenny",100000)
account_two = Bank("Buddy",50000)
account_three = Bank("Angel",200000)

# display account info
account_one.display_account()
account_two.display_account()
account_three.display_account()

# deposit
account_one.deposit(50000)
account_two.deposit(70000)
account_three.deposit(80000)

# withdraw
account_one.withdraw(9000)
account_three.withdraw(10000)
account_three.withdraw(200000)

# call a classmethod - number of account
Bank.sum_of_account()

# call a staticmethod
account_one.is_millionaire(account_one.balance)
account_two.is_millionaire(account_two.balance)
account_three.is_millionaire(account_three.balance)
