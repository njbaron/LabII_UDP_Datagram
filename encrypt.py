"""
Author: Nicholas Baron (830278807)
Description: This program is a 16bit encrypter with an 8 bit key. It takes 16bits divides it into
2 bytes, a and b. The bytes are then encrypted with the function (a,b) = (b,a(XOR)key).
"""

def encrypt(keys, inString):
    """

    :param keys:
    :param inString:
    :return:
    """
    for i in range(0, len(keys)):
        inString = encrypt_help(keys[i], inString)
    return inString

def encrypt_help(key, inString):
    """
    This is the basic encryption function. It encrypts for only one key.
    :param key: This is the 8-bit key.
    :param inString: This is the bytes array that is to be encrypted.
    :return: This is the encrypted bytes array.
    """

    if len(inString) < 1:
        print("[WARNING] String given to encrypt was found to be empty.")
        return inString

    print("[LOG} Encrypt with key: " + chr(key))
    outString = bytearray()
    inString = bytearray(inString)

    if len(inString) % 2: # Is the string an even number of bytes? If no add a 3 bytes.
        inString.append(0x00)
        inString.append(0x00)
        inString.append(0x03)
    else:
        inString.append(0x00)
        inString.append(0x02)

    for i in range(0, len(inString)-1, 2):
        outString.append(inString[i+1])
        outString.append(inString[i] ^ key)

    return outString