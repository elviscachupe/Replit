#Este es un programa que pide un año y muestra si es bisiesto o no


n1=int(input("Ingrese un año para saber si es bisiesto "))
if n1 % 4 == 0:
  if n1 % 100 == 0:
    if n1 % 400 == 0:
      print("El año es bisiesto")
    else:
      print("El año  no es bisiesto")
  else: 
    print("El año es bisiesto")
else:
  print("El año  no es bisiesto")
