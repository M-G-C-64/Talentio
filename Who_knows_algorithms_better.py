'''Limak and Radewoosh are going to compete against each other in the upcoming algorithmic contest. 
They are equally skilled but they won't solve problems in the same order.

There will be n problems. The i-th problem has initial score pi and it takes exactly ti minutes to 
solve it. Problems are sorted by difficulty — it's guaranteed that pi < pi + 1 and ti < ti + 1. A 
constant c is given too, representing the speed of loosing points. Then, submitting the i-th problem 
at time x (x minutes after the start of the contest) gives max(0,  pi - c·x) points.

Limak is going to solve problems in order 1, 2, ..., n (sorted increasingly by pi). Radewoosh is going 
to solve them in order n, n - 1, ..., 1 (sorted decreasingly by pi). Your task is to predict the outcome 
— print the name of the winner (person who gets more points at the end) or a word "Tie" in case of a tie.

You may assume that the duration of the competition is greater or equal than the sum of all ti. That 
means both Limak and Radewoosh will accept all n problems

Input Format

The first line contains two integers n and c (1 ≤ n ≤ 50, 1 ≤ c ≤ 1000) — the number of problems and 
the constant representing the speed of loosing points. The second line contains n integers p1, p2, ..., pn 
(1 ≤ pi ≤ 1000, pi < pi + 1) — initial scores. The third line contains n integers t1, t2, ..., tn 
(1 ≤ ti ≤ 1000, ti < ti + 1) where ti denotes the number of minutes one needs to solve the i-th problem.

Constraints

(1 ≤ n ≤ 50, 1 ≤ c ≤ 1000)

Output Format

Print "Limak" (without quotes) if Limak will get more points in total. Print "Radewoosh" (without quotes)
if Radewoosh will get more points in total. Print "Tie" (without quotes) if Limak and Radewoosh will get 
the same total number of points.

Sample Input 0

3 2
50 85 250
10 15 25
Sample Output 0

Limak
Sample Input 1

3 6
50 85 250
10 15 25'''




ip1 = list(map(int, input().split(' ')))
n = ip1[0]
c = ip1[1]
pi = list(map(int, input().split(' ')))
ti = list(map(int, input().split(' ')))
L = 0
R = 0
x = 0
for i in range(len(pi)):
    x = x+ti[i]
    L = L + max(0, pi[i]-c*x)
#print(L)
x = 0
for i in range(len(pi)):
    x = x+ ti[-i-1]
    R = R + max(0, pi[-i-1]-c*x)
#print(R)
print('Limak') if L>R else print('Tie') if R==L else print('Radewoosh')





