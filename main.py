alphabet = {
    ".-": "A", "-...": "B", "-.-.": "C",
    "-..": "D", ".": "E", "..-.": "F",
    "--.": "G", "....": "H", "----": "CH",
    "..": "I", ".---": "J", "-.-": "K",
    ".-..": "L", "--": "M", "-.": "N",
    "---": "O", ".--.": "P", "--.-": "Q",
    ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W",
    "-..-": "X", "-.--": "Y", "--..": "Z",
    ".----": "1", "..---": "2", "...--": "3",
    "....-": "4", ".....": "5", "-....": "6",
    "--...": "7", "---..": "8", "----.": "9",
    "-----": "0", "..--..": "?", "--..--": ",",
    "--...-": "!", ".-.-.-": ".", ".--.-.": "@",
    "-..-.": "/", "-....-": "-", "-.--.": "(",
    "-.--.-": ")", ".----.": "'", ".-..-.": "\""
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
        double_slashes = morse_code.count("//")

        # morse code format 1 (spaces between letters are " " and spaces between words are " / ")
        if spaces > 0 and double_slashes == 0:
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
                # if symbol is "/", then it is space and is taken care of in previous iteration
                elif symbol == "/":
                    pass
                # if symbol is " " and previous symbol is "/", then space is taken care of in previous iteration
                elif symbol == " " and morse_code[count-2] == "/":
                    pass
                # if it is " ", then letter is completed and is translated
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
                # if last symbols are "/" or "|" then it is end of sentence
                elif count == len(morse_code) - 1 and (
                                morse_code[len(morse_code) - 2] == "/" or morse_code[len(morse_code) - 2] == "|"):
                    pass
                elif count == len(morse_code) and (
                                morse_code[len(morse_code) - 1] == "/" or morse_code[len(morse_code) - 1] == "|"):
                    pass
                # if symbol is "/" or "|", then it is space
                else:
                    # we have to find out if it is space between words or letters
                    # if previous symbol is also "/" or "|", then it is space between words
                    if morse_code[count - 2] == "/" or morse_code[count - 2] == "|":
                        translation += " "
                    # if previous symbol is not "/" nor "|" then it is space between letters (taken care of already)
                    # and letter is completed and translated
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
                # get key by value in dictionary
                translation += list(alphabet.keys())[list(alphabet.values()).index(symbol)] + "/"
            else:
                translation += "/"
        # end the morse code
        translation += "/"

        print(translation)
        return translation

    except ValueError:
        print("Incorrect symbols!")
        translate_to_morse()


def user_action():
    action = input("1. Text to Morse Code\n2. Morse Code to text\nEnter number of action: ")
    if action == "1":
        translate_to_morse()
    elif action == "2":
        translate_to_text()
    else:
        print("Enter number 1 or 2!")
        user_action()


user_action()
