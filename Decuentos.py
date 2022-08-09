#Esta aplicacíon realiza descuentos dependiendo de la cantidad que adquiramos, solo hace descuento si la cantidad es mayor a 4

print("aplicacion de descuentos")
n1=int(input("ingrese cantidad del producto"))
n2=0.75
n3=int(input("precio del producto"))
n4=0.25
if n1>4:
  res=(n3*n1*n2)
  print("precio total con descuento")
  print(res)
else:
  res=(n3*n1*1)
  print("no hay descuento")
  print(res)

print("precio total sin descuento")
print(n1*n3)

if n1>4:
  res=(n3*n1*n4)
  print("descuento del precio total")
  print(res)
else:
  res=(0)
  print("no hay descuento")
  print(res)
