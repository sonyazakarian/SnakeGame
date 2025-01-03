"""

look at practice questions on hashing and such 

MAD compression scheme: MAD = Multiplication Addition Division

Practice questions. 

1. Solution:
a in [1,23)
b in [0,23)

2. 

hash(i) = ((i * 2 + 3) % 13) % 11
              a   b    p     N

for (1, A): for 1: ((1*2 + 3) % 13) % 11 = 5 = Goes in bucket 5 
for (4, C): for 4: ((4*2 + 3) % 13) % 11 = 0 = Goes in bucket 0
for (5, P): for 5: ((5*2 + 3) % 13) % 11 = 0 = Goes in bucket 0
for (9, L): for 9: ((9*2 + 3) % 13) % 11 = 8 = Goes in bucket 8




Buckets:
0    (4, C)    (5, P)
1
2
3
4
5    (1, A)
6
7
8    (9, L)
9
10



3. Insert values into a hash table with 7 buckets 

4, 7, 9, 10, 14000

for 4:  4 % 7 = 4 
for 7:  7 % 7 = 0
for 9:  9 % 7 = 2
for 10: 10 % 7 = 3
for 14000:  14000 % 7 = 0

Buckets:
0   7   14000
1
2   9
3   10
4   4
5
6


"""