# morse_translator.py
# 📡 R2-D2's Secret Morse Translator

MORSE_CODE_DICT = {
    'A': '.-',     'B': '-...',   'C': '-.-.',
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.',  ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.',  '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'
}

# Invert the dictionary to decode Morse to letters
MORSE_TO_LETTERS = {v: k for k, v in MORSE_CODE_DICT.items()}


def letters_to_morse(text):
    """Converts plain text to Morse code."""
    text = text.upper()
    morse_code = []
    for char in text:
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append('')  # Unrecognized characters become blanks
    return ' '.join(morse_code)

def morse_to_letters(code):
    """Converts Morse code to plain text."""
    words = code.split(' / ')
    decoded = []
    for word in words:
        letters = word.split()
        decoded_word = ''.join(MORSE_TO_LETTERS.get(char, '') for char in letters)
        decoded.append(decoded_word)
    return ' '.join(decoded)


def run_cli():
    """Command Line Interface for R2-D2's Morse Translator."""
    print("🔊 Welcome to R2-D2's Morse Translator 🔊")
    while True:
        print("\nChoose an option:")
        print("1. Encode text to Morse code")
        print("2. Decode Morse code to text")
        print("3. Exit")
        
        choice = input("👉 Your choice (1/2/3): ").strip()
        
        if choice == '1':
            text = input("📤 Enter text to encode: ")
            print("🔐 Morse Code:")
            print(letters_to_morse(text))
        elif choice == '2':
            code = input("📥 Enter Morse code to decode (use / for spaces): ")
            print("💬 Decoded Text:")
            print(morse_to_letters(code))
        elif choice == '3':
            print("👋 Goodbye, Padawan!")
            break
        else:
            print("🚫 Invalid choice. Try again.")
