#Este programa pide las cosas que compramos y hace una lista hasta que escribamos "fin"


n1=str(input("Ingrese objetos "))
lista=[]
lista.append(n1)
n2="fin"
while n1 != n2:
  n1=str(input("Ingrese fin para acabar la lista y mostrarla "))
  lista.append(n1)
print("Su lista es:",lista)
