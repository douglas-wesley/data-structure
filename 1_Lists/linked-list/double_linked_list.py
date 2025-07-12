class NoDuplo:
    """Nó para lista duplamente encadeada"""
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None

class ListaDuplamenteEncadeada:
    """
    Lista Duplamente Encadeada:
    - Cada nó tem ponteiro para próximo E anterior
    - Navegação bidirecional (frente e trás)
    - Permite inserção/remoção eficiente em qualquer posição
    """
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0
    
    def inserir_inicio(self, dado):
        """Insere elemento no início"""
        novo_no = NoDuplo(dado)
        if not self.cabeca:
            self.cabeca = self.cauda = novo_no
        else:
            novo_no.proximo = self.cabeca
            self.cabeca.anterior = novo_no
            self.cabeca = novo_no
        self.tamanho += 1
    
    def inserir_fim(self, dado):
        """Insere elemento no final"""
        novo_no = NoDuplo(dado)
        if not self.cauda:
            self.cabeca = self.cauda = novo_no
        else:
            self.cauda.proximo = novo_no
            novo_no.anterior = self.cauda
            self.cauda = novo_no
        self.tamanho += 1
    
    def inserir_posicao(self, dado, posicao):
        """Insere elemento em posição específica"""
        if posicao <= 0:
            self.inserir_inicio(dado)
            return
        if posicao >= self.tamanho:
            self.inserir_fim(dado)
            return
        
        novo_no = NoDuplo(dado)
        atual = self.cabeca
        for i in range(posicao):
            atual = atual.proximo
        
        novo_no.anterior = atual.anterior
        novo_no.proximo = atual
        atual.anterior.proximo = novo_no
        atual.anterior = novo_no
        self.tamanho += 1
    
    def remover(self, dado):
        """Remove primeira ocorrência do elemento"""
        atual = self.cabeca
        while atual and atual.dado != dado:
            atual = atual.proximo
        
        if not atual:
            return False
        
        if atual.anterior:
            atual.anterior.proximo = atual.proximo
        else:
            self.cabeca = atual.proximo
        
        if atual.proximo:
            atual.proximo.anterior = atual.anterior
        else:
            self.cauda = atual.anterior
        
        self.tamanho -= 1
        return True
    
    def exibir_frente(self):
        """Exibe elementos da frente para trás"""
        elementos = []
        atual = self.cabeca
        while atual:
            elementos.append(atual.dado)
            atual = atual.proximo
        return elementos
    
    def exibir_tras(self):
        """Exibe elementos de trás para frente"""
        elementos = []
        atual = self.cauda
        while atual:
            elementos.append(atual.dado)
            atual = atual.anterior
        return elementos


if __name__ == "__main__":
    print("2. LISTA DUPLAMENTE ENCADEADA:")
    lista_dupla = ListaDuplamenteEncadeada()
    lista_dupla.inserir_inicio(100)
    lista_dupla.inserir_fim(200)
    lista_dupla.inserir_posicao(150, 1)
    print(f"Lista (frente): {lista_dupla.exibir_frente()}")
    print(f"Lista (trás): {lista_dupla.exibir_tras()}")
    lista_dupla.remover(150)
    print(f"Após remover 150: {lista_dupla.exibir_frente()}")
    print(f"Tamanho: {lista_dupla.tamanho}\n")