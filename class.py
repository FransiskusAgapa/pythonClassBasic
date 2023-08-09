import math

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
print("\n= 1st Student =")
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
print("\nThird Student")
print(student_three.fname)
print(student_three.lname)
print(student_three.gender)
print(student_three.age)
print(student_three.major)
print(student_three.gpa)

# restaurant order
class Order:
    def __init__(self, food, spice_level, price, quantity):
        self.food = food
        self.spice_level = spice_level #  1- 5 - 5 being the spiciest
        self.price = price
        self.quantity = quantity

first_order = Order("Vietnamese Pho", 5,12.50,1)
second_order = Order("Spice Waala",3,10.99,2)
third_order = Order("Korean BBQ",4,13.10,3)

print("\n= 1st Food Order =")
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

class Shoe:
    def __init__(self, brand, price, quantity, in_stock):
        self.brand = brand
        self.price = price 
        self.quantity = quantity
        self.in_stock = in_stock

    def price_n_quantity(self):
        self.price = self.price * self.quantity
    
    #on-sale price reduction
    def on_sale_by_percentage(self,percentage):
        self.price = math.trunc(self.price * ( 1 - percentage))

    # price tax
    def add_tax(self, tax):
        return math.trunc(tax + self.price)

tax_value = 6
print("\n= 1st Shoe Order =")
shoe_one = Shoe("Nike",55.10,2,True)
print(f"Brand: {shoe_one.brand}")
print(f"Price per pairs: ${shoe_one.price}")
shoe_one.price_n_quantity() # call this method/function to update price based on quantity
print(f"Price for {shoe_one.quantity} pairs: ${shoe_one.price}")
shoe_one.on_sale_by_percentage(0.2) # call this method/function to update price based on sale percentage
print(f"Price after {0.2 * 100}% sale: ${shoe_one.price}")
print(f"Price before tax: ${shoe_one.price}")
print(f"Price Total (plus tax ${tax_value}): tax: ${shoe_one.add_tax(tax_value)}")
