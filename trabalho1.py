
n = input("Numero de origens: ")
m = input("Numero de destinos: ")
e = input("Numero de entrepostos: ")

class Problema(object):

    def _init_(sefl,matriz_coeficientes,matriz_x,l_oferta,l_demanda):
        self.matriz_coeficientes = matriz_coeficientes
        self.matriz_x = matriz_x
        self.l_oferta = l_oferta
        self.l_demanda = l_demanda



def le_dadosorigem(n):

    l = []
    for i in range(n):
        i = input()
        l.append(i)
    return l

def le_dadosdestino(m):

    l = []
    for i in range(n):
        i = input()
        l.append()
    return l

def le_matriz_coeficientes(matriz_coeficientes):

    for i in matriz_coeficientes:
        i = input()
    return matriz_coeficientes

def verifica_balanceamento(lista_demanda,lista_oferta):

    demanda = 0
    oferta = 0

    for i in lista_demanda:
        demanda = demanda + i
    for i in lista_origem:
        oferta = oferta + i

    if demanda == oferta:
        return "balanceado"
    elif demanda > oferta:
        lista_oferta.append(demanda - oferta)
        return "oferta desbalanceada"
    else:
        lista_demanda.append(oferta - demanda)
        return "demanda desbalanceado"


def adiciona_linha(matriz_coeficientes):

    l = []
    l = [0 for i in range(len(matriz_coeficientes[0]))]
    matriz_coeficientes.append(l)


def adiciona_coluna(matriz_coeficientes):

    for i in matriz_coeficientes:
        i.append(0)



def balanceamento(lista_demanda,lista_oferta,matriz_coeficientes):

    verifica = verifica_balanceamento(lista_demanda,lista_oferta)

    if verifica == "balanceado":
        print "Problema balanceado"
    elif verifica == "oferta desbalanceada":
        adiciona_linha(matriz_coeficientes)
    else:
        adiciona_coluna(matriz_coeficientes)

def verifica(l):
    for i in l:
        if i != 0:
            return False
    return True



def cantonoroeste(problema):
    linha = 0
    coluna = 0
    while(verifica(problema.l_oferta) and verifica(l_demanda)):
        if problema.l_oferta[linha] < problema.l_demanda[coluna]:
            problema.matriz_x[linha][coluna] = problema.l_oferta[linha]
            problema.l_demanda[coluna] = problema.l_demanda[coluna] - problema.l_oferta[linha]
            problema.l_oferta[linha] = 0
            linha = linha + 1
        elif problema.l_oferta[linha] > problema.l_demanda[coluna]:
            problema.matriz_x[linha][coluna] = problema.l_demanda[coluna]
            problema.l_oferta[linha] = problema.l_oferta[linha] - problema.l_demanda[coluna]
            problema.l_demanda[coluna] = 0
            coluna = coluna + 1
        else:
            problema.matriz_x[linha][coluna] = problema.l_demanda[coluna]
            problema.l_oferta[linha] = 0
            problema.l_demanda[coluna] = 0
            coluna = coluna + 1
            linha = linha + 1




