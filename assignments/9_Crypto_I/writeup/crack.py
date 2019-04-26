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
