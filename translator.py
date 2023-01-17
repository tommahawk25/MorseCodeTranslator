from typing import Dict, Final


class MorseCodeTranslator:
    """Translate Morse code into text and text into Morse code."""

    ALPHABET: Final[Dict[str, str]] = {
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
        ".-..-.": '"',
    }

    def __init__(self, message_input: str):
        self.message_input: str = message_input
        self.translation: str = "Translation: "
        self.morse_type: int = 1

    @classmethod
    def translate(cls, message_input: str) -> str:
        """Translates text into Morse code or Morse code into text."""
        translator: MorseCodeTranslator = cls(message_input)
        translator._translate()
        return translator.translation

    def _translate(self) -> str:
        """
        Decides whether the input message_input is text or Morse code (and which type).
        Runs translation accordingly.
        """
        if self._is_text():
            self._translate_to_morse()
        else:
            if self._morse_type() == 1:
                self._translate_from_morse_type_1()
            elif self._morse_type() == 2:
                self._translate_from_morse_type_2()
            else:
                self._translate_from_morse_type_3()
        return self.translation

    def _is_text(self) -> bool:
        """
        Decides whether the input message_input is text. Returns "True" if yes. Returns "False" if it's a Morse code.
        """
        dots = self.message_input.count(".")
        dashes = self.message_input.count("-")
        slashes = self.message_input.count("/")
        return dots + dashes + slashes <= len(self.message_input) / 2

    def _morse_type(self) -> int:
        """
        Detect a Morse code type:
        1: Words are divided by " / " and symbols are divided by " "
        2: Words are divided by "//" and symbols are divided by "/"
        3: Words are divided by "||" and symbols are divided by "|"
        """
        if " " in self.message_input:
            morse_type = 1
        else:
            if "/" in self.message_input:
                morse_type = 2
            else:
                morse_type = 3
        return morse_type

    def _translate_to_morse(self) -> str:
        """Translated text into Morse code."""
        for char in self.message_input:
            if char == " ":
                self.translation += "/ "
            else:
                self.translation += (list(self.ALPHABET.keys())[list(self.ALPHABET.values()).index(char.upper())]) + " "
        self.translation = self.translation[:-1]
        return self.translation

    def _translate_from_morse_type_1(self) -> str:
        """Translates Morse code (type 1) into text."""
        for word in self.message_input.split(" / "):
            for letter in word.split(" "):
                self.translation += self.ALPHABET.get(letter)
            self.translation += " "
        self.translation = self.translation[:-1]
        return self.translation

    def _translate_from_morse_type_2(self) -> str:
        """Translates Morse code (type 2) into text."""
        for word in self.message_input.split("//"):
            for letter in word.split("/"):
                if letter == "":
                    pass
                else:
                    self.translation += self.ALPHABET.get(letter)
            self.translation += " "
        self.translation = self.translation[:-2]
        return self.translation

    def _translate_from_morse_type_3(self) -> str:
        """Translates Morse code (type 3) into text."""
        for word in self.message_input.split("||"):
            for letter in word.split("|"):
                if letter == "":
                    pass
                else:
                    self.translation += self.ALPHABET.get(letter)
            self.translation += " "
        self.translation = self.translation[:-2]
        return self.translation


if __name__ == "__main__":
    input_message: str = input("Enter message: ")
    result = MorseCodeTranslator.translate(input_message)
    print(result)
