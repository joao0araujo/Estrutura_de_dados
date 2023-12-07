class Elemento:
    def __init__(self, v):
        self.valor = v
        self.prox = None

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tam = 0

    def imprimir(self):
        if self.inicio == None:
            print("Fila vazia")
        else:
            print("Imprimindo fila:")
            temp = self.inicio
            while temp != None:
                print(temp.valor)
                temp = temp.prox

    def enfileirar(self, n):
        if self.inicio == None:
            self.inicio = n
            self.tam += 1
        else:
            temp = self.inicio
            while temp.prox:
                temp = temp.prox
            temp.prox = n
            self.tam += 1

    def desenfileirar(self):
        if self.inicio:
            temp = self.inicio
            self.inicio = temp.prox
            return temp

def main():

    f = Fila()
    f.enfileirar(Elemento(10))
    f.enfileirar(Elemento(20))
    f.enfileirar(Elemento(30))
    f.imprimir()

    f.desenfileirar()
    f.imprimir()



if __name__ == "__main__":
    main()











