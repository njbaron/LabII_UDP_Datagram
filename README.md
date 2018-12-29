# LabII_UDP_Datagram
This is a program that will encrypt and decrypt data and append a UDP datagram header. 

UDP Datagram Sender/ Reciever
By Nick Baron

You need to have python!

How to run Sender
* Once the zip file has been extracted place sender.py, reciever.py, encrypt.py, decrypt.py, and helpers.py in a folder together.
* All of the key files as well as all of the test files should then be added to the same folder.
* In a terminal window(in windows power-shell or equivalent) move to the directory that contains the programs.
* Use the command "python sender.py {-e} {key_file} [input_file] [sender_ip] [reciever_ip] [sender_port] [reciever_port] [output_file]"
	* the {-e} is a flag that will cause the program to try and encrypt the [input_file] with the keys int the {key_file}.
	* if {-e} is not added only the commands in the [] are required.
* the [output_file] is generated with a UDP datagram.

How to run the Reciever
* Once the zip file has been extracted place sender.py, reciever.py, encrypt.py, decrypt.py, and helpers.py in a folder together.
* all of the key files as well as all of the test files should then be added to the same folder.
* In a terminal window(in windows power-shell or equivalent) move to the directory that contains the programs.
* Use the command "python reciever.py {-d} {key_file} [input_file] [sender_ip] [reciever_ip] [output_file]"
	* the {-d} is a flag that will cause the program to try and decrypt the [input_file] with the keys int the {key_file}.
	* if {-d} is not added only the commands in the [] are required.
* the [output_file] is generated with the recieved file infromation. It will be the same as the input file from the sender.

Example Commands(Using provided example files)
* Sender: `python .\sender.py .\test_file_0 192.168.1.1 192.168.1.0 53 5534 output`
* Sender with encryption: `python .\sender.py -e .\test_keys_0 .\test_file_0 192.168.1.1 192.168.1.0 53 5534 output`
* Reciever: `python .\reciever.py output 192.168.1.1 192.168.1.0 recieved`
* Reciever with decryption: `python .\reciever.py -d .\test_keys_0 output 192.168.1.1 192.168.1.0 recieved`
