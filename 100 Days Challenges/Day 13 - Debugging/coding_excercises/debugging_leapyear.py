# consider the following code

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 4000 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# it is appearant that the issue is that the other if statements are nested within the first if statment, so if the first statement's condition is not met, the nested ifs will be ignored compeletly
# also, on line 6, it's 4000 instead of 400
# i've solved this in day 10, so I'll just use my answer there, the fix:

def is_leap(year):
    r_1 = year % 4
    r_2 = year % 100
    r_3 = year % 400

    if r_2 == 0 and r_3 != 0:
        return False
    elif r_1 != 0:
        return False
    else:
        return True
