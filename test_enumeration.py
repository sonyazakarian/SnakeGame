



from enum import Enum

class Color(Enum):  # inheritance class
    RED = 1 
    GREEN = 2
    BLUE = 3

class WeekDays(Enum):
    MONDAY = 1
    TUESDAY = 2 
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6 
    SUNDAY = 7 

class Counter:

    def __init__(self,start,end):
        self.val = 0 
        self.start = start
        self.end = end

    def __iter__(self):
        self.val = 0 # this is like a count variable
        return self 
    
    def __next__(self):
        next_val = self.val 
        self.val += 1
        return next_val 


def main():
    print(Color.RED)
    for c in Color:
        print(c)

    for d in WeekDays:
        print(d)

    the_day = WeekDays.MONDAY
    if the_day is WeekDays.TUESDAY:
        print("NO")

    foo = Counter()
    next_val = next(foo)
    print(next_val)
    print(next(foo))
    print(next(foo))

    # for num in foo:
    #   print(num)

    for count in [0,1,2,3,4]:
        print(count)

    foo = Counter(0,4)
    for count in foo:
        print(count)

if __name__ == '__main__':
    main()