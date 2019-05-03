# Crypto II Writeup

Name: Cheyenne Scott
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Cheyenne Scott 

## Assignment Writeup

### Part 1 (70 Pts)
flag is: CMSC389R-{m3ss@g3_!n_A_b0ttl3}

Couldn't get screenshot in here, so it is in a separate file.

### Part 2 (30 Pts)

1. Both of the files come out fizzier and more gray than the original. They both have about 5 main colors for the dots. Both files also keep the same shape and size as the original. 

2. ECB would be less secure because it adds some encryption and changes the original colors, however, you are still able to see the outlines of the shapes as well as the inner shapes and location. There is still information leaked by using ECB, while CBC makes it much less readable and harder to get any information from just looking at the picture. This makes sense too because ECB is more basic and will only encrypt a file one time in blocks (which is why you have that line effect). CBC will encrypt in blocks then continue to encrypt on top of that. 
