from typing import Dict


alphabet: Dict[str, str] = {
    ".-": "A",   "-...": "B",   "-.-.": "C",
    "-..": "D",   ".": "E",   "..-.":   "F",
    "--.": "G",   "....": "H",   "----":   "CH",
    "..": "I",   ".---": "J",   "-.-": "K",
    ".-..": "L",   "--": "M",   "-.": "N",
    "---": "O",   ".--.": "P",   "--.-": "Q",
    ".-.": "R",   "...": "S",   "-": "T",
    "..-": "U",   "...-": "V",   ".--": "W",
    "-..-": "X",   "-.--": "Y",   "--..": "Z",
    ".----": "1",   "..---": "2",   "...--": "3",
    "....-": "4",   ".....": "5",   "-....": "6",
    "--...": "7",   "---..": "8",   "----.": "9",
    "-----": "0",   "..--..": "?",   "--..--": ",",
    "--...-": "!",   ".-.-.-": ".",   ".--.-.": "@",
    "-..-.": "/",   "-....-": "-",   "-.--.": "(",
    "-.--.-": ")",   ".----.": "'",   ".-..-.": "\""
}


class MorseCodeTranslator:

    def __init__(self, message: str):
        self.message: str = message
        self.translation: str = "Translation: "
        self.temp_result: str = ""
        self.letter: str = ""

    # Gets a part of Morse code and converts it into a letter.
    def letter_translation(self, temp_result: str) -> str:
        self.temp_result = temp_result
        self.letter = alphabet.get(temp_result)
        self.translation += self.letter
        # Clear temporary result for another iteration.
        self.temp_result = ""
        return self.translation

    # Decides whether the input message is text or Morse code and runs the translation accordingly.
    # For testing purposes I added boolean variable.
    def text_or_morse(self, message: str) -> bool:
        self.message = message
        dots = message.count(".")
        dashes = message.count("-")
        slashes = message.count("/")
        if dots + dashes + slashes >= len(message) / 2:
            is_text = False
            self.translate_to_text(message)
        else:
            is_text = True
            self.translate_to_morse(message)
        return is_text

    # Translate Morse Code into text.
    # Every iteration it tests if symbol is part of a space or part of a letter.
    def translate_to_text(self, message: str) -> str:
        try:
            self.message = message
            count: int = 0
            spaces: int = message.count(" ")
            double_slashes: int = message.count("//")

            # Morse code format 1 (spaces between letters are " " and spaces between words are " / ")
            if spaces > 0 and double_slashes == 0:
                for symbol in message:
                    count += 1
                    # If symbol is part of a letter, it adds this symbol to current symbols expressing that letter.
                    if symbol != " " and symbol != "/":
                        self.temp_result += symbol
                    # Tests if " " is space between words.
                    # If so, it translates current symbols from previous iterations into a letter and adds a space.
                    elif symbol == " " and message[count] == "/" and message[count+1] == " ":
                        self.letter_translation(self.temp_result)
                        self.translation += " "
                    # Symbol is part of space between words from previous iterations and was already taken care of.
                    elif symbol == "/" or (symbol == " " and message[count-2] == "/"):
                        pass
                    # Symbols forming a letter are completed and translated into that letter.
                    else:
                        self.letter_translation(self.temp_result)

            # Morse code format 2 (spaces between letters are "/" and spaces between words are "//")
            else:
                for symbol in message:
                    count += 1
                    # If symbol is part of a letter, it adds this symbol to current symbols expressing that letter.
                    if symbol != "/" and symbol != "|" and symbol:
                        self.temp_result += symbol
                    # If last symbols are "/" or "|" then it is end of message.
                    elif count == len(message) - 1 and (
                            message[len(message) - 2] == "/" or message[len(message) - 2] == "|"):
                        pass
                    elif count == len(message) and (
                            message[len(message) - 1] == "/" or message[len(message) - 1] == "|"):
                        pass
                    # Other cases are spaces ("/").
                    # We have to find out if it is space between words or letters:
                    else:
                        # If previous symbol is also "/" or "|", then it is space between words
                        if message[count - 2] == "/" or message[count - 2] == "|":
                            self.translation += " "
                        # Other cases it is space between letters. Current letter is completed and translated.
                        else:
                            self.letter_translation(self.temp_result)

            # When loop is finished, we also need to finish translation of letter.
            self.letter_translation(self.temp_result)
            print(self.translation)
            return self.translation

        except TypeError:
            print("Incorrect symbols!")

    # Translates text into Morse code.
    def translate_to_morse(self, message: str) -> str:
        try:
            self.message = message
            for symbol in message:
                symbol: str = symbol.upper()
                if symbol != " ":
                    # Gets a key by value in dictionary.
                    self.translation += list(alphabet.keys())[list(alphabet.values()).index(symbol)] + "/"
                else:
                    self.translation += "/"
            # End the morse code.
            self.translation += "/"

            print(self.translation)
            return self.translation

        except ValueError:
            print("Incorrect symbols!")


if __name__ == "__main__":
    input_message: str = input("Enter a message: ")
    MorseCodeTranslator(input_message).text_or_morse(input_message)
