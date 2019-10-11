import pytest 

def late_submission(time):
    if(time > 23.59):
        print("Assignment was not submitted on time")
        flag = false 
    else:
        print("You have submitted the assignment, congrats!")
        flag = true

