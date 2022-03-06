# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"
# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.

with open("./Input/Names/invited_names.txt") as name_file:
    name_list = name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as data:
    letter_contents = data.read()

for name in name_list:
    stripped_name = name.strip()
    new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

    # Save the letters in the folder "ReadyToSend".
    with open(f"./Output/ReadyToSend/{stripped_name}.txt", mode="w") as data:
        data.write(new_letter)

