from trabalho1 import *

'''
p = Problema()
p.matriz_coeficientes = [[1,2,3,4],[4,3,2,4],[0,2,2,1]]
p.matriz_x =[[4,2,0,0],[0,5,3,0],[0,0,3,7]]
p.l_demanda = [4,7,6,7]
p.l_oferta = [6,8,10]
'''

'''
uv = derivauv(p)
print uv
 if criteriodeotimalidade(p,uv):
    print p.matriz_x
'''

'''
p = Problema()
p.matriz_coeficientes = [[40, 45, 999, 999], [55, 30, 999, 999], [999, 35, 999, 999], [0, 25, 30, 40], [25, 0, 40, 35]]
p.matriz_x = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
p.l_oferta = [300, 220, 400, 920, 920]
p.l_demanda = [920, 920, 400, 520]
'''
#[[2, 1], [2, 0], [3, 0], [3, 1]]

p1 = Problema()
p1.matriz_coeficientes = [[40, 45, 999, 999], [55, 30, 999, 999], [999, 35, 999, 999], [0, 25, 30, 40], [25, 0, 40, 35]]
p1.matriz_x = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
p1.l_oferta = [300, 220, 400, 920, 920]
p1.l_demanda = [920, 920, 400, 520]

lista1 = []
cantonoroeste(p1, lista1)
#print(p1.matriz_x)
corrige(p1,lista1)
otimalidade(p1,lista1)
print (p1.matriz_x)


p2 = Problema()
p2.matriz_coeficientes = [[1,2,3,4],[4,3,2,4],[0,2,2,1]]
p2.matriz_x =[[4,2,0,0],[0,5,3,0],[0,0,3,7]]
p2.l_demanda = [4,7,6,7]
p2.l_oferta = [6,8,10]

lista2 = []
cantonoroeste(p2, lista2)
#print(p2.matriz_x)
corrige(p2,lista2)
otimalidade(p2,lista2)
print (p2.matriz_x)

p = Problema ()
p.matriz_coeficientes = [[2, 3, 4, 5, 0], [3, 2, 5, 2, 0], [4, 1, 2, 3, 0]]
p.matriz_x = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
p.l_oferta = [15, 20, 25]
p.l_demanda = [8, 10, 12, 15, 15]


lista = []
cantonoroeste(p, lista)
teste = []
#print(p.matriz_x)
#uv = []
#inicial = [0,0]
#pilha = []
corrige(p,lista)

for i in lista:
    print(p.matriz_x[i[0]][i[1]])
'''
uv = derivauv(p,lista)
criteriodeotimalidade(p,uv,inicial)
lista.append(inicial)
pilha = percorre_caminho(inicial,lista)
print pilha
'''
otimalidade(p,lista)

print (p.matriz_x)

print("P",verificacorretude(p))
print("P1",verificacorretude(p1))
print("P2",verificacorretude(p2))

'''
lista = []
cantonoroeste(p, lista)
teste = []
print(p.matriz_x)
corrige(p,lista)
for i in lista:
     print i
'''
#    print(p.matriz_x[i[0]][i[1]])
#otimalidade(p,lista)

'''
def corrige(problema,lista):

    n = 0

    for i in lista:
        n = n + 1
        if i[0] < (len(problema.matriz_x) - 1)  and i[1] < (len(problema.matriz_x[0]) - 1):
            if problema.matriz_x[i[0]][i[1] + 1] == 0 and problema.matriz_x[i[0] + 1][i[1]] == 0:
                lista.insert(n, [i[0] + 1, i[1]])
'''
'''


teste = derivauv(p,lista)

print teste
'''

'''
pilha = [1,2,3,4]
i = input()
empilha(i,pilha)
print pilha
desempilha(i,pilha)
print pilha
'''
