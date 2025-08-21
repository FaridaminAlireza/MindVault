# Node of a Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Singly Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    # Search for a key
    def search(self, key):
        curr = self.head
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        return False

    # Delete by value
    def delete(self, key):
        curr = self.head

        # If head node holds the key
        if curr and curr.data == key:
            self.head = curr.next
            return

        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next

        if curr is None:
            return  # key not found

        prev.next = curr.next

    # Count nodes
    def count(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    # Print the linked list
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")


# ✅ Example Usage
if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_beginning(5)
    ll.insert_at_end(30)

    print("Linked List: ", end="")
    ll.print_list()   # 5 -> 10 -> 20 -> 30 -> None

    print("Search 20:", ll.search(20))  # True
    print("Search 99:", ll.search(99))  # False

    print("Count:", ll.count())         # 4

    ll.delete(10)
    print("After deleting 10: ", end="")
    ll.print_list()                     # 5 -> 20 -> 30 -> None
