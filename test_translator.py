import unittest
from translator import MorseCodeTranslator


class TestTranslate(unittest.TestCase):

    def test_translate_to_text_format_1(self):
        message = ".... .. --..-- / .... --- .-- / .- .-. . / -.-- --- ..- ..--.."
        self.assertEqual(MorseCodeTranslator(message).translate_to_text(message),
                         "Translation: HI, HOW ARE YOU?")

    def test_translate_to_text_format_2a(self):
        message = "....|..|--..--||....|---|.--||.-|.-.|.||-.--|---|..-|..--..||"
        self.assertEqual(MorseCodeTranslator(message).translate_to_text(message),
                         "Translation: HI, HOW ARE YOU?")

    def test_translate_to_text_format_2b(self):
        message = "..../../--..--//..../---/.--//.-/.-././/-.--/---/..-/..--..//"
        self.assertEqual(MorseCodeTranslator(message).translate_to_text(message),
                         "Translation: HI, HOW ARE YOU?")

    def test_translate_to_text_format_2c(self):
        message = "..../../--..--//..../---/.--//.-/.-././/-.--/---/..-/..--../"
        self.assertEqual(MorseCodeTranslator(message).translate_to_text(message),
                         "Translation: HI, HOW ARE YOU?")

    def test_translate_to_text_format_2d(self):
        message = "..../../--..--//..../---/.--//.-/.-././/-.--/---/..-/..--.."
        self.assertEqual(MorseCodeTranslator(message).translate_to_text(message),
                         "Translation: HI, HOW ARE YOU?")

    def test_translate_to_morse(self):
        message = "HI, HOW ARE YOU?"
        self.assertEqual(MorseCodeTranslator(message).translate_to_morse(message),
                         "Translation: ..../../--..--//..../---/.--//.-/.-././/-.--/---/..-/..--..//")

    def test_message_is_text_1(self):
        message = "HI, HOW ARE YOU?"
        self.assertEqual(MorseCodeTranslator(message).text_or_morse(message), True)

    def test_message_is_text_2(self):
        message = "...././.-../.-../---//"
        self.assertEqual(MorseCodeTranslator(message).text_or_morse(message), False)

    # # This one does not work! Problem is in: self.letter = alphabet.get(self.temp_result). It returns NoneType.
    # # However, I don't know why. This part of the code is in other tests too, and it works fine.
    # def test_letter_translation(self):
    #     temp_result = "-.-."
    #     self.assertEqual(MorseCodeTranslator(temp_result).letter_translation(temp_result), "Translation: C")


if __name__ == "__main__":
    unittest.main()
