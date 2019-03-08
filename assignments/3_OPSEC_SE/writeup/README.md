# Writeup 3 - Operational Security and Social Engineering

Name: Cheyenne Scott
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Cheyenne Scott

## Assignment Writeup

### Part 1 (40 pts)

Using the knowledge that Elizabeth has already suffered a web server breach, I would contact her through email and provide a legit looking phone number for her to contact, making myself look like a company that secures websites and services. I would even set up a quick website and make it google-able so if she were to try to research it, it would come up. When she calls to get help, or I call her (depending on how the email goes), I would get to know her a little bit, ask her about how she is doing and try to come across as a super overly friendly customer service representative, just looking to help. First, I would tell her about our "packages", mentioning how each one will provide more security, kind of like life lock. I would even recommend her the "cheaper" option as that would cover her bases. When she goes to pay, I would give her the option to pay over the phone, in which case we would need her card number and pin, which she could enter into the phone and then I could use a device to capture the numbers they dial, thus not only giving me their card number, but also their pin. To get the maiden name, pet, and city, I would offer to make their account over the phone and save time. Here, I would ask for a username and password, then have her answer three security questions which require mother's maiden name, city they were born in and their first pet. Finally, I would gather "additional" information about them in order to implement the most effective firewall for their server. I would need their server information, the type of data that would be most frequently accessed on the server and what browser they primarily use when accessing the server, since I will find out that it is used for their website. 

### Part 2 (60 pts)

One vulnerability was the use of the same username for multiple websites and to log into important accounts, like for the webserver. One way to mitigate this issue of a guessed username from other sites, is using different usernames for different websites. It would make it more difficult to link the different accounts together. For accounts like the webserver, it should have it's own username that is seperate from all other associated and public accounts. Another big vulnerability was having an open port. The open port allowed access to the web server. Since the port also gave essentially unlimited attempts, a brute force attack was much easier to implement. To fix this, putting a firewall on all ports and changing port numbers to commonly unused ones will give the attacker a harder time and increase your time to react. Finally, a weak password was used, one so weak that it was on a leaked password list. By going through a password list of previously leaked passwords and implementing a brute force attack, we were able to guess the password to the webserver. To avoid this problem, changing passwords and using different passwords for different areas would be helpful. Passwords should also contain at least 8 characters, numbers, both upper and lowercase letters and special characters. Making common words or names passwords is also an easy way for a hacker to guess it. Making it phrases with various things mixed in will lead to a stronger password. 
