
class Problema(object):

    def __init__(self):
        self.matriz_coeficientes = []
        self.matriz_x = []
        self.l_oferta = []
        self.l_demanda = []

def imprime(matriz):
    for linha in matriz:
       for valor in linha:
           print("{:>6.2f}".format(valor), end=' ')
       print()

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

'''
def le_matriz(n,m):

    mat = []
    for i in range(n):
        l = []
        for j in range(m):
          l.append(input())
        mat.append(l)

    return mat
'''

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

    verifi = verifica_balanceamento(problema.l_demanda, problema.l_oferta)

    if verifi == "balanceado":
        print("Problema balanceado")
    elif verifi == "oferta desbalanceada":
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



def cantonoroeste(problema, lista):

    linha = 0
    coluna = 0

    print(problema.l_demanda)
    print(problema.l_oferta)

    demanda = problema.l_demanda[:]
    oferta = problema.l_oferta[:]

    while (not (verifica(oferta) and verifica(demanda))):
        if oferta[linha] < demanda[coluna]:
            problema.matriz_x[linha][coluna] = oferta[linha]
            lista.append([linha, coluna])
            demanda[coluna] = demanda[coluna] - oferta[linha]
            oferta[linha] = 0
            linha = linha + 1
        elif oferta[linha] > demanda[coluna]:
            problema.matriz_x[linha][coluna] = demanda[coluna]
            lista.append([linha, coluna])
            oferta[linha] = oferta[linha] - demanda[coluna]
            demanda[coluna] = 0
            coluna = coluna + 1
        else:
            problema.matriz_x[linha][coluna] = demanda[coluna]
            lista.append([linha, coluna])
            oferta[linha] = 0
            demanda[coluna] = 0
            coluna = coluna + 1
            linha = linha + 1


def corrige(problema,lista):

    n = 0

    for i in lista:
        n = n + 1
        if i[0] < (len(problema.matriz_x) - 1)  and i[1] < (len(problema.matriz_x[0]) - 1):
            if problema.matriz_x[i[0]][i[1] + 1] == 0 and problema.matriz_x[i[0] + 1][i[1]] == 0:
                lista.insert(n, [i[0], i[1] + 1])



'''
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
'''

def mostra_quadro(problema):

    print("                       ")

    for i in range(len(problema.l_demanda)):
        print("         "),
        print(i),
        print("       "),

    print("       Oferta")

    for i in range(len(problema.l_oferta)):
        print("         |"),
        for j in range(len(problema.l_demanda)):
            print("x =", problema.matriz_x[i][j], " ", "c = ", problema.matriz_coeficientes[i][j], "|"),
        print("       ", problema.l_oferta[i])

    print("Demanda"),
    print(" |"),

    for i in problema.l_demanda:
        print("      "),
        print(i),
        print("      |"),

    print(" ")


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

'''def linhaalocada(matriz):

    maior = 0
    linha = 0

    for i in range(len(matriz)):
        if maior < contaelementos(matriz[i]):
            maior = contaelementos(matriz[i])
            linha = i

    return linha
'''

def linhaalocada(lista):

    aux = []

    for i in lista:
        aux.append(i[0])

    maior = aux[0]

    for i in aux:
        if aux.count(i) > aux.count(maior):
            maior = i

    return maior

