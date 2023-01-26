# 2. Tenemos guardado en un diccionario los códigos morse corespondientes a cada caracter. Escribir un programa que lea una palabra y la muestre usando el código morse.

codigo = {
    'A': '.-',     'B': '-...',    'C': '-.-.',
    'D': '-..',    'E': '.',       'F': '..-.',
    'G': '--.',    'H': '....',    'I': '..',
    'J': '.---',   'K': '-.-',     'L': '.-..',
    'M': '--',     'N': '-.',      'O': '---',
    'P': '.--.',   'Q': '--.-',    'R': '.-.',
    'S': '...',    'T': '-',       'U': '..-',
    'V': '...-',   'W': '.--',     'X': '-..-',
    'Y': '-.--',   'Z': '--..',    '1': '.----',
    '2': '..---',  '3': '...--',   '4': '....-',
    '5': '.....',  '6': '-....',   '7': '--...',
    '8': '---..',  '9': '----.',   '0': '-----',
    '.': '.-.-.-', ',': '--..--',  ':': '---...',
    ';': '-.-.-.', '?': '..--..',  '!': '-.-.--',
    '"': '.-..-.', "'": '.----.',  '+': '.-.-.',
    '-': '-....-', '/': '-..-.',   '=': '-...-',
    '_': '..--.-', '$': '...-..-', '@': '.--.-.',
    '&': '.-...',  '(': '-.--.',   ')': '-.--.-'
}

palabra = input("Palabra: ")
fraseMorse = ""

for clav in codigo:
    for letra in palabra:
        if letra.upper() == clav:
            fraseMorse += codigo[clav] + " "

print(fraseMorse)