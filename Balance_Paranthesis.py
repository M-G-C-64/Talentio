'''Implement a program which prints 1 if the parenthesis in the given infix expression are balanced else 0.

Input Format

Refer sample input

Constraints

Input should not be empty.

Output Format

Refer sample output

Sample Input 0

9+(7-3*2)
Sample Output 0

1
Sample Input 1

()))
Sample Output 1

0'''




line = [char for char in input()]
u = 0
l = 0
for i in line:
    if i == '(':
        u = u+1
    elif i == ')':
        l = l+1
    else:
        pass
if u == l:
    print('1')
else:
    print('0')
    
    
