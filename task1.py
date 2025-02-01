class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sorted(self, other):
        dummy = Node()
        tail = dummy
        a, b = self.head, other.head
        
        while a and b:
            if a.data < b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        
        tail.next = a if a else b
        
        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list

    def insertion_sort(self):
        if not self.head or not self.head.next:
            return

        sorted_list = None
        current = self.head

        while current:
            next_node = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node

        self.head = sorted_list

    def sorted_insert(self, sorted_head, new_node):
        if not sorted_head or new_node.data < sorted_head.data:
            new_node.next = sorted_head
            return new_node
        
        current = sorted_head
        while current.next and current.next.data < new_node.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node
        return sorted_head

# Приклад використання
llist1 = LinkedList()
llist1.insert_at_end(3)
llist1.insert_at_end(1)
llist1.insert_at_end(4)
llist1.insert_at_end(2)

print("Оригінальний список:")
llist1.print_list()

llist1.reverse()
print("Реверсований список:")
llist1.print_list()

llist1.insertion_sort()
print("Відсортований список:")
llist1.print_list()

llist2 = LinkedList()
llist2.insert_at_end(0)
llist2.insert_at_end(5)
llist2.insert_at_end(6)

merged = llist1.merge_sorted(llist2)
print("Об'єднаний відсортований список:")
merged.print_list()
