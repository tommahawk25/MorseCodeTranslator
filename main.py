alphabet = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "----": "CH",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "-----": "0",
    "..--..": "?",
    "--..--": ",",
    "--...-": "!",
    ".-.-.-": ".",
    ".--.-.": "@",
    "-..-.": "/",
    "-....-": "-",
    "-.--.": "(",
    "-.--.-": ")",
    ".----.": "'",
    ".-..-.": "\""
}
# possible to add more symbols if needed


def translate_to_text():
    try:
        morse_code = input("Enter a morse code: ")
        translation = "Translation: "
        temp_result = ""
        letter = ""
        count = 0
        spaces = morse_code.count(" ")
        backslashes = morse_code.count("//")

        # morse code format 1 (spaces between letters are " " and spaces between words are " / ")
        if spaces > 0 and backslashes == 0:
            for symbol in morse_code:
                # count iterations
                count += 1
                # if symbol is not " " nor "/", then it is another symbol within letter
                if symbol != " " and symbol != "/":
                    temp_result += symbol
                # if symbols " ", "/", " " continue after each other, then it is space between words
                elif symbol == " " and morse_code[count] == "/" and morse_code[count+1] == " ":
                    letter = alphabet.get(temp_result)
                    translation += letter + " "
                    # clear temporary result for another iteration
                    temp_result = ""
                # if symbol is "/", then it is space taken care of in previous iteration
                elif symbol == "/":
                    pass
                # if symbol is " " and previous symbol is "/", then it is space taken care of in previous iteration
                elif symbol == " " and morse_code[count-2] == "/":
                    pass
                # if it is " ", then letter is done and is translated
                else:
                    letter = alphabet.get(temp_result)
                    translation += letter
                    # clear temporary result for another iteration
                    temp_result = ""

        # morse code format 2 (spaces between letters are "/" and spaces between words are "//")
        else:
            for symbol in morse_code:
                # count iterations
                count += 1
                # if symbol is not "/" nor "|", then it is another symbol within letter
                if symbol != "/" and symbol != "|" and symbol:
                    temp_result += symbol
                # if symbol is "/" or "|", then it is space
                else:
                    # we have to find out if it is space between words or letters
                    # if previous symbol is also "/" or "|", then it is space between words
                    if morse_code[count - 2] == "/" or morse_code[count - 2] == "|":
                        translation += " "
                    # if previous symbol is not "/" nor "|", then it is space between letter, letter is translated
                    else:
                        letter = alphabet.get(temp_result)
                        translation += letter
                        # clear temporary result for another iteration
                        temp_result = ""

        # when all loop is done, it is needed to translate last remaining temporary result
        letter = alphabet.get(temp_result)
        translation += letter
        temp_result = ""
        print(translation)
        return translation

    except TypeError:
        print("Incorrect morse code symbols!")
        translate_to_text()


def translate_to_morse():
    try:
        text = input("Enter text: ")
        translation = "Translation: "

        for symbol in text:
            symbol = symbol.upper()
            if symbol != " ":
                translation += list(alphabet.keys())[list(alphabet.values()).index(symbol)] + "/"
            else:
                translation += "//"
        print(translation)
        return translation

    except ValueError:
        print("Incorrect symbols!")
        translate_to_morse()


def user_action():
    action = input("1. Text to Morse Code\n2. Morse Code to text\nType number of action: ")
    if action == "1":
        translate_to_morse()
    elif action == "2":
        translate_to_text()
    else:
        print("Type number 1 or 2!")
        user_action()


user_action()
