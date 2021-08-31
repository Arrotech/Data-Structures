from collections import deque

# initialize an empty linked list
empty_list = deque()

# initialize linked list with a string
string_list = deque('abcde')

# initialize linked list with a list
list1 = deque(['a', 'b', 'c', 'd', 'e'])

# initialize linked list with dictionaties
dict_list = deque([{'1': 'a'}, {'2': 'b'}])

# add items at the end of the linked list
list1.append('f')

# add items at the beginning of the linked list
list1.appendleft('g')

# remove items at the end of the linked list
list1.pop()

# remove items at the beginning of the linked list
list1.popleft()

if __name__ == '__main__':
    print(empty_list)
    print(string_list)
    print(list1)
    print(dict_list)
