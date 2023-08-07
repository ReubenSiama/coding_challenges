number = 1234
base = 10
current_value = number
converted = 0
range1 = 2 ** 31 * -1
range2 = range1 * -1 -1

if number < 0:
    current_value *=  -1

while not current_value == 0:
    iterator = current_value % base
    current_value = int(current_value / base)
    multiply = converted * 10
    converted = multiply + iterator
    if(converted <= range1 ):
        converted = 0
    if(converted >= range2):
        converted = 0

if number < 0:
    converted *=  -1

print(number)
print(converted)
