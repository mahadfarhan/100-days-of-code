import pandas as pd

df = pd.read_csv("./NATO alphabet/nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (_, row) in df.iterrows()}

user_name = input("Enter your name: ").upper().strip()

while True:
    try:
        user_name_phonetics = [nato_dict[letter] for letter in user_name]
        break
    except KeyError as e:
        user_name = (
            input(f"{e.args[0]!r} is an invalid character. Please enter your name: ")
            .upper()
            .strip()
        )


print(user_name_phonetics)
