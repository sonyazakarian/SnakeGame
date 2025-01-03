




# Update current from Alpha to Beta
current = current.next

# Now current is at Beta
# Remove Gamma
current.next = current.next.next
current.next.prev = current

# Point Delta's next to trailer
current.next.next = None          
trailer.prev = current.next 





"""
A max-priority queue is an abstract data type like queue with the added requirement that items are stored with a priority:

Higher-priority elements of the queue are dequeued first.
Consider a priority queue with the following methods in the interface:

enqueue(element, priority) - inserts a new element into the queue, with the given priority
dequeue_max() - dequeues the element in the queue with the highest priority. If two elements have the same priority, then the first one enqueued is the first one dequeued.
maximum() - returns the highest priority element 

What data structure is best suited for implementing a max-priority queue? What's the runtime for each of the operations?
"""
"""

Queue

Priority = Low or High 

enqueue(4, Low)
enqueue(2, High)
enqueue(7, Low)
enqueue(8, High)
enqueue(9, High)
enqueue(11, High)
enqueue(14, Low)
"""

dequeue_max()

4 2 7 8 9 11 14
L H L H H H  L 

dequeue_max()
take out elements with High Priority 
However, 2, 8, 9 and 11 all have the same priority 

first one enqueued is first one dequeued. So, 2 is dequeued. 

new list: 

4 7 8 9 11 14

dequeue_max() again 

4 7 9 11 14

maximum()


