#convert given integer to roman numerals
def divide(num, div):
    num = int(num / div)
    match div:
        case 1000:
            return "M" * num
        case 100:
            if num < 4 and num > 0:
                return "C" * num
            elif num == 5:
                return "D"
            elif num > 4 and num < 9:
                return "D" * (num - 5)
            elif num == 4:
                return "CD"
            else:
                return "CM"
        case 10:
            if num < 4 and num > 0:
                return "X" * num
            elif num == 5:
                return "L"
            elif num > 4 and num < 9:
                return "L" * num
            elif num == 4:
                return "XL"
            else:
                return "XC"
        case 1:
            if num < 4 and num > 0:
                return "I" * num
            elif num > 4 and num < 9:
                return "V" + "I" * (num - 5)
            elif num == 4:
                return "IV"
            elif num == 9:
                return "IX"

def getMod(num, div):
    return num % div

def convert(num):
    number = num
    converted = ""
    iterator = True
    while iterator == True:
        if(number > 3999):
            iterator = False
            print("Number too large")
        elif number >= 1000:
            converted += divide(number, 1000)
            number = getMod(number, 1000)
        elif number >=100 and number <1000:
            converted += divide(number, 100)
            number = getMod(number, 100)
        elif number >=10 and number <100:
            converted += divide(number, 10)
            number = getMod(number, 10)
        elif number <= 10 and number > 0:
            converted += divide(number, 1)
            number = getMod(number, 1)
        else:
            iterator = False
    return converted

number = input("Enter a number to convert: ")
converted = convert(int(number))
print(converted)
