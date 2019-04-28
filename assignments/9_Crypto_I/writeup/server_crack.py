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
