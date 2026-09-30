import functions as func

random_password = func.rng_password(int(input('how many letters?\n')),int(input('how many numbers?\n')),int(input('how many symbols?\n')))

print(random_password)
