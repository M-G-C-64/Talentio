'''Rahul has got a new phone.He is getting lots of messages on Facebook and many of 
them are from girls.But he knows many boys uses fake ID to prank others. So he designed 
a method to guess whether the user who messaged him is a male or female. If the number 
of distinct characters in one's user name is odd, then he is a male, otherwise she is 
a female.

You are given the string that denotes the user name, please help our Rahul to determine 
the gender of this user by his method

Input Format

The first-line contains a non-empty string, that contains only lowercase English letters 
— the user name. This string contains at most 100 letters.

Constraints

1<=length of string<=1000

Output Format

If it is a female by our Chandu's method (the number of distinct characters is 'ODD' ), 
print "CHAT WITH HER!" (without the quotes), otherwise, print "IGNORE HIM!" (without the quotes).

Sample Input 0

wjmzbmr
Sample Output 0

CHAT WITH HER!
Sample Input 1

xiaodao
Sample Output 1

IGNORE HIM!'''




inp = [char for char in input()]
inps = set(inp)
if len(inps)%2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
    
    
