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

    ##created a method to automate the new owner command.

    def change_owner(self, new_owner):
        self.owner = new_owner

#### Step 2 once completed, create varible with instance attibutes:

jeep = Vehicle('CT252', 'Compass', 'Tim')


# The following below were used to used the validity of the "Jeep" variable

# print("Jeep")
# print(Jeep.model_type)
# print(Jeep.owner)
# print(Jeep.reg_num)

print(f" Welcome to the state BMV {jeep.owner}, you are the current owner of a Jeep {jeep.model_type} with a registration number {jeep.reg_num}.")

d()

print(f" Welcome back {jeep.owner}, we recieved a change of owner request for vehicle under registration tag # {jeep.reg_num}.......status will be updated in 5 days.")

#### Step 3 process an owner change from tim --> tom

d()
d()

print(f" ** 5 days later **")
print(f"{jeep.owner}, your request has been approved.")

## pulling in the method from above to change the owner.

jeep.change_owner("Tom")

#following below were used to test out new owner was processed:

# print(Jeep.owner)

d()

print(f"{jeep.owner}, you are now the new owner of the Jeep {jeep.model_type} under tag number {jeep.reg_num}....Thank you")

