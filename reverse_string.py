string = input("Enter a string:")
# string = '!ab#d^sg*'

def reverseString(text):
    alphabet_strings = getAllAlphabetsFromString(text)
    reversed_string = ''

    for i in range(len(text)):
        if not text[i].isalpha():
            reversed_string += text[i]
        else:
            reversed_string += alphabet_strings[-1]
            alphabet_strings = alphabet_strings[:-1]

    return reversed_string

def getAllAlphabetsFromString(text):
    alphabet_strings = '';
    for char in text:
            if char.isalpha():
                alphabet_strings += char
    return alphabet_strings

print(string)
print(reverseString(string))
