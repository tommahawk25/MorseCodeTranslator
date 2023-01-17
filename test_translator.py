import unittest
from translator import MorseCodeTranslator


class TestTranslate(unittest.TestCase):

    def test_translate_from_morse_type_1(self):
        message = ".... .. --..-- / .... --- .-- / .- .-. . / -.-- --- ..- ..--.."
        self.assertEqual(
            MorseCodeTranslator(message)._translate_from_morse_type_1(),
            "Translation: HI, HOW ARE YOU?"
        )

    def test_translate_from_morse_type_2(self):
        message = "..../../--..--//..../---/.--//.-/.-././/-.--/---/..-/..--..//"
        self.assertEqual(
            MorseCodeTranslator(message)._translate_from_morse_type_2(),
            "Translation: HI, HOW ARE YOU?"
        )

    def test_translate_from_morse_type_3(self):
        message = "....|..|--..--||....|---|.--||.-|.-.|.||-.--|---|..-|..--..||"
        self.assertEqual(
            MorseCodeTranslator(message)._translate_from_morse_type_3(),
            "Translation: HI, HOW ARE YOU?"
        )

    def test_translate_to_morse(self):
        message = "HI, HOW ARE YOU?"
        self.assertEqual(
            MorseCodeTranslator(message)._translate_to_morse(),
            "Translation: .... .. --..-- / .... --- .-- / .- .-. . / -.-- --- ..- ..--.."
        )

    def test_detect_morse_type_1(self):
        message = ".... . .-.. .-.. --- / .--- --- .... -."
        self.assertEqual(MorseCodeTranslator(message)._morse_type(), 1)

    def test_detect_morse_type_2(self):
        message = "...././.-../.-../---//.---/---/..../-.//"
        self.assertEqual(MorseCodeTranslator(message)._morse_type(), 2)

    def test_detect_morse_type_3(self):
        message = "....|.|.-..|.-..|---||.---|---|....|-.||"
        self.assertEqual(MorseCodeTranslator(message)._morse_type(), 3)


if __name__ == "__main__":
    unittest.main()
