import random 
dict = {}

with open ('Dictionary.txt', 'r') as file:
    for word in file:
        strip = word.rstrip().lower()
        #wordlength = random.randint((len(word)), )
        wordlength = random.randint(1, 20)
        
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

        #wordlength = dict[wordlength]

#answer = random.choice((dict[wordlength]))
#guess = input(str(''))
#wordlength = int(input("pick a wordlength"))

#wordpool = [word for word in dict[wordlength] if len(word) == tries]
#answer = random.choice(dict[wordlength])
answer = int(input('how many letters?'))
#answer = dict[wordlength]
guessed_letters = []
#len(answer) == 5
state = '*' * len(answer)
tries = input('how many tries do you want?')
tried = 0
#tries = len(answer)



#str(len(answer)) = 6

        #word = 'car'
        #while tries < 6:
while tried < tries and "*" in state:
    #tries +=1
    guess = input('')
    wordfamily = {}
    while(len(guess)!= 1):
        print("Invalid")
    guessed_letters.append(guess)    
    ind_occur = answer.count(guess)
    
    largest_family = max(wordfamily.values())       
    word_list = largest_family     

    for word in file:
        for i in word:
            if word[i] == guess:
                print(f"words with {guess}:{word}")
                state[i] = guess
            else:
                tries -=1



    
    print("This is your progress:", state)    
    print("you have", tries - tried, "guesses left")
    print()
#print("The word was")
    if tries == 0:
        print(f"Game Over! The are no more")   
    else:
        print(f"Congratulations! You WON! The last word i {word}")
