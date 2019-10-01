import math

print('Teniendo en cuenta la ecuacion del tipo ax^2+bx+c:')
print('----------------------------------------')
a=int(input('Introduce el valor de a: '))
b=int(input('Introduce el valor de b: '))
c=int(input('Introduce el valor de c: '))

#Calculamos el discriminante

d=(b*b)-4*a*c

#Comprobamos y calculamos

if d<0:
    print('No existen soluciones reales')
else:
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print('----Soluciones----')
    print "Solucion x1: "+x1
    print "Solucion x2: "+x2
