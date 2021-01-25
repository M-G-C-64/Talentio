'''Ramdev baba and Gaur Gopal das both are very good friends. They really like each other 
works. They both like to solve competitive programming questions. But today, they both 
busy, so he asked you to solve this problem.

Sometimes some words like "localization" or "internationalization" are so long that writing 
them many times in one text is quite tiresome.

Let's consider a word too long, if its length is strictly more than 10 characters. All too 
long words should be replaced with a special abbreviation.

This abbreviation is made like this: we write down the first and the last letter of a word 
and between them we write the number of letters between the first and the last letters.

Input Format

The first-line contains an integer n (1 ≤ n ≤ 100). Each of the following n lines contains 
one word. All the words consist of lowercase Latin letters and possess lengths of from 1 to 100 characters.

Constraints

(1 ≤ n ≤ 100)

Output Format

Print n lines. The i-th line should contain the result of replacing the i-th word from the input data.

Thus, "localization" will be spelled as "l10n", and "internationalization» will be spelled as "i18n".

You are suggested to automatize the process of changing the words with abbreviations. At that, 
all too long words should be replaced by the abbreviation and the words that are not too long should not undergo any changes.

Sample Input 0

4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis
Sample Output 0

word
l10n
i18n
p43s'''




num = int(input())
lines = []
for i in range(0,num):
    lines.append(input())

for i in lines:
    if len(i)>10:
        print(i[0],end='')
        print(len(i)-2,end='')
        print(i[-1])
    else:
        print(i)
        
        
        
        
