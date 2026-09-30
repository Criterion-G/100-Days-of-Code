# create a function that determines if a year is a leap year or not
# the function should return boolean values only
# leap == True
# not leap == False
def is_leap_year(year):
    r_1 = year % 4
    r_2 = year % 100
    r_3 = year % 400

    if r_2 == 0 and r_3 != 0:
        return False
    elif r_1 != 0:
        return False
    else:
        return True

# the above is my solution that I came up with after debugg in the lines below
# r_3 is redundant as any year that is divisble by 400 is divisable by 100

def test_leap(year):
    r_1 = year % 4
    r_2 = year % 100
    r_3 = year % 400
    return [r_1, r_2, r_3]

LIST_YEARS = [2000, 2020, 2024, 2400, 1700, 1989, 2100]

for i in LIST_YEARS:
    if sum(test_leap(i)) == 0:
        None
    else:
        print(f'year {i} result: {test_leap(i)}')

for i in LIST_YEARS:
    print(f'result for {i} is {is_leap_year(i)}')

# the hardest part of this challenge was more on the side of math than anything else.
