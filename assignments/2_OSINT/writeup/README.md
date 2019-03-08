# Writeup 2 - OSINT

Name: Cheyenne Scott
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Cheyenne Scott

## Assignment Writeup

### Part 1 (45 pts)

*Please use this space to writeup your answers and solutions (and how you found them!) for part 1.*
The person's name is Elizabeth Moffet. She works at 1337bank.money. Her twitter is v0idcache (found with namechk.com) and email is v0idcache@protonmail.com. IP address associated with the website is 142.93.136.81. Ports 22 (ssh), 80 (HTTP), 1337 (menandmice-dns), found using nmap. The server is using Werkzeug/0.14.1 Python/3.7.2, which I found using browserspy.dk.

One flag was found in secret directory:
Congrats! Flag is: CMSC389R-{h1ding_fil3s_in_r0bots_L0L}

Flag in the source code:
Good find! CMSC389R-{h1dd3n_1n_plain_5ight}


### Part 2 (75 pts)

*Please use this space to detail your approach and solutions for part 2. Don't forget to upload yourcompleted source code to this /writeup directory as well!*
The found password is linkinpark, which was found by brute forcing and looping through the word list with the username v0idcache and password linkinpark.

Good work! Here's a flag: CMSC389R-{brut3_f0rce_m4ster}
CMSC389R-{YWX4H3d3Bz6dx9lG32Odv0JZh}
