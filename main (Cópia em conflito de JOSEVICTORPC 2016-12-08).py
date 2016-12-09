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

    p = Problema ()
    p.matriz_coeficientes = [[2, 3, 4, 5, 0], [3, 2, 5, 2, 0], [4, 1, 2, 3, 0]]
    p.matriz_x = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    p.l_oferta = [15, 20, 25]
    p.l_demanda = [8, 10, 12, 15, 15]


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
    lista = []
    #mostra_quadro(p)
    balanceamento(p)
    #mostra_quadro(p)
    #Teste canto noroeste OK
    variaveisbasicas = []
    print (p.matriz_coeficientes)
    cantonoroeste(p,variaveisbasicas)
    corrige(p,lista)
    mostra_quadro(p)
    print (p.matriz_x)
    #Teste otimalidade OK
    #uv = derivauv(p)
    #coordenada = []
    #criteriodeotimalidade(p,uv,coordenada)
    #print "uv calculado",uv
    print ("coordenada")
    otimalidade(p,lista)
    #mostra_quadro(p)

    print (p.matriz_x)


main()
