#import gc

class No:
    def __init__(self, v):
        self.valor = v
        self.esq = None
        self.dir = None

class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, r, n):
        if self.raiz == None:
            self.raiz = n
        elif n.valor <= r.valor:
            if r.esq == None:
                r.esq = n
            else:
                self.inserir(r.esq, n)
        else:
            if r.dir == None:
                r.dir = n
            else: 
                self.inserir(r.dir, n)
    def preordem(self, r):
        if r:
            print(r.valor)
            self.preordem(r.esq)
            self.preordem(r.dir)



def main():
    a = Arvore()
    a.inserir(a.raiz, No(10))
    a.inserir(a.raiz, No(5))
    a.inserir(a.raiz, No(3))
    a.inserir(a.raiz, No(1))
    a.inserir(a.raiz, No(4))
    a.inserir(a.raiz, No(2))

    a.preordem(a.raiz)



if __name__ == "__main__":
    main()











