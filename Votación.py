#Este programa pide un numero del 1 al 3 y cuando ingrese su numero le muestra a la persona por que cadidato voto


print("1. Candidato A")
print("2. Candidato B")
print("3. Candidato C")
n1=float(input("Elija un candidato segun el numero"))

if n1 == 1:
  print("Usted ha votado por el partido color rojo")
elif n1 == 2:
  print("Usted ha votado por el partido color verde")
elif n1 == 3:
  print("Usted ha votado por el partido color azul")
else:
  n1 > 3 or n1 < 0
  print("Opcion erronea")
