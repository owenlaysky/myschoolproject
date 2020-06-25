1006#
"""
A = float(input())
B = float(input())
C = float(input())

media = (A/10*2)+(B/10*2)+(C/10*2);
print("MEDIA = %.5f" %media)
"""
"""
1007#
a= int(input())
b= int(input())
c= int(input())
d= int(input())

difference=((a * b) - (c * d))

print("DIFERENCA = %d" %difference)
"""
"""
1008#
number = int(input())
jamkerja = int(input())
uang = float(input())

gaji = float(jamkerja * uang)

print("NUMBER = %d" %number)
print("SALARY = U$ %0.2f" %gaji)
"""
"""
1009#
name = input()
gaji = float(input())
totaljual = float(input())

bonus = float(totaljual * (15/100))

total = gaji + bonus

print("TOTAL = R$ %0.2f" %total)
"""
"""
1010#
a,b,c = input().split()
a = int(a)
b = int(b)
c = float(c)

d,e,f = input().split()
d = int(d)
e = int(e)
f = float(f)

res = (b*c)+(e*f)
print("VALOR A PAGAR: R$ %.2f" % (res))
"""
"""
1011#
pi = 3.14159
r = float(input())
VOLUME = (4/3)*pi*r**3
print("VOLUME = %.3f" %VOLUME)
"""
"""
1012#
valor = input().split(" ")

a, b, c = valor
pi = 3.14159

triangulo = (float(a) * float(c))/2
circulo = pi * (float(c)* float(c))
trapezio = float(c) *(float(a) + float(b)) / 2
quadrado = float(b) * float(b)
retangulo = float(a) * float(b)


print("TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f" % (triangulo, circulo, trapezio, quadrado, retangulo))
"""
1018#
uangkertas = [100,50,20,10,5,2,1]
uangkamu = int(input)
for uang in uangkertas :
	print (uang)