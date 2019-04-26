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
	data = s.recv(1024)
	# parse data
	# crack 3 times
	

if __name__ == "__main__":
	server_crack()
