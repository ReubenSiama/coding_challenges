def encrypt(text):
    encryptedString = ''
    for char in text:
        if char.isspace():
           encryptedString += char
        else:
            temp = ord(char) + 3
            encryptedString += chr(temp)
    return encryptedString

def decrypt(text):
    decryptedString = '';
    for char in text:
        if char.isspace():
            decryptedString += char
        else:
            temp = ord(char) - 3
            decryptedString += chr(temp)
    return decryptedString

myString = input("Enter a string to encrypt: ")
encrypted = encrypt(myString)

print("Your string: ", myString)
print("Encrypted: ", encrypted)
print("Decrypted: ", decrypt(encrypted))
