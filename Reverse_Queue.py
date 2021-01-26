'''Write a program to reverse a queue Q

Input Format

The first line contains a single integer q, the number of queries

The next q lines represents the single space-separated integers q1,q2.. qn

Constraints

1 < q < 10^5

1 < q1, q2.. . .qn < 10^3

Output Format

Prints the reversed queue.

Sample Input 0

5
3  5  2  5  8
Sample Output 0

8 5 2 5 3
Sample Input 1

4
67 89 67 89
Sample Output 1

89 67 89 67'''




num = int(input())
qu = list(map(str, input().split()))
for i in range(1,num+1):
    print(qu[-i],end = ' ')
    
    
