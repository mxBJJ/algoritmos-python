class No(object):

    def __init__(self, dado, anterior, proximo):
        self.dado = dado
        self.anterior = anterior
        self.proximo = proximo


class ListaDuplamenteEncadeada(object):

    cabeca = None
    rabo = None

    def acrescentar(self, dado):
        """ Acrescenta um novo no a lista. """
        novo_no = No(dado, None, None)

        if self.cabeca is None:
            self.cabeca = novo_no
            self.rabo = novo_no
        else:
            novo_no.anterior = self.rabo
            novo_no.proximo = None
            self.rabo.proximo = novo_no
            self.rabo = novo_no

    def remover(self, dado):
        """ Remove um no da lista. """
        no_atual = self.cabeca
        while no_atual is not None:
            if no_atual.dado == dado:
                if no_atual.anterior is None:
                    self.cabeca = no_atual.proximo
                    no_atual.proximo.anterior = None
                else:
                    no_atual.anterior.proximo = no_atual.proximo
                    no_atual.proximo.anterior = no_atual.anterior

            no_atual = no_atual.proximo

    def mostrar(self):

        print("Lista Duplamente Encadeada:\n")

        no_atual = self.cabeca

        no = ""

        while no_atual is not None:
            if no_atual.anterior is None:
                no += "None "
            no += "<---> | " + str(no_atual.dado) + " | "
            if no_atual.proximo is None:
                no += "<---> None"

            no_atual = no_atual.proximo
        print(no)
        print("="*80)


lista = ListaDuplamenteEncadeada()

lista.acrescentar(2)
lista.mostrar()
lista.acrescentar(5)
lista.mostrar()
lista.acrescentar(12)
lista.mostrar()
lista.acrescentar(20)
lista.mostrar()

lista.remover(12)
lista.mostrar()
lista.remover(5)
lista.mostrar()
