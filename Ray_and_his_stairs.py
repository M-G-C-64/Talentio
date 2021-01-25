'''Ray climbs the stairs inside a multi-storey building. Every time Ray climbs a stairway, he starts 
counting steps from 1 to the number of steps in this stairway. he speaks every number aloud. For example, 
if he climbs two stairways, the first of which contains 3 steps, and the second contains 4 steps, he will 
pronounce the numbers 1,2,3,1,2,3,4.

You are given all the numbers pronounced by Ray. How many stairways did he climb? Also, output the 
number of steps in each stairway.

The given sequence will be a valid sequence that Ray could have pronounced when climbing one or
more stairways.

Input Format
The first line contains n (1≤n≤1000) — the total number of numbers pronounced by Ray.

The second line contains integers a1,a2,…,an (1≤ai≤1000) — all the numbers Ray pronounced
while climbing the stairs, in order from the first to the last pronounced number. Passing 
a stairway with x steps, he will pronounce the numbers 1,2,…,x in that order.

The given sequence will be a valid sequence that Ray could have pronounced when climbing 
one or more stairways.

Constraints

1≤ai≤1000

Output Format
In the first line, output t — the number of stairways that Ray climbed. In the second line, 
output t numbers — the number of steps in each stairway he climbed. Write the numbers in the 
correct order of passage of the stairways.

Sample Input 0
5
1 2 1 2 1

Sample Output 0
3
2 2 1
Sample Input 1

1
1
Sample Output 1

1
1'''







tot = int(input())
seq = list(map(int, input().split(' ')))
otot = 1
mxst = []
for i in range(len(seq)-1):
    #print(i)
    if seq[i+1] <= seq[i]:
        otot = otot + 1
        mxst.append(seq[i])
mxst.append(seq[-1])
print(otot)
for i in mxst:
    print(i,end = ' ')
