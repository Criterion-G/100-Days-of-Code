import string as st

# challenge one
# create a function that title cases the input

def name_format(f_name: str, l_name: str):
    f_formatted = st.capwords(f_name)
    l_formatted = st.capwords(l_name)
    return f'{f_formatted} {l_formatted}' # return is the end of the function
    print('whatever') # < this line of could is essentially useless

# when thinking about the function with an output, once the function is called it will run its code
# then it will take the return statement and under the hood, the line that called the function will
# replace essentially be replaced with whatever is in the return statemnet

output = name_format('FAisaL','AlOTAIBI') # this line of code will be replaced with the functions output

# a key way to visualize this with code is to take the output of a function and pass it as a parameter
# for another function.. Observe:

def greet(name):
    return f'hello {name}, have a wonderful life!'

print(greet(output))

# functions with multiple return values

def name_format_2(f_name: str, l_name: str):
    if f_name == '' or l_name == '':
        return None                             # the first return value, will exist the code if condition is met.
    f_formatted = st.capwords(f_name)
    l_formatted = st.capwords(l_name)
    return f'{f_formatted} {l_formatted}'

# you can store a function within a variable and call the function by the variable name, the key is not to assign the function to the variable with the paranthesis.

my_fav_func = greet

my_fav_func('Faisal')  ### This is the variable itself assinged the functionlities of it's assigned function
