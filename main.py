from trabalho1 import *


def main():

    #n = input("Numero de origens: ")
    #m = input("Numero de destinos: ")

    p = Problema()
    p.matriz_coeficientes = [[1,2,3,4],[4,3,2,4],[0,2,2,1]]
    p.matriz_x = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    p.l_oferta = [6,8,10]
    p.l_demanda = [4,7,6,7]

    #Teste balanceamento coluna OK
    #p.matriz_coeficientes = [[1,2,3],[4,3,2],[0,2,2]]
    #p.matriz_x = [[0,0,0],[0,0,0],[0,0,0]]
    #p.l_demanda = [4,7,6]

    #Teste balanceamento linha OK
    #p.matriz_coeficientes = [[1,2,3,4],[4,3,2,4]]
    #p.matriz_x = [[0,0,0,0],[0,0,0,0]]
    #p.l_oferta = [6,8]

    '''print "Ofertas:"
    p.l_oferta = le_dados(n)
    print "Demandas:"
    p.l_demanda = le_dados(m)
    print "Matriz de coeficientes:"
    p.matriz_coeficientes = le_matriz(n,m)
    print "Matriz de variaveis x"
    p.matriz_x = le_matriz(n,m)'''

    mostra_quadro(p)
    balanceamento(p)
    mostra_quadro(p)

main()
