# Create a bill claculator that calculates the bill with the tip choice and how many people are splitting a bill.
# This is my solution
bill = float(input('Your total bill is: '))
tip = float(input('What percentage would you like to tip? '))
split = int(input('For how many people would you like to split this bill? '))
paytotal = bill * (1 + (tip/100)) / split
print(f'each person should pay: {round(paytotal, 2)}')

# I have an idea to create the script which promts the user to choose from a predefined list of tips instead of manual input
# Hint, it involves functions and loops.
# Maybe I'll attempt that when I'm ready

# Result = I did it with 7 lines of code. The instructor did it with 10. My code is effcient, but as mentioned above, it could be better.