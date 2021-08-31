from collections import deque

history = deque()

history.appendleft('arrotech.co.ke')
history.appendleft('arrotech.co.ke/articles')
history.appendleft('arrotech.co.ke/articles/flask-python')

history.popleft()
history.popleft()

if __name__ == '__main__':
    print(history)