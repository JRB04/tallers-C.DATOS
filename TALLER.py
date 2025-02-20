numeros=[]
repetido=[]
print("cuantos numeros desea ingresar")

n=int(input())
i= 0
while i < n:
		print("valor numero", i + 1)
		valor= int(input())
		numeros.append(valor)
		i += 1
promedio = sum(numeros) / len(numeros)
print("el promedio es: ",promedio)
for i in range(len(numeros)):
	for  repetidos in range(len(numeros)):
				if i != repetidos:
					if numeros[i] == numeros[repetidos]:
						if numeros[i] not in repetido:
							repetido.append(numeros[i])
print("numero repetido: ", repetido)
			