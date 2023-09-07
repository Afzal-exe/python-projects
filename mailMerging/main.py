names = open("./Input/Names/invited_names.txt", mode='r+')
template = open("./Input/Letters/starting_letter.txt", mode='r+')
for name in names:
    new = name.strip()
    template = open("./Input/Letters/starting_letter.txt", mode='r+')
    new_temp = template.read().replace('[name]',new)
    newletter = open(f"./Output/ReadyToSend/{new}.txt", mode='w')
    newletter.write(new_temp)
    newletter.close()
    template.close()
names.close()

