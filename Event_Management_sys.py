
###Question 2

# Task 2: Event Management System Enhancement


# Problem Statement: Use the existing Event class by adding an attribute to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.
# Code Example: Basic Event class without participant tracking.


#Step 1 Create a Class Attribute with a builtin instances that can be customize.

from helper import d


class Event():

    def __init__(self, names, date, member_list): # have the "names" be a list to populate names.
        self.names = names
        self.date = date
        self.member_list = member_list

# Step 2 Create a varible to the Class create and customize instances within:

ballroom_1 = Event(["Jim", "Tim", "Tom"], "Aug0824", "member_list")

# The following was used test the instance attribute, verfiy it was creating the correct output.
    # print(ballroom_1)
        # print(ballroom_1.names)
            # print(len(ballroom_1.names))
d()

print(f"Welcome to Rogers Event Management system.") 
print(f"Tonight event which is taking on {ballroom_1.date} will have an estimate guest count of {len(ballroom_1.names)}.")
print(f"The Guest list contains {ballroom_1.names}.")

d()
###Step 3: Adding additonal guests.

print(f"Request to add additonal guests to {ballroom_1.date} event was recieved.")

# names = ["Jim", "Tim", "Tom"]

ballroom_1.names.append("Jill")
ballroom_1.names.append("Will")
ballroom_1.names.append("Tonya")
ballroom_1.names.append("Jessica")
ballroom_1.names.append("Fiona")

#The following was used the verify the names were added correctly:
    #print(ballroom_1.names)
d()
d()

print(f"Request has been approved, Please be advised your guestlist now contains the following names: ")
print(F"   {ballroom_1.names}")


### step 4: Implementing a count system to count the number of guests.

ballroom_1.member_list = len(ballroom_1.names)

#The following was used the verify the names were counted correctly:
    #print(ballroom_1.member_list)

print(f"   Updating your guest count to a total of {len(ballroom_1.names)} guests.")