
###Question 2

# Task 2: Event Management System Enhancement


# Problem Statement: Use the existing Event class by adding an attribute to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.
# Code Example: Basic Event class without participant tracking.


#Step 1 Create a Class Attribute with a builtin instances that can be customize.

from helper import d


class Event():

    def __init__(self, event_name, date, participant_list): # have the "names" be a list to populate names.
        self.event_names = event_name
        self.date = date
        self.participant_list = participant_list
    
    ### added the add_participant method
    def add_participant(self, new_participant):
        self.participant_list.append(new_participant)
    
    #getter 
    ####added a method to count participant in the list.

    def get_participant_count(self ):
        return len(self.participant_list)
            

# Step 2 Create a varible to the Class create and customize instances within:

ballroom_1 = Event("Gala", "Aug0824", ["Jim", "Tim", "Tom"])

# The following was used test the instance attribute, verfiy it was creating the correct output.
# print(ballroom_1)
    # print(ballroom_1.participant_list)
        # print(ballroom_1.get_participant_count())

d()

print(f"Welcome to Rogers Event Management system.") 
print(f"Tonight event which is taking on {ballroom_1.date} will have an estimate guest count of {ballroom_1.get_participant_count}.")
print(f"The Guest list contains {ballroom_1.participant_list}.")

d()
###Step 3: Adding additonal guests.

print(f"Request to add additonal guests to {ballroom_1.date} event was recieved.")

ballroom_1.add_participant("Jill")
ballroom_1.add_participant("Will")
ballroom_1.add_participant("Tonya")
ballroom_1.add_participant("Jessica")
ballroom_1.add_participant("Fiona")


# The following was used the verify the names were added correctly:
    #print(ballroom_1.participant_list)

d()
d()

print(f"Request has been approved, Please be advised your guestlist now contains the following names: ")
print(F"{ballroom_1.participant_list}")


# ### step 4: Implementing a count system to count the number of guests.


# #The following was used the verify the names were counted correctly:
    # print(ballroom_1.get_participant_count())


print(f"Updating your guest count to a total of {ballroom_1.get_participant_count()} guests.")