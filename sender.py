"""
Author: Nicholas Baron (830278807)
Description: This program reads a file and generates a UDP header writing the information into an output file.
"""

import sys
import helpers
import encrypt

arg_offset = 0
encrypting = 0

if sys.argv[1] == '-e':
    if not len(sys.argv) == 9:
        print("[ERROR] Incorrect sender (encrypt option) command line arguments: \"python sender.py {-e} {keys} {input_file} {sender_ip} {reciever_ip} {source_port} {destination_port} {output_file}\"")
        exit(1)
    else:
        encrypting = 1
        arg_offset = 2
elif not len(sys.argv) == 7:
    print("[ERROR] Incorrect sender command line arguments: \"python sender.py {input_file} {sender_ip} {reciever_ip} {source_port} {destination_port} {output_file}")
    exit(1)

"""Read Port Info"""
source_port = int(sys.argv[4 + arg_offset])
source_port_bytes = source_port.to_bytes(2, 'big')
dest_port = int(sys.argv[5 + arg_offset])
dest_port_bytes = dest_port.to_bytes(2, 'big')

print("Source port: " + str(source_port))
print("Destination port: " + str(dest_port) + "\n")

"""Read IP Addresses"""
source_ip = sys.argv[2 + arg_offset]
source_ip_bytes = helpers.big_endian_ip(source_ip)
dest_ip = sys.argv[3 + arg_offset]
dest_ip_bytes = helpers.big_endian_ip(dest_ip)

print(" Big-endian IP:")
print("Source IP: " + str((source_ip_bytes[0] << 24) + (source_ip_bytes[1] << 16) + (source_ip_bytes[2] << 8) + source_ip_bytes[3]))
print("Destination IP: " + str((dest_ip_bytes[0] << 24) + (dest_ip_bytes[1] << 16) + (dest_ip_bytes[2] << 8) + dest_ip_bytes[3]))
for i in range(0, len(source_ip_bytes)):
    print("Source IP byte" + str(i) + ": " + str(int(source_ip_bytes[3-i])))
for i in range(0, len(dest_ip_bytes)):
    print("Destination IP byte" + str(i) + ": " + str(int(dest_ip_bytes[3-i])))

data = bytearray()
"""Get Data"""
data += helpers.read_file(sys.argv[1 + arg_offset])
if encrypting:
    keys = helpers.get_keys(sys.argv[2])
    data = encrypt.encrypt(keys, data)
data_length = len(data)
if data_length % 2: # Is the string an even number of bytes? If no add 3 bytes.
        data += encrypting.to_bytes(3, 'big')

print("file size(Byte, without zero padding) " + str(data_length))
total_length = data_length + 8
total_length_bytes = total_length.to_bytes(2, 'big')
print("total length(bytes): " + str(total_length))

packet = bytearray()
"""Pseudo Header"""
packet += source_ip_bytes
packet += dest_ip_bytes
packet += int(17).to_bytes(2, 'big')
packet += total_length_bytes

"""UDP Header"""
packet += source_port_bytes
packet += dest_port_bytes
packet += total_length_bytes
packet += int(0).to_bytes(2, 'big') #Checksum placeholder

packet += data

"""Calculating checksum"""
check_sum = helpers.check_sum(packet)
check_sum_bytes = check_sum.to_bytes(2, 'big')
packet[18] = check_sum_bytes[0]
packet[19] = check_sum_bytes[1]
print("checksum: " + hex(check_sum)[2:])

"""Write Datagram"""
try:
    helpers.write_file(sys.argv[6 + arg_offset], packet[12:])
    print("File is successfully written to datagram!")
except:
    print("File is unsuccessfully written to datagram!")
print()
