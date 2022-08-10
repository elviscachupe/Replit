#Este programa pide la altura y el radio de un cilindro y nos da el volumen


a=int(input("Ingrese la altura: "))
r=int(input("Ingrese el radio: "))

c=(r*r)*3.14

v=c*a
print("El volumen del cilindro es de:", v)
