#Taller 1 
#Punto 6

print("ingrese valor")
n = int(input())
print("ingreso: ",n)
contador = 0
while n>0:
	d = n % 2 #residuo
	n = n // 2 #cociente
	contador = contador + 2 #suma el numero de operaciones por cada iteracion
	print(d)

print("Numero de operaciones T(n)=",contador)
print("El algoritmo es O(n)")
