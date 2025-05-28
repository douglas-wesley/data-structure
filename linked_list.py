class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None
#   | data | next | -> |data|next|
#   head -> None 
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def display(self):
        current_node = self.head
        if not current_node:
            print("A lista está vazia")
            return 
        print("Sua lista:")
        while current_node:
            print(current_node.data)
            current_node = current_node.next



if __name__ == '__main__':
    my_shopping_list = LinkedList()

# Verificando se a lista está vazia inicialmente
    my_shopping_list.display()

# Adicionando alguns itens
    my_shopping_list.append("Maçãs")
    my_shopping_list.append("Leite")
    my_shopping_list.append("Pão")
    my_shopping_list.append("Ovos")

# Exibindo a lista de compras atualizada
    my_shopping_list.display()

    print("\n--- Adicionando mais um item ---")
    my_shopping_list.append("Cenouras")
    my_shopping_list.display()

