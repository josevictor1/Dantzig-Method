
class Problema(object):

    def __init__(self):
        self.matriz_coeficientes = []
        self.matriz_x = []
        self.l_oferta = []
        self.l_demanda = []

def copiamatriz(mat):
    mat1 = []
    for i in mat:
        mat1.append(i[:])

    return mat1

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
    demanda = problema.l_demanda[:]
    oferta = problema.l_oferta[:]

    while (not (verifica(oferta) and verifica(demanda))):
        if oferta[linha] < demanda[coluna]:
            problema.matriz_x[linha][coluna] = oferta[linha]
            demanda[coluna] = demanda[coluna] - oferta[linha]
            oferta[linha] = 0
            linha = linha + 1
        elif oferta[linha] > demanda[coluna]:
            problema.matriz_x[linha][coluna] = demanda[coluna]
            oferta[linha] = oferta[linha] - demanda[coluna]
            demanda[coluna] = 0
            coluna = coluna + 1
        else:
            problema.matriz_x[linha][coluna] = demanda[coluna]
            oferta[linha] = 0
            demanda[coluna] = 0
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

def criteriodeotimalidade(problema,uv,coordenada):

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

    if menor >= 0:
        return True
    else:
        coordenada.append(x)
        coordenada.append(y)
        return False

def verificasomalinha(linha,resultante):

    soma = 0

    for i in linha:
        soma = soma + i

    if soma == resultante:
        return True
    else:
        return False

def verificasomacoluna(matriz,resultante,coluna):

    soma = 0

    for i in range(len(matriz)):
        soma = soma + matriz[i][coluna]

    if soma == resultante:
        return True
    else:
        return False

def encontraproximocoluna(matriz,inicial):

    menor = 0

    for i in range(len(matriz)):
        if matriz[i][inicial[1]] != 0 and i != inicial[0]:
            if menor == 0:
                menor = i
            elif abs(inicial[0] - i) < abs(inicial[0] - menor):
                menor = i

    return menor

def encontraproximolinha(linha,inicial):

    menor  = 0

    for i in range(len(linha)):
        if linha[i] != 0 and i != inicial[1]:
            if menor == 0:
                menor = i
            elif abs(inicial[1] - i) < abs(inicial[1] - menor):
                menor  = i

    return menor

def otimalidade(problema):

    uv = []
    inicial = []
    atual = []

    while(True):

        uv = derivauv(problema)

        if criteriodeotimalidade(problema,uv,inicial):
            return problema
        else:
            copia = copiamatriz(problema.matriz_x)
            copia[inicial[0]][inicial[1]] = 1
            menor = [0,0]
            atual = inicial[:]
            subtrai = []
            soma = []

            flag = True

            while flag:
                if not verificasomacoluna(copia,problema.l_demanda[atual[1]],atual[1]):

                    atual[0] = encontraproximocoluna(copia,atual)

                    if subtrai != [] and problema.matriz_x[menor[0]][menor[1]] > problema.matriz_x[atual[0]][atual[1]]:
                        menor = atual[:]

                    subtrai.append([atual[0],atual[1]])
                    copia[atual[0]][atual[1]] = copia[atual[0]][atual[1]] - 1

                elif not verificasomalinha(copia[atual[0]],problema.l_oferta[inicial[0]]):
                    atual[1] = encontraproximolinha(copia,atual)
                    soma.append([atual[0],atual[1]])
                    copia[atual[0]][atual[1]] = copia[atual[0]][atual[1]] + 1

                else:
                    flag = False

                    for i in soma:
                        problema.matriz_x[i[0]][i[1]] = problema.matriz_x[i[0]][i[1]] + problema.matriz_x[menor[0]][menor[1]]

                    subtrai.remove(menor)
                    for i in subtrai:
                        problema.matriz_x[i[0]][i[1]] = problema.matriz_x[i[0]][i[1]] - problema.matriz_x[menor[0]][menor[1]]

                    problema.matriz_x[inicial[0]][inicial[1]] = problema.matriz_x[menor[0]][menor[1]]
                    problema.matriz_x[menor[0]][menor[1]] = 0
