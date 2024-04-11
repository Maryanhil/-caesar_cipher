def encrypt(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)

    return result

def decrypt(text, shift):
    return encrypt(text, 26 - shift)

# Test the code
text = "Marianne"
shift = 3
print("Text: " + text)
print("Shift: " + str(shift))
print("Cipher: " + encrypt(text, shift))

cipher = encrypt(text, shift)
print("Decrypted: " + decrypt(cipher, shift))                                                        