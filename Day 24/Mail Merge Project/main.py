with open("./Mail Merge Project/Input/Names/invited_names.txt") as names:
    list_of_names = names.read().splitlines()
    with open("./Mail Merge Project/Input/Letters/starting_letter.txt") as letter:
        letter_template = letter.read()
        for name in list_of_names:
            with open(
                f"./Mail Merge Project/Output/ReadyToSend/{name}.txt", "w"
            ) as letter_to_send:
                letter_to_send.write(letter_template.replace("[name]", name))
