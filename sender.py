import sys
import encrypt
import helpers

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
    a
    b = (b[0]<<8) + b[1]
    ret_int = a + b
    print(a)
    print(b)
    while(ret_int > 0xffff):
        remainder = ret_int >> 16
        ret_int = (ret_int-0x10000) + remainder
    return ret_int


if not len(sys.argv) == 7:
    print("[ERROR} Command line aruments incorrect.")
    print("[ERROR] Expecting: \"python sender.py {input_file} {source-ip} {reciever-ip} {source-port} {destination-port} {datagram-filename}\"")
    exit(1)

"""Reading Data"""
keys = helpers.getKeys("test_keys_0")
data = helpers.read(sys.argv[1])

data_length = len(data)

for i in range(0, len(keys)):
    data = encrypt.encrypt(keys[i], data)

total_length = data_length + 20 #adding the length of the header.
print(total_length)
total_length = total_length.to_bytes(2, 'big')

"""Creating psuedo header"""
packet = bytearray()
packet += big_endian_ip(sys.argv[2])
packet += big_endian_ip(sys.argv[3])
packet += int(0).to_bytes(1, 'big')
packet += int(17).to_bytes(1, 'big')
packet += total_length

"""Creating UDP Header"""
packet += int(sys.argv[4]).to_bytes(2, "big")
packet += int(sys.argv[5]).to_bytes(2, 'big')
packet += total_length
packet += int(0).to_bytes(1, 'big') #adding space for the checksum value
packet += int(0).to_bytes(1, 'big')
#packet += data

"""Calculating checksum"""
checksum = 0x00
for i in range(0, len(packet)-2, 2):
    checksum = ones_add(checksum, packet[i:i+2])
print(checksum)
checksum = checksum ^ 0xffff
print(checksum)
checksum = checksum.to_bytes(2,'big')
packet[18] = checksum[0]
packet[19] = checksum[1]




print(packet)
print(len(packet))

