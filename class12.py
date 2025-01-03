


def is_anagram(self,word):
    if len(self) == len(word):
        # build set of self 
        # build set of word 
        # see if they're equal 

def remove(self,k):




def main():
    the_map = HashMap()
    with open( 'baby_names2016.txt', 'r') as infile:
        for line in infile:
            data = line.rstrip().split(' ')
            the_map.put(data[0], int(data[1]))
    print(the_map)



def main():
    the_map = HashMap()
    with open( 'Dictionary.txt', 'r') as infile:
        for line in infile:
            data = line.rstrip()
            the_map.put( "".join( sorted(data)), data)
    print(the_map)