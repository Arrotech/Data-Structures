# Linked Lists

Linked lists can be implemented in `Stacks, Queues, and Graphs`.

## Linked lists vs lists

### 1. Performance

 Lists are `dynamic arrays` and therefore the `memory usage` for both lists and linked lists is very `similar` or rather `insignificant`.

 ### 2. Insertion and Deletion

 The `insert()` and `remove()` functions are used to insert or remove items at `specific positions`.

 The `append()` and `pop()` functions are used to insert or delete items from the `end of the list`.

  Inserting or removing items that are `at the end of the list` takes constant time, 0(1).

 Inserting or removing items that are `not at the end of the list` requires `shifting` at the background, so it `consumes more time`. When inserting or removing items closer to the beginning or at the beginning of a list, the `time complexity will grow with the size of the list`.

 Inserting or removing items at the `beginning or at the end of a linked list` will have a `constant time complexity of, 0(1)`.

    NB: 1.For this reason linked lists have a performance advantage when using Queues(FIFO). This is because queues involve inserting and removing elements at the beginning of the list.


    NB: 2.When working with stacks(LIFO) the performance is similar because items are inserted or removed at the end of the list.

### 3. Element Retrieval/lookup

When searching for a specific element, both lists and linked lists have `similar performance, time complexity of 0(n)`, since you need to `iterate the whole list` to find the element you are looking for.

When it comes to element lookup, lists perform much better than linked lists. When you know which element you want to access, lists can perform this operation in `O(1)` time. Trying to do the same with a linked list would take `O(n) because you need to traverse the whole list` to find the element.

## Deque

The method `collections.deque()` pronounced as ('deck') stands for `double-ended queue` can be used for linked lists to:

1. Create an empty list.
2. Create linked list with iterable items `(strings, lists, and dictionaries)`.
3. Add and remove elements at the beginnig and at the end of the linke list.

### Implementing Queues and Stacks

#### Queues

With queues, you want to add values to a list `(enqueue)`, and when the timing is right, you want to remove the element that has been on the list the longest `(dequeue)`. For example, `imagine a queue at a trendy and fully booked restaurant. If you were trying to implement a fair system for seating guests, then you’d start by creating a queue and adding people as they arrive:`

Suppose you have Mary, John, and Susan in the queue in that order. Remember that since queues are `FIFO`, the first person who got into the queue should be the first to get out.

Now imagine some time goes by and a few tables become `unavailable`. At this stage, you want to remove people from the queue in the correct order.

    Every time you call popleft(), you remove the head element from the linked list, mimicking a real-life queue.

#### Stacks

`Stack` uses the `LIFO` approach, meaning that the last element to be inserted in the stack should be the first to be removed.

Imagine you’re creating a web browser’s history functionality in which store every page a user visits so they can go back in time easily.

Every time the user visited a new site, you added it to your history variable using appendleft(). Doing so ensured that each new element was added to the head of the linked list.

Now suppose that after the user read both articles, they wanted to go back to the first home page to pick a new article to read. Knowing that you have a stack and want to remove elements using LIFO.