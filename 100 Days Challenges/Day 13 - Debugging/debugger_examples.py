import random
import debugger_module as math_func

# use case 1
def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3) # we can step into the code of functions from other libraries by changing the json config 'JustMyCode' to false
        new_item = math_func.add(new_item, item)
        b_list.append(new_item) # the bug was that this line was not indented, making it append one item after the loop has been completed
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])

# to run a debugger in must IDEs I think, is that you have to create a breakpoint for the debugger to start on, then run the debugger.
