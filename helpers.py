"""
Author: Nick Baron 830278807
Description: This is a set of helper methods that can be used for a variety of purposes.
"""


def get_keys(keyFileName, numberKeys = 8):
    """
    This functions retrieves keys from a file.
    :param keyFileName: This is the filename that is supposed to contain the keys.
    :param numberKeys: This is the number of keys that are being requested for encryption.
    :return: This is a bytes array that contains the keys.
    """
    keys = read_file(keyFileName)

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


def read_file(file):
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


def write_file(file, string):
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

def big_endian_ip(ip_string):
    ip_string_arr = ip_string.split(".")
    if not len(ip_string_arr) == 4:
        print("[ERROR] Invalid IP: " + str(ip_string))
        exit(1)
    big_endian = bytearray()
    for i in range(3, -1, -1):
        big_endian.append(int(ip_string_arr[i]))
    return big_endian

def ones_add(a, b):
    b = (b[0] << 8) + b[1]
    ret_int = a + b
    print("a: " + str(a))
    print("b: " + str(b))
    while ret_int > 0xffff:
        remainder = ret_int >> 16
        ret_int = (ret_int & 0xffff) + remainder
    return ret_int

def check_sum(packet, compliment = True):
    checksum = 0
    for i in range(0, len(packet), 2):
        checksum = ones_add(checksum, packet[i:i + 2])
    if compliment:
        checksum = checksum ^ 0xffff
    print(checksum)
    return checksum

def compare_ip(source, read):
    ret_bool = True
    for i in range(0, len(source)):
        try:
            if not source[i] == read[i]:
                ret_bool = False
        except:
            ret_bool = False
    return ret_bool