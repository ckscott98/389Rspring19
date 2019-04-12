# Writeup 7 - Binaries I

Name: Cheyenne Scott
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Cheyenne Scott

## Assignment Writeup

### Part 1 (90 Pts)

*Put your code here as well as in main.c*
```c
/*
 * Name: Cheyenne Scott 
 * Section: 0201
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: Cheyenne Scott 
 */

/* your code goes here */

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int main(){
	int i;
	//make both hex values into strings
	char str1[11];
	char str2[11];
	strcpy(str1, "0x1ceb00da");
	strcpy(str2, "0xfeedface");
	//prints str1 and str2
	printf("%s\n%s\n", str1, str2);
	//xor str2 with str1, set as str2
	char nstr2[sizeof(str2)];
	for(i = 0; i<sizeof(str2); i++){
		nstr2[i] = (char)(str2[i]^str1[i]);
	}
	strcpy(str2, nstr2);
	//xor str1 with str2, set as str1
	char nstr1[sizeof(str1)];
	for(i = 0; i<sizeof(str1); i++){
		nstr1[i] = (char)(str1[i]^str2[i]);
	}
	strcpy(str1, nstr1);
	//xor str1 with str2, set as str2
	char nnstr2[sizeof(str2)];
	for(i = 0; i<sizeof(str2); i++){
		nnstr2[i] = (char)(str2[i]^str1[i]);
	}
	strcpy(str2, nnstr2);
	//makes str2 a string
	//prints str2
	for(i = 0; i< sizeof(str2); i++){
		printf("%02X ", str2[i]);
	}
	//makes str1 a string
	//prints str1
	for(i = 0; i< sizeof(str1); i++){
		printf("%02X ", str1[i]);
	}

	return 0;
}


```
output: 
```
0x1ceb00da
0xfeedface
30 78 57 06 00 64 66 61 63 65 00 30 00 31 63 65 62 30 30 64 61 00 
```

### Part 2 (10 Pts)

*Replace this text with your repsonse to our prompt for part 2!*