'''
def derivauv(problema,lista):

    uv = []
    u = [1.1 for i in range(len(problema.l_oferta))]
    v = [1.1 for i in range(len(problema.l_demanda))]

    intervalo = len(problema.l_demanda)

    #linha = linhaalocada(problema.matriz_x)
    linha = linhaalocada(lista)
    u[linha] = 0
    print("linha",linha)
    for i in range(len(problema.matriz_x[linha])):
        if [linha,i] in lista:
            v[i] = u[linha] + problema.matriz_coeficientes[linha][i]

    print(v)

    for i in range(len(problema.matriz_coeficientes)):
        for j in range(intervalo):
            if ([i,j] in lista):
                if u[i] == 1.1 and v[j] != 1.1:
                    u[i] = problema.matriz_coeficientes[i][j] - v[j]
                elif u[i] != 1.1 and v[j] == 1.1:
                    v[j] = problema.matriz_coeficientes[i][j] - u[i]

    uv.append(u)
    uv.append(v)

    return uv
'''
def derivauv(problema,lista):

    uv = []
    u = [1.1 for i in range(len(problema.l_oferta))]
    v = [1.1 for i in range(len(problema.l_demanda))]

    intervalo = len(problema.l_demanda)

    #linha = linhaalocada(problema.matriz_x)
    linha = linhaalocada(lista)
    u[linha] = 0
    #print "linha",linha
    for i in range(len(problema.matriz_x[linha])):
        if [linha,i] in lista:
            #print v[i]
            v[i] = u[linha] + problema.matriz_coeficientes[linha][i]


    while (1.1 in u) or (1.1 in v):
        #print "entrou"
        for i in lista:
            #print i
            if u[i[0]] == 1.1 and v[i[1]] != 1.1:

                u[i[0]] = problema.matriz_coeficientes[i[0]][i[1]] - v[i[1]]
                #print(u[i[0]],problema.matriz_coeficientes[i[0]][i[1]],"-",v[i[1]])

            elif u[i[0]] != 1.1 and v[i[1]] == 1.1:
                v[i[1]] = problema.matriz_coeficientes[i[0]][i[1]] - u[i[0]]
                #print(u[i[0]],problema.matriz_coeficientes[i[0]][i[1]],"-",v[i[1]])

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
        coordenada[0] = x
        coordenada[1] = y
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
                menor = i

    return menor

def retiramenor(problema,a,b,lista):

    soma1 = 0
    soma2 = 0

    for i in range(len(problema.matriz_x[0])):
        soma1 = soma1 + problema.matriz_x[a[0]][i]
        soma2 = soma2 + problema.matriz_x[b[0]][i]

    if soma1 > soma2:
        lista.remove(b)
        lista.append(a)
        return a
    else:
        lista.append(b)
        return b

def empilha(no,pilha):
    pilha.insert(0,no)

def desempilha(pilha):
    pilha.pop(0)

def topo(pilha):
    return pilha[0]

def proximo(lista,visitados,nodo,flag):

    #print lista
    for i in lista:
        #print i[flag]

        if (not (i in visitados)) and i[flag] == nodo:
                #print "visitados",i[flag]
                return i

        #print i
    return []



def percorre_caminho(origem,lista):

    pilha = []
    visitados = []
    flag = 1
    atual = [-1,-1]
    #print(atual)
    atual = proximo(lista, visitados, origem[flag], flag)
    #empilha(atual, pilha)
    #print("origem",origem)
    #print("atual", atual)
    while atual != origem:

        if flag == 1:
            flag = 0
        else:
            flag = 1

        if atual == []:
            #print(pilha)
            desempilha(pilha)
            if pilha == []:
                atual = proximo(lista, visitados, origem[flag], flag)
            else:
                atual = pilha[0]
            #atual = proximo(lista, visitados, atual[flag], flag)
        else:
            #print("nao retornou vazio")
            visitados.append(atual)
            empilha(atual, pilha)
            #print("pilha",pilha)
            #print("atual",atual)
            #atual = proximo(lista, visitados, atual[flag], flag)
            #print "novo atual", atual
        atual = proximo(lista, visitados, atual[flag], flag)
        #print 'visitadosAAAAAAAAAAAAAAAAAAAAAAAAAAAA',visitados
    empilha(atual,pilha)
    #print("PILHA",pilha)
    return pilha

def verificacorretude(problema):


    for i in range(len(problema.matriz_x)):
        soma = 0
        for j in range(len(problema.matriz_x[0])):
            soma = soma + problema.matriz_x[i][j]
        if soma != problema.l_oferta[i]:
            return False

    for i in range(len(problema.matriz_x[0])):
        soma = 0
        for j in range(len(problema.matriz_x)):
            soma = soma + problema.matriz_x[j][i]
        if soma != problema.l_demanda[i]:
            return False

    return True


