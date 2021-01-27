#Need to be recondisered

'''This is a simple challenge to get things started. Given a sorted array (arr) and a 
number (V), can you print the index location of V in the array?

Input Format

The first line contains an integer, V , a value to search for.

The next line contains an integer, n , the size of arr.

The last line contains n space-separated integers, each a value of arr[i] where 0<=i

Constraints

0<=i

Output Format

Output the index of V in the array.

Sample Input 0

5
5
2 3 4 25 5
Sample Output 0

4
Sample Input 1

2
5
2 3 4 25 5
Sample Output 1

0'''



ind = int(input())
lenn = int(input())
line = [char for char in input()]
if line[ind-1] == ' ':
    print(0)
else:
    print(line[ind-1])
    
    
    
