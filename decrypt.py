"""
Author: Nicholas Baron (830278807)
Description: This program is a 16bit decrypter with an 8 bit key. It takes 16bits divides it into
2 bytes, a and b. The bytes are then decrypted with the function (a,b) = (b(XOR)key,a).s
"""


def decrypt(key, inString):
    """
    This is the method that handles decryption for specific keys.
    :param key: This is the 8-bit key that is being decrypted.
    :param inString: This is the string that is to be encrypted.
    :return: This is the decrypted string.
    """

    if len(inString) < 1:
        print("[WARNING] String given to decrypt was found to be empty.")
        return inString

    print("[LOG} Decrypt with key: " + chr(key))
    outString = bytearray()
    inString = bytearray(inString)

    for i in range(0, len(inString)-1, 2):
        outString.append(inString[i+1] ^ key)
        outString.append(inString[i])

    if outString[len(outString)-2] == 0x00:
        if outString[len(outString)-1] == 0x02: # Is there a buffer? If so remove it.
            outString = outString[:-2]
        elif outString[len(outString)-1] == 0x03:
            outString = outString[:-3]
    else:
        print("[LOG] Didn't find any part that indicates padding.")

    return outString