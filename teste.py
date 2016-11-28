from trabalho1 import *

p = Problema()

p.matriz_coeficientes = [[1,2,3,4],[4,3,2,4],[0,2,2,1]]
p.matriz_x =[[4,2,0,0],[0,5,3,0],[0,0,3,7]]
p.l_demanda = [4,7,6,7]
p.l_oferta = [6,8,10]

'''
uv = derivauv(p)
print uv
if criteriodeotimalidade(p,uv):
    print p.matriz_x
'''
cantonoroeste(p)
print "demanda" ,p.l_demanda

print p.matriz_x
otimalidade(p)

print p.matriz_x
