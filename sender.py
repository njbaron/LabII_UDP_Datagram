import sys
import encrypt
import helpers



if not len(sys.argv) == 8:
    print("[ERROR} Command line aruments incorrect.")
    print("[ERROR] Expecting: \"python sender.py {key file} {input-file} {source-ip} {reciever-ip} {source-port} {destination-port} {datagram-filename}\"")
    exit(1)

"""Reading Data"""
keys = helpers.getKeys(sys.argv[1])
data = helpers.read(sys.argv[2])

for i in range(0, len(keys)):
    data = encrypt.encrypt(keys[i], data)

data_length = len(data)
total_length = data_length + 20 #adding the length of the header.
print(total_length)
total_length = total_length.to_bytes(2, 'big')

"""Creating psuedo header"""
packet = bytearray()
packet += helpers.big_endian_ip(sys.argv[3])
packet += helpers.big_endian_ip(sys.argv[4])
packet += int(0).to_bytes(1, 'big')
packet += int(17).to_bytes(1, 'big')
packet += total_length

"""Creating UDP Header"""
packet += int(sys.argv[5]).to_bytes(2, "big")
packet += int(sys.argv[6]).to_bytes(2, 'big')
packet += total_length
packet += int(0).to_bytes(1, 'big') #adding space for the checksum value
packet += int(0).to_bytes(1, 'big')
packet += data

"""Calculating checksum"""
checksum = helpers.check_sum(packet)
packet[18] = checksum[0]
packet[19] = checksum[1]

"""Writing to file"""
helpers.write(sys.argv[7], packet)

print(packet)
print(len(packet))

