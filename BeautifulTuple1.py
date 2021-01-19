'''
Print whether the tuple is beautiful or not

A tuple is considered beautiful if all elements in the tuple are divisible by first element.

Input Format

Refer Sample Input

Constraints

Elements of tuple should not be empty.

Output Format

Refer Sample Output

Sample Input 0

1 4 5 3 4 6 6
Sample Output 0

YES
Sample Input 1

4 4 5 3 4 4 4
Sample Output 1

NO
'''

tup = list(map(int, input().split()))
base = tup[0]

for i in tup:
    k=i%base
    if k == 0:
        pass
    else:
        break
if k == 0:
    print("YES")
else:
    print("NO")
