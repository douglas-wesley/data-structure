class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#   | data | next | -> |data|next|
#   head -> None 
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data): # Dar uma revisada nisso depois
        new_node = Node(data)
        
        if self.head == None:
            self.head = new_node
            return

        current_node = self.head
        
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node
        return
    
    def lenght(self):
        if self.head == None:
            return 0

        current_node = self.head
        total = 0

        while current_node:
            current_node = current_node.next
            total += 1
        return total
    
    def get(self,index):
        if index >= self.lenght() or index < 0:
            return None
        current_idx = 0
        current_node = self.head

        while current_node != None:
            if index == current_idx:
                return current_node.data
            current_node = current_node.next
            current_idx += 1


    def to_list(self):
        node_data = []
        current_node = self.head

        while current_node:
            node_data.append(current_node.data)
            current_node = current_node.next
        return node_data

    def display(self):
        contents = self.head

        if contents is None:
            print("Lista está vazia")

        while contents:
            print(contents.data, end=' -> ')
            contents = contents.next
        print()
        print('---------')

    def reverse_linkedlist(self):
        previous_node = None
        current_node = self.head

        while current_node:
            next = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next
        self.head = previous_node


my_list = LinkedList()
my_list.display()

my_list.append(3)
my_list.append(7)
my_list.append(8)
my_list.append(6)

my_list.display()
print(f"Total de números é {str(my_list.lenght())}")
print(my_list.to_list())
print('---------')

my_list.reverse_linkedlist()
my_list.display()
