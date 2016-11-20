
n = input("Numero de origens: ")
m = input("Numero de destinos: ")
e = input("Numero de entrepostos: ")

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
        i input()
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

def diferenca_coluna(matriz_coeficientes):

    primeiro_menor = 0
    segundo_menor = 0
    l =[]

    for i in range(2,len(matriz_coeficientes[0])):
        primeiro_menor = matriz_coeficientes[i][0]
        for j in range(len(matriz_coeficientes)):
            if primeiro_menor > matriz_coeficientes[j][i]:
                segundo_menor = primeiro_menor
                primeiro_menor = matriz_coeficientes[j][i]
            elif segundo_menor




def diferenca_linha(matriz_coeficientes):

    primeiro_menor = 0
    segundo_menor =
    l = []
    for i in range(len(matriz_coeficientes)):
        primeiro_menor = matriz_coeficientes[i][0]
        segundo_menor = primeiro_menor
        for j in range(2,len(matriz_coeficientes[0])):
            if primeiro_menor > matriz_coeficientes[i][j]:
                segundo_menor = primeiro_menor
                primeirto_menor = matriz_coeficientes[i][j]
            elif segundo_menor > matriz_coeficientes[i][j]:
                segundo_menor = matriz_coeficientes[i][j]
        l.append(segundo_menor - primeiro_menor)
    return l







