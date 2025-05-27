# test_morse_translator.py

import unittest
from morse_translator import letters_to_morse, morse_to_letters

class TestMorseTranslator(unittest.TestCase):
    def test_letters_to_morse_basic(self):
        self.assertEqual(letters_to_morse('SOS'), '... --- ...')

    def test_letters_to_morse_with_space(self):
        self.assertEqual(letters_to_morse('HELLO WORLD'), '.... . .-.. .-.. --- / .-- --- .-. .-.. -..')

    def test_morse_to_letters_basic(self):
        self.assertEqual(morse_to_letters('... --- ...'), 'SOS')

    def test_morse_to_letters_with_space(self):
        self.assertEqual(morse_to_letters('.... . .-.. .-.. --- / .-- --- .-. .-.. -..'), 'HELLO WORLD')

    def test_letters_to_morse_unrecognized_characters(self):
        self.assertEqual(letters_to_morse('Hi!'), '.... .. -.-.--')
    def test_morse_to_letters_invalid_morse(self):
        self.assertEqual(morse_to_letters('.... .. .-.-.-.-'), 'HI')

if __name__ == '__main__':
    unittest.main()