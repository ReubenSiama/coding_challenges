# Given a string s, return the most frequent character (an alphabet letter) in the string
# string = "abcddefda1111133333"
string = "AA0AB0BB0ccc0aa0aw00wo0BBBw123123"

def countCharacters():
    characters = []
    char_count = []
    most = 0
    char = ''
    if len(string) > 100 or len(string) == 0:
        return "Cannto process data"
    for s in string:
        if not s in characters and s.isalpha() and s.islower():
            characters.append(s)

    for a in range(len(characters)):
        count = 0
        stri = ''
        for s in string:
            if characters[a] == s:
                stri += s
        char_count.append(stri)

    for count in char_count:
        if most < len(count):
            most = len(count)
            char = count[-1]

    result = "Most repeated character is \'{}\', repeated {} times"
    return result.format(char, most)

print(countCharacters())
