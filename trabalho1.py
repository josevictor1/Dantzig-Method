
class Problema(object):

    def __init__(self):
        self.matriz_coeficientes = []
        self.matriz_x = []
        self.l_oferta = []
        self.l_demanda = []

def le_dados(n):

    l = []
    for i in range(n):
        i = input()
        l.append(i)

    return l

def le_matriz(n,m):

    mat = []
    for i in range(n):
        l = []
        for j in range(m):
          l.append(input())
        mat.append(l)

    return mat

def verifica_balanceamento(lista_demanda,lista_oferta):

    demanda = 0
    oferta = 0

    for i in lista_demanda:
        demanda = demanda + i
    for i in lista_oferta:
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

def balanceamento(problema):

    verifica = verifica_balanceamento(problema.l_demanda,problema.l_oferta)

    if verifica == "balanceado":
        print "Problema balanceado"
    elif verifica == "oferta desbalanceada":
        adiciona_linha(problema.matriz_coeficientes)
        adiciona_linha(problema.matriz_x)
    else:
        adiciona_coluna(problema.matriz_coeficientes)
        adiciona_coluna(problema.matriz_x)

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

def mostra_quadro(problema):

    print"                       "

    for i in range(len(problema.l_demanda)):
        print "         ",
        print i,
        print "       ",

    print "       Oferta"

    for i in range(len(problema.l_oferta)):
        print  "         |",
        for j in range(len(problema.l_demanda)):
            print "x =",problema.matriz_x[i][j]," " ,"c = ",problema.matriz_coeficientes[i][j],"|",
        print "       ",problema.l_oferta[i]

    print"Demanda",
    print " |",

    for i in problema.l_demanda:
        print "      ",
        print i,
        print "      |",


