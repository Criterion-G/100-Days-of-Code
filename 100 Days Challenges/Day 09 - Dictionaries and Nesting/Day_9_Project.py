# create a blind auction script

bids = {}

status = True

while status == True:

    name = input('what\'s your name?\n')
    bid = int(input('what\'s your bid?\n'))

    bids[name] = bid

    cont = input('anyone would like to make another bid? y or n\n')

    if cont == 'n':
        status = False

print(bids)
max_valuepair = max(bids.items(), key= lambda k: k[1])
print(f'SOLD! to {max_valuepair[0]}, with the bid of {max_valuepair[1]}! Congrats!')

# turns out it is simplier than I expected, nice!
