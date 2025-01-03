
import random

def mystery_function():
    n = int(input("How large an array would you like? "))
    array = [random.random() for i in range(n)]
    q1_count = 0
    q2_count = 0
    q3_count = 0

    for i in range(1,n+1):
        q1_count += 1
        for j in range(i):
            q2_count += 1
            array[j] += 1
            q3_count += 1
    print(f"{q1_count}")
    print(f"{q2_count}")
    print(f"{q3_count}")

    if q2_count == q1_count * (q1_count + 1) / 2 and q3_count == q1_count * (q1_count + 1) / 2:
        print("True")


    return array 

    

mystery_function()



"""

def mystery_function():
    n = 19
    array = [random.random() for i in range(n)]
    q1_count = 0
    q2_count = 0
    q3_count = 0

    for i in range(1,n+1):
        print("YAY")
        q1_count += 1
        for j in range(i):
            print("YAY!")
            q2_count += 1
            array[j] += 1
            print("YAYYYYYY!!!!!!!!")
            q3_count += 1
    
    print(f"{q1_count}")
    print(f"{q2_count}")
    print(f"{q3_count}")

    return array

mystery_function()









for i in range(1,5):
    print("Yay!")



for i in range(1,20):
    for j in range(i):



1: for j in range(1)     runs once 
2: for j in range(2)      runs twice 
3: for j in range(3)   
4: for j in range(4)
5: for j in range(5)
6: for j in range(6)
7: for j in range(7)
8: for j in range(8)
9: for j in range(9)
10: for j in range(10)

goes until 19. 


1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + .... + 19

1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + ... + n - 1




"""