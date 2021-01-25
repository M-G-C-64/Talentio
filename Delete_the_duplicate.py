'''Given a string S, remove the characters which exist more than one times,and print the remaining string.

Input Format

You are given a string ‘s’.

Constraints

1<=length of string<=100

Output Format

Print the string without characters that are repeated.

Sample Input 0

trigger
Sample Output 0

tie'''




srg = [char for char in input()]
res = ''
for i in range(len(srg)):
    m = 0
    for j in range(len(srg)):
        #print(i,j)
        if i == j:
            pass
        else:
            if srg[i] == srg[j]:
                m = 1
    if m == 0:
        res = res+srg[i]
print(res)
