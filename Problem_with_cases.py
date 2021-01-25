'''Ishani is very upset that many people on the internet mix uppercase and lowercase letters 
in one word. That's why she decided to invent an extension for his favorite browser that would 
change the letters' register in every word so that it either only consists of lowercase letters 
or, vice versa, only of uppercase ones. At that as little as possible letters should be changed 
in the word. For example, the word MoUse must be replaced with mouse, and the word SiP — with 
SIP. If a word contains an equal number of uppercase and lowercase letters, you should replace 
all the letters with lowercase ones. For example, maTRIx should be replaced by matrix. Your task 
is to use the given method on one given word.

Input Format

The first line contains a word s — It consists of uppercase and lowercase letters and possesses 
the length from 1 to 100.

Constraints

1<=length of s<=100

Output Format

The first line contains a word s — it consists of uppercase and lowercase Latin letters and 
possesses the length from 1 to 100.

Sample Input 0

BNHWpnpawg
Sample Output 0

bnhwpnpawg
Sample Input 1

VTYGP
Sample Output 1

VTYGP'''




import re

line = input()
low = re.findall("[a-z]",line)
upp = re.findall("[A-Z]",line)

if len(low)>=len(upp):
    print(line.lower())
else:
    print(line.upper())
