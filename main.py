import numpy
import sys

r1 = int(input("Numero de filas de la Matriz 1: "))
c1 = int(input("Numero de columnas de la Matriz 1: "))
r2 = int(input("Numero de filas de la Matriz 2: "))
c2 = int(input("Numero de columnas de la Matriz 2: "))

matriz1 = numpy.zeros((r1,c1))
matriz2 = numpy.zeros((r2,c2))
matrizr = numpy.zeros((r1,c2))

print("Introdice los elementos de la matris 1: ")
for i in range(0,r1):
  for j in range(0,c1):
    matriz1[i,j] = float(input("Elemnto ["+str(i+1)+","+str(j+1)+"]: "))

print("Introdice los elementos de la matris 2: ")
for i in range(0,r2):
  for j in range(0,c2):
    matriz2[i,j] = float(input("Elemento ["+str(i+1)+","+str(j+1)+"]: "))

#OPERACIONES
for i in range (0,r1):
  for j in range (0,c2):
    for k in range (0,r2):
      matrizr[i,j]+=matriz1[i,k]*matriz2[k,j]
print(matrizr)