def otimalidade(problema,lista):

    uv = []

    pilha = []

    while True:
        inicial = [0,0]
        uv = derivauv(problema,lista)

        if criteriodeotimalidade(problema,uv,inicial):
            return problema
        else:
            lista.append(inicial)
            pilha = percorre_caminho(inicial,lista)

            if pilha != []:
                subtrai = []
                soma = []

                for i in range(len(pilha)):
                    if i % 2 == 0:
                        soma.append(pilha[i])
                    else:
                        subtrai.append(pilha[i])

                menor = subtrai[0]

                for i in subtrai:
                    if problema.matriz_x[i[0]][i[1]] < problema.matriz_x[menor[0]][menor[1]]:
                        menor = i
                    elif problema.matriz_x[i[0]][i[1]] == problema.matriz_x[menor[0]][menor[1]] and problema.matriz_coeficientes[i[0]][i[1]] > problema.matriz_coeficientes[menor[0]][menor[1]]:
                        menor = i

                valormenor = problema.matriz_x[menor[0]][menor[1]]
                for i in soma:
                    problema.matriz_x[i[0]][i[1]] = problema.matriz_x[i[0]][i[1]] + valormenor

                for i in subtrai:
                    problema.matriz_x[i[0]][i[1]] = problema.matriz_x[i[0]][i[1]] - valormenor

                lista.remove(menor)



def mostraresultado(problema):

    print("\nMatriz Coeficientes:\n")
    imprime(problema.matriz_coeficientes)

    print("\n---------------------------------------\n")

    print ("\nMatriz X:\n")
    imprime(problema.matriz_x)

    resultado = 0

    for i in range(len(problema.matriz_x)):
        for j in range(len(problema.matriz_x[0])):

            if problema.matriz_x[i][j] != 0:
                resultado = resultado + (problema.matriz_x[i][j] * problema.matriz_coeficientes[i][j])

    print("\nResultado Z: ",resultado)





'''
def otimalidade(problema,lista):

    uv = []
    inicial = [0,0]
    atual = []

    segura = 0

    while True:

        uv = derivauv(problema,lista)
        print(uv)
        if segura > 3:
            break

        if criteriodeotimalidade(problema, uv, inicial):
            return problema
        else:
            copia = copiamatriz(problema.matriz_x)
            copia[inicial[0]][inicial[1]] = 1
            escolha = [0,0]
            atual = inicial[:]
            subtrai = []
            soma = []
            print("inicial", inicial,copia[inicial[0]][inicial[1]])
            flag = True

            while flag:
                #print "Iteracao", segura
                if not verificasomacoluna(copia, problema.l_demanda[atual[1]], atual[1]):
                    #print "verificou coluna"
                    atual[0] = encontraproximocoluna(copia, atual)

                    if subtrai != [] and problema.matriz_x[escolha[0]][escolha[1]] > problema.matriz_x[atual[0]][atual[1]]:
                        escolha[0] = atual[0]
                        escolha[1] = atual[1]

                    subtrai.append([atual[0], atual[1]])
                    copia[atual[0]][atual[1]] = copia[atual[0]][atual[1]] - 1

                elif not verificasomalinha(copia[atual[0]], problema.l_oferta[inicial[0]]):
                    #print "linha"
                    atual[1] = encontraproximolinha(copia, atual)
                    soma.append([atual[0], atual[1]])
                    copia[atual[0]][atual[1]] = copia[atual[0]][atual[1]] + 1

                else:
                    flag = False

                    print "Soma obtido", soma
                    print "Subtrai obtido",subtrai
                    for i in soma:
                        problema.matriz_x[i[0]][i[1]] = problema.matriz_x[i[0]][i[1]] + problema.matriz_x[escolha[0]][escolha[1]]

                    for i in subtrai:
                        if i == escolha and problema.matriz_x[escolha[0]][escolha[1]] == problema.matriz_x[i[0]][i[1]]:
                            escolha = retiramenor(problema,escolha,i,lista)

                    if escolha in subtrai:
                        subtrai.remove(escolha)

                    for i in subtrai:
                        problema.matriz_x[i[0]][i[1]] = problema.matriz_x[i[0]][i[1]] - problema.matriz_x[escolha[0]][escolha[1]]

                    problema.matriz_x[inicial[0]][inicial[1]] = problema.matriz_x[escolha[0]][escolha[1]]
                    problema.matriz_x[escolha[0]][escolha[1]] = 0
                    print"matriz resultante",problema.matriz_x
                    uv = derivauv(problema,lista)
                    print("UV ",uv)


        segura = segura + 1
'''
