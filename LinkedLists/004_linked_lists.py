
class LinkedList:
    """Linked List."""

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = node

    def insert_in_between(self, existing_node, data):
        if existing_node is None:
            print("Node is missing.")
            return
        node = Node(data)
        node.next = existing_node.next
        existing_node.next = node

    def remove_node(self, data):
        node = self.head
        if node is not None:
            if node.data == data:
                self.head = node.next
                node = None
                return
        while node is not None:
            if node.data == data:
                break
            previous = node
            node = node.next

        if node is None:
            return

        previous.next = node.next
        node = None

    def print_list(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " --> ".join(nodes)


class Node:
    """Node Element."""

    def __init__(self, data=None, next=None):
        """Initialize variables."""
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data


if __name__ == '__main__':
    linked_list = LinkedList()

    first_node = Node("a")
    linked_list.head = first_node

    second_node = Node("b")
    third_node = Node("c")

    first_node.next = second_node
    second_node.next = third_node

    linked_list.insert_at_beginning("d")
    linked_list.insert_at_end("e")
    linked_list.insert_in_between(second_node, "g")
    linked_list.remove_node("g")
    linked_list.remove_node("e")
    linked_list.remove_node("d")
    print(linked_list.print_list())
