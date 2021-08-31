from collections import deque

# Suppose you are serving people at the restaurant, you want to serve them in the order of their arrival therefore you have them queued.

queue = deque()

# adding people to the queue in the correct order
queue.append('Mary')
queue.append('John')
queue.append('Harun')

# removing people from the queue in the correct order
# every time you call popleft() you remove the head element.
queue.popleft()

if __name__ == '__main__':
    print(queue)