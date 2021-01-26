'''Write a program to perform pairwise swap of linked list

Input Format

The first line consist of an upper limit of the list(including the integer).

The second line consists of lower limit of the list(excluding the integer).

Constraints

The upper and lower limits should be positive integers.

Output Format

The first line consists of elements of linked list.

The second line consists of pairwise swapped elements of the list.

Sample Input 0

5
2
Sample Output 0

3 4 5 
4 3 5
Sample Input 1

6
3
Sample Output 1

4 5 6 
5 4 6'''



upp = int(input())#in
low = int(input())#ex
lst = []
for i in range (low+1,upp):
    print(i,end = ' ')
    lst.append(i)
lst.append(upp)
print(lst[-1])
for i in range(len(lst)):
    if len(lst)%2 == 0:
        pass
    else:
        if i == len(lst)-1:
            print(lst[i])
    if i%2==0:
        pass
    else:
        print(lst[i],lst[i-1],end = ' ')
    
    
    
    
