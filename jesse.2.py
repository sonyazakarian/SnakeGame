import random 
#dict = {}

with open ('Dictionary.txt', 'r') as file:
        
            strip = [word.strip().lower() for word in file]
            #wordlength = random.randint((len(word)), )
            """wordlength = random.randint(1, 20)
            
            #print(wordlength)
            #dict[wordlength] = []
            #dict[wordlength].append(word)
            #if(type([]) == type(dict[wordlength])):
            if (wordlength in dict.keys()):
                dict[wordlength].append(strip)

            else:
                dict[wordlength] = []
                dict[wordlength].append(strip)
            #print(dict[wordlength])

            #wordlength = dict[wordlength]"""

    #answer = random.choice((dict[wordlength]))
    #guess = input(str(''))
    #wordlength = int(input("pick a wordlength"))

    #wordpool = [word for word in dict[wordlength] if len(word) == tries]
    #answer = random.choice(dict[wordlength])
length = int(input('how many letters?: '))
    #answer = dict[wordlength]

    #len(answer) == 5
word_list = [word for word in strip if len(word) == length]
state = '*' * length
tries = int(input('how many tries do you want?: '))
guessed_letters = []
    #tried = 0
    #tries = len(answer)

    #tries = 0


    #str(len(answer)) = 6

            #word = 'car'
            #while tries < 6:
while tries>0 and "*" in state:
    print('this is your progress', state)
    print(f'lives left: {tries}')
    #tries +=1
    guess = input('guess a letter: ').lower()
    print(word_list)
    if not guess.isalpha() or len(guess)!= 1 or guess in guessed_letters:
        print("Invalid")
        continue
    
    guessed_letters.append(guess)    
    #ind_occur = answer.count(guess)
    wordfamily = {}
    
    
    
    #pattern = 
    for word in word_list:
        pattern = ''.join(r if r == guess else '*' for  r in word)
        wordfamily.setdefault(pattern, []).append(word)

    largest_family = max(wordfamily.values(), key=len)  
    #largest_family = wordfamily.values()     
    word_list = largest_family    
    #print(wordfamily)

        

    if guess in word_list[0]:
        for i in range(length):
            if word_list[0][i] == guess:
                    #print(f"words with {guess}:{word_list}")
                state[i]= guess
                #print(state)
    else:
        tries -=1



    
    """print("This is your progress:", state)    
    print("you have", tries - tried, "guesses left")
    print()"""
#print("The word was")
if tries == 0:
    print(f"Game Over! The are no more, the answer was{random.choice(word_list)}")   
else:
    print(f"Congratulations! You WON! The last word is {word_list[0]}")