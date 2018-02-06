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


if not len(sys.argv) == 7:
    print("[ERROR} Command line aruments incorrect.")
    print("[ERROR] Expecting: \"python sender.py {input_file} {source-ip} {reciever-ip} {source-port} {destination-port} {datagram-filename}\"")
    exit(1)

"""Reading Data"""
keys = helpers.getKeys("test_keys_0")
data = helpers.read(sys.argv[1])
for i in range(0, len(keys)):
    data = encrypt.encrypt(keys[i], data)

data_length = len(data)

total_length = data_length + 20 #adding the length of the header.
total_length = total_length.to_bytes(2, 'big')
print(total_length)

"""Creating psuedo header"""
packet = bytearray()
packet += big_endian_ip(sys.argv[2])
packet += big_endian_ip(sys.argv[3])
packet.append(0x00)
packet.append(17)
packet += total_length

"""Creating UDP Header"""
packet += int(sys.argv[4]).to_bytes(2, "big")
packet += int(sys.argv[5]).to_bytes(2, 'big')
packet += total_length
packet.append(0x00) #adding space for the checksum value
packet.append(0x00)
packet += data

"""Calculating checksum"""
for i in range(0, len(packet)-2, 2):
    



print(packet)
print(len(packet))

