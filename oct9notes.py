

"""

Direct Addressing
- the keys are the indexes
- utilization - inefficient
    - if one of the keys you're trying to store is 1,000, have to store 1,000 slots just to store that last one, 
      and have a lot of wasted space in the preceding 999 spots, some/many of which could be empty 
    - the size of the table can be a disadvantage (have to know largest element)

To minimize this inefficiency, we should use a hash table, with a hash function. This more effectively distributes
the values. 


hash function 
hash(key) --> "key"  (The identity function)
hash_code(key) --> Compression (You pass in a key, get an index)  range for input is (-infinity, infinity)
give me a key, run it through the hashing function, find the index where that key should be 

diff between chaining and open addressing - ?
are there "buckets" in open addressing?

diff between the division method and MAD

Division method 
hash(key) = |hash_code(key)| % N
example
We want to store: 1, 3, 5, 10, 6, 8 (in that order). Put into buckets 0, 1, 2, 3, 4, 5 (6 buckets). 
goes:
0 --> 6
1 --> 1
2 --> 8
3 --> 3
4 --> 10
5 --> 5


You want to make sure that no bucket gets superr long because that'll impact the efficiency. So, then, you make more buckets. 

Load factor L: L = n/N    (n = number of elements you're storing, N = size of the structure (number of buckets?)). 
YOU DON'T WANT YOUR LOAD FACTOR TO BE BIGGER THAN 0.75. 
Once you hit more than 75%, it's a good idea to increase the number of buckets that you have. 
They figured out 0.75 by doing studies. 

prime numbers relevance from the preclass?
better off with prime number of buckets, and prime number of elements?



MAD

hash(key) = ((hash_code(key) | * a + b) % p) % N
1 <= a <= p - 1
0 <= b < p -1
p is prime (we want to pick a prime because this helps scatter things out a bit)
- no chance of a being a multiple of p or vice versa
for a and b, can just pick random, as long as it falls between those specified ranges above. 

e.g. let's pick:
p = 19, a = 3, b = 1
and let's use numbers from our example before

(fabulous quiz question for future)

((key x 3 + 1) % 19) % 6 

0 --> 10 6 0 
1 -->
2 -->
3 -->
4 --> 1 3 5
5 -->

for this particular set of numbers, we can see that it scattered much more nicely/evenly for the division method than for MAD


doubled the size of the structure (i didn't get why):

0 
1
2
3
4
5
6
7
8
9
10 
11

Now we've changed N to be 12, so this is our new equation:
((key x 3 + 1) % 19) % 12

0     10 6 
1
2
3
4     1 5 
5
6     8 
7
8
9
10    3 
11


__hash__

immutable 
you cannot use lists as keys in a dictionary 

if you try immutable keys you will get an error/exception 


__eq__


hashing integers 
e.g. hash(5) = 5. usually pretty simple. although you can pick whether you want it to just return the value itself, or do some operation to it. 

hash("hello") = ?
could do the number of letters: every word that has the same number of letters goes into the same bucket
or every digit could be converted to a number (hex value or something)
could include the place in each calculation
  hash(s) = s[0] + s[1] * p + s[2] * p^2
  this makes sure that hash("hello") is not the same as hash("olelh"). permutation is distinct. 



  LAB 10 question 2


h(x) = ((13x + 5) mod 23) mod N
Values = 41, 28, 11, 82, 40, 75, 21, 0,  90, 52, 96, 70, 83, 98, 1, 43, 4, 85, 79, 87

20 buckets

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20



"""





