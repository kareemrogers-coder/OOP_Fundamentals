#####Question 1

#####City Infrastructure Management System


#####Objective: The aim of this assignment is to apply the concepts of Object-Oriented Programming in Python to build a simulated City Infrastructure Management System. This system will incorporate classes, objects, methods, and data structures to manage different aspects of a city, such as buildings, traffic, and events.


# Task 1: Vehicle Registration System


# Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.
# Code Example: Provide a basic structure for the Vehicle class without methods.

from helper import d

# step 1 is to create a class Attributes with built in intances that can be modify:

class Vehicle():
    def __init__(self, reg_num, model_type,owner):
        self.reg_num = reg_num
        self.model_type = model_type
        self.owner = owner

#### Step 2 once completed, create varible with instance attibutes:

Jeep = Vehicle('CT252', 'Compass', 'Tim')

# The following below were used to used the validity of the "Jeep" variable

# print("Jeep")
# print(Jeep.model_type)
# print(Jeep.owner)
# print(Jeep.reg_num)

print(f" Welcome to the state BMV {Jeep.owner}, you are the current owner of a Jeep {Jeep.model_type} with a registration number {Jeep.reg_num}.")

d()

print(f" Welcome back {Jeep.owner}, we recieved a change of owner request for vehicle under registration tag # {Jeep.reg_num}.......status will be updated in 5 days.")

#### Step 3 process an owner change from tim --> tom

d()
d()

print(f" ** 5 days later **")

print(f"{Jeep.owner}, your request has been approved.")

old_owner = "Tim"
updated_owner = ("Tim")
Jeep.owner = updated_owner.replace("Tim", "Tom")

#following below were used to test out new owener was processed:

# print(new_owner)

# print(Jeep.owner)

d()
print(f"{old_owner}, your Jeep {Jeep.model_type} has been transfer the new owner {Jeep.owner}, as requested tag number {Jeep.reg_num} will remain the same....Thank you")

