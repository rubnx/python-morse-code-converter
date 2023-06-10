import pandas as pd

df = pd.read_csv("MorseCodeEdited.csv")

letters = df.LETTER.to_list()
code = df.CODE.to_list()


def text_to_morse():
    submited_text = input("Write some text to turn into Morse Code: ").upper()
    print(submited_text)

    coded_text = ""
    for letter in submited_text:
        if letter in letters:
            index = letters.index(letter)
            morse_code = code[index]
        elif letter == " ":
            morse_code = ""
        else:
            morse_code = letter
        coded_text += morse_code + " "

    print(f"Your text in Morse code is:\n{coded_text}")


def morse_to_text():
    submited_code = input("Input your Morse code to turn into text: ").split(" ")

    submited_code = [" " if x == "" else x for x in submited_code]

    decoded_text = []

    for symbol in submited_code:
        if symbol in code:
            index = code.index(symbol)
            plain_text = letters[index]
        else:
            plain_text = symbol
        decoded_text += plain_text

    decoded_string = ""
    for letter in decoded_text:
        decoded_string += letter

    print(f"Your text in Morse code is:\n{decoded_string}")


conversion_on = True

while conversion_on:
    type_of_conversion = input(
        "What you do want to do? Type 'code' to turn text into Morse or 'decode' to turn Morse into text: "
    )
    if type_of_conversion == "code":
        text_to_morse()
        conversion_on = False
    elif type_of_conversion == "decode":
        morse_to_text()
        conversion_on = False
    else:
        print("Try with 'code' or 'decode'")
