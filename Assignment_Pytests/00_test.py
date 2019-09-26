def count_username(username):
    counter = username.count()
    return counter

def min_char_test(counter):
    if(counter<=8):
        print("Username does not meet correct character count")
        tryagain = min_char_test(counter)
    else:
        return counter

    print ("Username is " + counter + " characters")
