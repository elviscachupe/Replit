#Esta es una función que pide que ingrese el ancho y el alto de un terreno y nos da el area del terreno


x=float(input("Ingrese ancho del terreno: "))
y=float(input("Ingrese altura del terreno: "))
def area(x,y):
  return x*y

print("El area del terreno es de: ", area(x,y))
