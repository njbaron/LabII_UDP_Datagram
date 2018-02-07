import sys
import decrypt
import helpers

if not len(sys.argv) == 5:
    print(len(sys.argv))
    print("[ERROR} Command line aruments incorrect.")
    print("[ERROR] Expecting: \"python reciever.py {key file} {source-ip} {reciever-ip} {input-file}\"")
    exit(1)

"""Reading Sent Data"""
packet = bytearray()
packet += helpers.read(sys.argv[4])
keys = helpers.getKeys(sys.argv[1])

"""Comparing IPs"""
source_ip = helpers.big_endian_ip(sys.argv[2])
dest_ip = helpers.big_endian_ip(sys.argv[3])
if helpers.compare_ip(source_ip, packet[:3]):
    print("[ERROR] Source ip does not match!")
if helpers.compare_ip(dest_ip, packet[4:7]):
    print("[ERROR] Destination ip does not match!")

"""Comparing Ports"""
#FIXME do we need to handle ports?

"""Calculating Checksum"""
checksum_sender = ((packet[18] << 8) + packet[19])
packet[18] = 0
packet[19] = 0
checksum_reciever = helpers.check_sum(packet, False)
checksum_reciever = checksum_reciever[0] << 8 + checksum_reciever[1]
if (checksum_sender & checksum_reciever) == 0:
    print("Checksum Correct")
else:
    print("Checksum Error")
    exit(1)

"""Displaying UDP datagram info"""
source_ip = sys.argv[2]
dest_ip = sys.argv[3]
source_port = (packet[12] << 8) + packet[13]
dest_port = (packet[14] << 8) + packet[15]
total_length = (packet[16] << 8) + packet[17]
print("Datagram from source-address " + str(source_ip) + " source-port " + str(source_port) + " to dest-address " + str(dest_ip) + " dest-port " + str(dest_port) + "; Length " + str(total_length) + " bytes.")
packet = packet[20:]
for i in range(len(keys) - 1, -1, -1):
    packet = decrypt.decrypt(keys[i], packet)
helpers.write("hardcoded_BS", packet)

#FIXME where do we specify the name of the output file?
#FIXME where do we specify the name of the key file?
#FIXME Do we have to check that the ports are the same as in the datagram?
#FIXME Do we have to check that the ip from the cmdline is the same as in the datagram?
#FIXME do we calculate the check sum before anything else in reciever?
