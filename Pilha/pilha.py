#import gc

class No:
    def __init__(self, v):
        self.valor = v
        self.prox = None

class Pilha:
    def __init__(self):
        self.topo = None

    def imprimir(self):
        if self.topo == None:
            print("Pilha vazia")
        else:
            print("Imprimindo pilha:")
            temp = self.topo
            while temp != None:
                print(temp.valor)
                temp = temp.prox

    def empilhar(self, n):
        if self.topo == None:
            self.topo = n
        else:
            n.prox = self.topo
            self.topo = n

    def desempilhar(self):
        if self.topo == None:
            print("Erro: Pilha vazia")
        else:
            temp = self.topo
            self.topo = temp.prox
            del temp #garbage collector
            #gc.collect()


def main():
    p = Pilha()
    p.imprimir()
    p.empilhar(No(10))
    p.empilhar(No(100))
    p.empilhar(No(1000))
    p.imprimir()
    p.desempilhar()
    p.imprimir()
    p.empilhar(No(5))
    p.imprimir()


if __name__ == "__main__":
    main()











