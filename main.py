from trabalho1 import *

def main():

    #n = input("Numero de origens: ")
    #m = input("Numero de destinos: ")
    '''
    p = Problema()
    p.matriz_coeficientes = [[1,2,3,4],[4,3,2,4],[0,2,2,1]]
    p.matriz_x = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    p.l_oferta = [6,8,10]
    p.l_demanda = [4,7,6,7]
    '''

    #Teste 2
    '''
    p = Problema()
    p.matriz_coeficientes = [[40,45,999,999],[55,30,999,999],[999,35,999,999],[0,25,30,40],[25,0,40,35]]
    p.matriz_x = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    p.l_oferta = [300,220,400,920,920]
    p.l_demanda = [920,920,400,520]
    '''

    '''
    p = Problema()
    p.matriz_coeficientes = [[5,2,7,4],[3,6,6,3],[6,1,2,4],[4,3,6,6]]
    p.matriz_x = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    p.l_oferta = [80,30,60,45]
    p.l_demanda = [70,40,70,35]
    '''

    #p = Problema()
    #p.matriz_coeficientes = [[6,5,8],[13,12,1],[7,9,5],[10,6,4]]
    #p.matriz_x = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    #p.l_oferta = [10,20,12,13]
    #p.l_demanda = [8,32,15]




    #Teste balanceamento coluna OK
    #p.matriz_coeficientes = [[1,2,3],[4,3,2],[0,2,2]]
    #p.matriz_x = [[0,0,0],[0,0,0],[0,0,0]]
    #p.l_demanda = [4,7,6]

    #Teste balanceamento linha OK
    #p.matriz_coeficientes = [[1,2,3,4],[4,3,2,4]]
    #p.matriz_x = [[0,0,0,0],[0,0,0,0]]
    #p.l_oferta = [6,8]

    """print "Ofertas:"
    p.l_oferta = le_dados(n)
    print "Demandas:"
    p.l_demanda = le_dados(m)
    print "Matriz de coeficientes:"
    p.matriz_coeficientes = le_matriz(n,m)
    print "Matriz de variaveis x"
    p.matriz_x = le_matriz(n,m)
    """

    #mostra_quadro(p)

    #mostra_quadro(p)
    #Teste canto noroeste OK



    #Teste otimalidade OK

    #coordenada = []
    #criteriodeotimalidade(p,uv,coordenada)

    #otimalidade(p,lista)
    #mostra_quadro(p)

    '''
    p = Problema ()
    p.matriz_coeficientes = [[2, 3, 4, 5, 0], [3, 2, 5, 2, 0], [4, 1, 2, 3, 0]]
    p.matriz_x = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    p.l_oferta = [15, 20, 25]
    p.l_demanda = [8, 10, 12, 15, 15]
    lista = []
    balanceamento(p)
    variaveisbasicas = []
    print (p.matriz_coeficientes)
    cantonoroeste(p,variaveisbasicas)
    corrige(p,lista)
    mostra_quadro(p)
    print (p.matriz_x)
    uv = derivauv(p)
    print "uv calculado",uv
    print ("coordenada")
    print (p.matriz_x)
    '''

    problema = Problema()



    while(True):

        print("1- Inserir problema\n")
        print("2- Rodar exemplos\n")
        print("3- Sair\n")
        n = int(input())

        if n == 1:


            numeroofertas = int(input("Digite o número de ofertars: "))
            numerodemandas = int(input("Digite o número de demandas: "))
            numerodetransbordos = int(input("Digite o número de transbordos: "))

            while(numeroofertas < 0 and numerodemandas < 0):
                numeroofertas = int(input("Digite o número de ofertars: "))
                numerodemandas = int(input("Digite o número de demandas: "))
                numerodetransbordos = int(input("Digite o número de transbordos: "))

            problema.matriz_coeficientes = [[0 for j in range(numerodemandas+numerodetransbordos)]for i in range(numeroofertas+numerodetransbordos)]
            problema.matriz_x = [[0 for j in range(numerodemandas+numerodetransbordos)]for i in range(numeroofertas+numerodetransbordos)]

            for i in range(numeroofertas):
                print("\nEntre com o valor da oferta",i,": ")
                problema.l_oferta.append(float(input()))

            for i in range(numerodemandas):
                print("\nEntre com o valor da demanda",i,": ")
                problema.l_demanda.append(float(input()))

            balanceamento(problema)

            soma = 0
            for i in problema.l_demanda:
                soma = soma + i

            for i in range(numerodetransbordos):
                problema.l_demanda.insert(0,soma)
                problema.l_oferta.append(soma)

            M = soma * 2

            print(problema.l_demanda)
            print(problema.l_oferta)
            print(problema.matriz_x)

            for i in range(numeroofertas+numerodetransbordos):
                for j in range(numerodemandas+numerodetransbordos):
                    print("\nPara celulás que não possuam valores digite M")
                    print("\nEntre com os custos da posição",i," ",j," : ")
                    aux = input()

                    if aux == "M" or aux == "m":
                        problema.matriz_coeficientes[i][j] = M
                    else:
                        problema.matriz_coeficientes[i][j] = float(aux)

            lista = []

            print(problema.l_demanda)
            print(problema.l_oferta)
            print(problema.matriz_x)
            print("\nExecutando cantonoroeste...")
            cantonoroeste(problema,lista)
            corrige(problema,lista)

            otimalidade(problema,lista)

            mostraresultado(problema)


            sair = 0
            while(sair != 1):
                sair = int(input("Você deseja sair: 1-Sim 0-Não "))
                if sair == 1:
                    n = 0

        elif n == 2:
            print("\n---------------------------------------\n")
            p1 = Problema()
            p1.matriz_coeficientes = [[40, 45, 999, 999], [55, 30, 999, 999], [999, 35, 999, 999], [0, 25, 30, 40], [25, 0, 40, 35]]
            p1.matriz_x = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
            p1.l_oferta = [300, 220, 400, 920, 920]
            p1.l_demanda = [920, 920, 400, 520]

            lista1 = []
            cantonoroeste(p1, lista1)
            corrige(p1,lista1)
            otimalidade(p1,lista1)
            #print (p1.matriz_x)


            print("\nP1")
            mostraresultado(p1)

            print("\n---------------------------------------\n")
            p2 = Problema()
            p2.matriz_coeficientes = [[1,2,3,4],[4,3,2,4],[0,2,2,1]]
            p2.matriz_x =[[4,2,0,0],[0,5,3,0],[0,0,3,7]]
            p2.l_demanda = [4,7,6,7]
            p2.l_oferta = [6,8,10]

            lista2 = []
            cantonoroeste(p2, lista2)
            corrige(p2,lista2)
            otimalidade(p2,lista2)

            #print (p2.matriz_x)

            print("\nP2")

            mostraresultado(p2)
            print("\n---------------------------------------\n")
            p = Problema ()
            p.matriz_coeficientes = [[2, 3, 4, 5, 0], [3, 2, 5, 2, 0], [4, 1, 2, 3, 0]]
            p.matriz_x = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
            p.l_oferta = [15, 20, 25]
            p.l_demanda = [8, 10, 12, 15, 15]


            lista = []
            cantonoroeste(p, lista)
            teste = []
            corrige(p,lista)

            otimalidade(p,lista)


            print("\nP")
            mostraresultado(p)

            #print (p.matriz_x)


        else:

            break






main()
