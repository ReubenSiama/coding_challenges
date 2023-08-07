# Given a string s, return the most frequent character (an alphabet letter) in the string
# string = "abcddefda1111133333"
string = "AA0AB0BB0ccc0aa0aw00wo0BBBw123123"

def countCharacters():
    most = 0
    char = ''
    if len(string) > 100 or len(string) == 0:
        return "Cannto process data"
    for s in string:
        if s.isalpha() and s.islower() and most < string.count(s):
            most = string.count(s)
            char = s
    
    return "Most repeated character is \'{}\', repeated {} times".format(char, most)

print(countCharacters())
