"""
Author: Nick Baron (830278807)
Description: This program reads a UDP datagram file and checks to make sure that the infromation is recieved without errors. It then writes the correct info to a output file.
"""

import sys
import helpers
import decrypt

arg_offset = 0
decrypting = 0

if sys.argv[1] == '-d':
    if not len(sys.argv) == 7:
        print("[ERROR] Incorrect reciever (decrypt option) command line arguments: \"python reciever.py {-d} {keys} {input_file} {sender_ip} {reciever_ip} {output_file}")
        exit(1)
    else:
        decrypting = 1
        arg_offset = 2
elif not len(sys.argv) == 5:
    print("[ERROR] Incorrect reciever command line arguments: \"python reciever.py {input_file} {sender_ip} {reciever_ip} {output_file}")
    exit(1)

packet = bytearray()
"""Read Datagram"""
packet += helpers.read_file(sys.argv[1 + arg_offset])

"""Get IP Addresses"""
source_ip = sys.argv[2 + arg_offset]
source_ip_bytes = helpers.big_endian_ip(source_ip)
dest_ip = sys.argv[3 + arg_offset]
dest_ip_bytes = helpers.big_endian_ip(dest_ip)

print("Source IP: " + str(source_ip_bytes))
print("Destination IP: " + str(dest_ip_bytes))

total_length_bytes = packet[4: 6]
total_length = (total_length_bytes[0] << 8) + total_length_bytes[1]
print("total length(bytes):" + str(total_length))

header = bytearray()
"""Psuedo Header"""
header += source_ip_bytes
header += dest_ip_bytes
header += int(17).to_bytes(2, 'big')
header += total_length_bytes

header = header + packet

"""Calculating Checksum"""
checksum_sender = ((header[18] << 8) + header[19])
header[18] = 0
header[19] = 0
checksum_reciever = helpers.check_sum(header, False)
checksum = checksum_sender + checksum_reciever
print("checksum:" + hex(checksum)[2:])
if checksum == 0xffff:
    print("Yupee checksum is correct!!!")
else:
    print("Boo checksum incorrect!!!")
    exit(1)

data = packet[8: total_length]
"""Decrypt Information"""
if decrypting:
    keys = helpers.get_keys(sys.argv[2])
    data = decrypt.decrypt(keys, data)

"""Write Info to File"""
helpers.write_file(sys.argv[4 + arg_offset], data)
print()