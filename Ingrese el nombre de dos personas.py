#Este programa identifica si la letra con que inicia el nombre de las dos personas coincide


n1=str(input("Ingrese primer nombre"))
n2=str(input("Ingrese segundo nombre"))
a = n1
b = n2

if (a[0]) == (b[0]):
  print("Coincidencia")
elif (a[-1]) == (b[-1]):
  print("Coincidencia")
else:
  print("No hay coincidencia")
