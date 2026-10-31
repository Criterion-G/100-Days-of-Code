with open(r'100 Days Challenges\Day 24 - High Score and Mail Merging\project - Mail Merge\names.txt', 'r') as names:
    names_list = []
    for name in names:
        names_list.append(name.rstrip()) # removes the \n from the names

for name in names_list:
    file_path = f'100 Days Challenges\\Day 24 - High Score and Mail Merging\\project - Mail Merge\\ready_letters\\letter_to_{name}.txt'

    with open('100 Days Challenges\\Day 24 - High Score and Mail Merging\\project - Mail Merge\\template_letter.txt', 'r') as template:
        new_letter = template.read()
        new_letter = new_letter.replace('{name}', name)

    with open(file_path, 'w') as letter:
        letter.write(new_letter)
