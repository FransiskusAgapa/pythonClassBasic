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

print("\n= 1st Food Order =")
print(f"Food : {first_order.food}")
print(f"Spice Level: {first_order.spice_level}")
print(f"Price: {first_order.price}")
print(f"Quantity: {first_order.quantity}")