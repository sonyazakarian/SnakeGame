

# pretend this is the SLL file 
# incl. the Node class and SLL class



class SLLIterator:

    def __init__(self,start,end):
        self.current = start
        

    def __next__(self):
        if not self.current is None:
            return_value = self.current.value
            self.current = self.current.next
            return return_value
        else:
            raise StopIteration()
        
    def __iter__(self):
        return self
        


class SinglyLinkedList:

    def __iter__(self):
        return SLLIterator(self.head)
    




def main():
    the_list.add_first(5)
    the_list.add_first(10)
    the_list.add_first(15)
    the_list.add_last(20)
    the_list.add_last(30)
    print(f"the_list is: {the_list}")

    list_iter = iter(the_list)

    
