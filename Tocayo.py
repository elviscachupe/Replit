#Este programa recibe los nombres de dos perdsona e identifica si tienen el mismo nombre y si lo tienen dice que son tocayos


n1=str(input("Ingrese el primer nombre"))
n2=str(input("Ingrese el segundo nombre"))
if n1 == n2:
   print("Son tocayos")
else:
  print("No son tocayos")


n1=float(input("Ingrese el primer numero "))
n2=float(input("Ingrese el segundo numero "))
n3= n1**n2
print(n3, "este es el resultado de el primero elevado el segundo número")


nom=str(input("ingrese su nombre"))
edad=float(input("Ingrese su año de nacimiento"))
a=2022-edad
print("Hola", nom, "ya tienes", a, " años")
