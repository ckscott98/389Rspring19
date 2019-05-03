# Crypto I Writeup

Name: Cheyenne Scott
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Cheyenne Scott

## Assignment Writeup

### Part 1 (70 Pts)
#!/usr/bin/env python3

import hashlib
import string

def crack():
	hashes = open("hashes.txt", "r")# open and read hashes.txt
	passwords = open("passwords.txt", "r")# open and read passwords.txt
	characters = string.ascii_lowercase
	hashesList = hashes.read().splitlines();
	passList = passwords.read().splitlines();

	for c in characters:
		for p in passList:
			passwd = c+p
			hash1 = hashlib.sha256(passwd.encode()).hexdigest()

			for h in hashesList:
				if h == hash1:
					print(p + ':' + h)

if __name__ == "__main__":
	crack()

### Part 2 (30 Pts)

#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack():
	hashes = open("hashes.txt", "r").read().splitlines()# open and read hashes.txt
	passwords = open("passwords.txt", "r").read().splitlines()# open and read passwords.txt
	characters = string.ascii_lowercase
	server_ip = '134.209.128.58'
	server_port = 1337

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((server_ip, server_port))

	# parse data
	# crack 3 times
	i = 0
	while(i < 3):
		data = s.recv(1024)
		print(data)
		data1 = data.splitlines()
		s = data1[2]
		
		for c in characters:
			for p in passwords:
				passwd = c + p
				hashed = hashlib.sha256(passwd.encode()).hexdigest()

				if s == hashed:
					print(p + ":" + s)
					s.send(hashed + "\n")
					time.sleep(1)
					
		data = s.recv(1024)
		print(data)
		i = i+1
		
if __name__ == "__main__":
	server_crack()

flag: CMSC389R-{h@sh1ng_@nd_sl@sh1ng}
*Your reflection goes here*
