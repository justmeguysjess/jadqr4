import pytest 

def submission_type(x):
    if(submission == 3):
        print("Submission File Type Not Allowed")
        return
    if(submission == 4):
        print("Submission File Type Not Allowed")
        return
    else:
        print("Successfully Submitted Assignment")
        return

def set_type(extension):
    if(extension == ".txt"):
        x = 1
        return x
    if(extension == ".jpg"):
        x = 2
        return x
    if(extension == ".gif"):
        x = 3
        return x
    if(extension == ".jif"):
        x = 4
        return x

print ("File type of extension" + x + " has been uploaded")
