# Pilhas são praticamentes listas no Python 
# Seguindo o estilo LIFO (Last-in First-out) eles possuem apenas 2 funções 
# append() -> Coloca um elemento no final da lista/pilha
# pop() -> Retira o ultimo elemento da lista/pilha

# Pilha vazia
pilha = [] 
# Adiciona elemento no final da pilha
pilha.append(4) 
pilha.append(3)
pilha.append(5)
pilha.append(6)  
# Printa o elemento
print(pilha)
# Retira o último elemento da pilha
pilha.pop()
pilha.pop()
pilha.pop()
print(pilha)
