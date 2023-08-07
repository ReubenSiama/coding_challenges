# Longest Substring Without Repeating Characters
# string = "abcabcdbb"
# string = 'bbbbb'
string = 'pwwkew'
count = 0
substring = ''
stringArray = []
arr = []

for s in string:
    if s in stringArray:
        arr.append(stringArray)
        stringArray = []

    stringArray.append(s)

arr.append(stringArray)

for a in arr:
    if count < len(a):
        substring = ''
        count = len(a)
        for s in a:
            substring += s

print("Longest substring without repeating characters is: ", substring)
print("Length of the substring is: ", count)
