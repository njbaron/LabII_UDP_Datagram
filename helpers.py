


def getKeys(keyFileName, numberKeys = 8):
    """
    This functions retrieves keys from a file.
    :param keyFileName: This is the filename that is supposed to contain the keys.
    :param numberKeys: This is the number of keys that are being requested for encryption.
    :return: This is a bytes array that contains the keys.
    """
    keys = read(keyFileName)

    if len(keys) > numberKeys:
        print("[WARNING] Found more than " + str(numberKeys) + " keys.")
        print("[NOTICE] Using " + str(numberKeys) + " keys.")
    elif len(keys) < numberKeys:
        print("[WARNING] Found less than " + str(numberKeys) + " keys.")
        print("[NOTICE] Using " + str(len(keys)) + " keys.")
    elif len(keys) == 0:
        print("[ERROR] Key file found to be empty. Cannot continue.")
        exit(1)

    return keys[:numberKeys]


def read(file):
    """
    This functions reads bytes arrays from the fiven file.
    :param file: This is the file that is to be read from.
    :return: This is the bytes array containing all the information from the file.
    """

    print("[LOG] Reading file: " + file)
    f = open(file, "rb") #read bytes
    retStr = f.read()
    f.close()
    return retStr


def write(file, string):
    """
    This functions writes bytes array back to a file.
    :param file: This is the file name that is to be written to.
    :param string: This is the information that is to be written to the file.
    :return: Nothing useful.
    """

    print("[LOG] Writing file: " + file)
    f = open(file, "wb") #write bytes
    f.write(string)
    f.close()