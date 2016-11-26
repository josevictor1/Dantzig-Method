
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

    while (not (verifica(problema.l_oferta) and verifica(problema.l_demanda))):
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

def transformalista(mariz):

    l = []

    for i in matriz:
        for j in i:
            l.append(matriz)

    return l

def montasistema(lista1):

    l = []

    for i in lista1:
        if i != 0:
            l.append(lista1.index(i))

    return l

def contaelementos(lista):
    n = 0
    for i in lista:
        if i != 0:
            n = n + 1

    return n

def linhaalocada(matriz):

    maior = 0
    linha = 0

    for i in range(len(matriz)):
        if maior < contaelementos(matriz[i]):
            maior = contaelementos(matriz[i])
            linha = i

    return linha

def derivauv(problema):

    uv = []
    u = [1.1 for i in range(len(problema.l_oferta))]
    v = [1.1 for i in range(len(problema.l_demanda))]

    intervalo = len(problema.l_demanda)

    linha = linhaalocada(problema.matriz_x)

    u[linha] = 0

    for i in range(len(problema.matriz_x[linha])):
        if problema.matriz_x[linha][i] != 0:
            v[i] = u[linha] + problema.matriz_coeficientes[linha][i]

    for i in range(len(problema.matriz_coeficientes)):
        for j in range(intervalo):
            if problema.matriz_x[i][j] != 0:
                if u[i] == 1.1 and v[j] != 1.1:
                    u[i] = problema.matriz_coeficientes[i][j] - v[j]
                elif u[i] != 1.1 and v[j] == 1.1:
                    v[j] = problema.matriz_coeficientes[i][j] - u[i]

    uv.append(u)
    uv.append(v)

    return uv

def criteriodeotimalidade(problema,uv):

    menor = 0
    co = 0
    x = 0
    y = 0

    for i in range(len(problema.matriz_coeficientes)):
        for j in range(len(problema.matriz_coeficientes[0])):
            co = problema.matriz_coeficientes[i][j] - uv[0][i] - uv[1][j]
            if problema.matriz_x[i][j] == 0 and (co < 0):
                if co < menor:
                    menor = co
                    x = i
                    y = j

    if menor == 0:
        return False
    else:
        problema.matriz_x[x][y] = menor
        return True








