# Nó do Circular
class NoCircular:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaCircular:
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0
    
    # Insere elemento no início
    def inserir_inicio(self, dado):
        
        novo_no = NoCircular(dado)
        if not self.cabeca:
            self.cabeca = novo_no
            novo_no.proximo = novo_no  # Aponta para si mesmo
        else:
            # Encontra o último nó
            atual = self.cabeca
            while atual.proximo != self.cabeca:
                atual = atual.proximo
            
            novo_no.proximo = self.cabeca
            atual.proximo = novo_no
            self.cabeca = novo_no
        self.tamanho += 1
    
    # Insere elemento no final
    def inserir_fim(self, dado):
        novo_no = NoCircular(dado)
        if not self.cabeca:
            self.cabeca = novo_no
            novo_no.proximo = novo_no
        else:
            atual = self.cabeca
            while atual.proximo != self.cabeca:
                atual = atual.proximo
            
            atual.proximo = novo_no
            novo_no.proximo = self.cabeca
        self.tamanho += 1
    
    # Remove elemento
    def remover(self, dado):
        if not self.cabeca:
            return False
        
        # Se há apenas um elemento
        if self.cabeca.proximo == self.cabeca and self.cabeca.dado == dado:
            self.cabeca = None
            self.tamanho -= 1
            return True
        
        # Se o elemento a remover é a cabeça
        if self.cabeca.dado == dado:
            atual = self.cabeca
            while atual.proximo != self.cabeca:
                atual = atual.proximo
            atual.proximo = self.cabeca.proximo
            self.cabeca = self.cabeca.proximo
            self.tamanho -= 1
            return True
        
        # Procura o elemento na lista
        atual = self.cabeca
        while atual.proximo != self.cabeca and atual.proximo.dado != dado:
            atual = atual.proximo
        
        if atual.proximo.dado == dado:
            atual.proximo = atual.proximo.proximo
            self.tamanho -= 1
            return True
        return False
    # Exibe elementos da lista
    def exibir(self, voltas=1):
        if not self.cabeca:
            return []
        
        elementos = []
        atual = self.cabeca
        total_elementos = self.tamanho * voltas
        
        for i in range(total_elementos):
            elementos.append(atual.dado)
            atual = atual.proximo
        
        return elementos
        
    # Buscar elemento
    def buscar(self, dado):
        if not self.cabeca:
            return -1
        
        atual = self.cabeca
        posicao = 0
        
        while True:
            if atual.dado == dado:
                return posicao
            atual = atual.proximo
            posicao += 1
            
            if atual == self.cabeca:  # Completou uma volta
                break
        
        return -1

if __name__ == "__main__":
    print("3. LISTA CIRCULAR:")
    lista_circular = ListaCircular()
    lista_circular.inserir_fim(1)
    lista_circular.inserir_fim(2)
    lista_circular.inserir_fim(3)
    print(f"Lista (1 volta): {lista_circular.exibir(1)}")
    print(f"Lista (2 voltas): {lista_circular.exibir(2)}")
    print(f"Buscar 2: posição {lista_circular.buscar(2)}")
    lista_circular.remover(2)
    print(f"Após remover 2: {lista_circular.exibir(1)}")
    print(f"Tamanho: {lista_circular.tamanho}")