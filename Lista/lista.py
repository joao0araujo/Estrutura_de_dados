class No:
    def __init__(self, v):
        self.valor = v
        self.prox = None

    def imprimir(self):
        return(f"Valor: {self.valor}")

class Lista:
    def __init__(self):
        self.inicio = None

    def imprimir(self):
        if self.inicio == None:
            print("Lista vazia")
        else:
            # print("Imprimindo lista:")
            temp = self.inicio
            while temp != None:
                print(temp.imprimir())
                temp = temp.prox

    def inserir(self, n):
        if self.inicio == None:
            self.inicio = n
        else:
            n.prox = self.inicio
            self.inicio = n

    def remover(self):
        if self.inicio == None:
            print("Erro: Lista vazia")
        else:
            temp = self.inicio
            self.inicio = temp.prox
            del temp #garbage collector
            #gc.collect()


def main():
    l = Lista()
    l.remover()
    l.imprimir()
    l.inserir(No(10))
    l.inserir(No(100))
    l.inserir(No(1000))
    l.imprimir()
    l.remover()
    l.imprimir()
    l.inserir(No(5))
    l.imprimir()


if __name__ == "__main__":
    main()











