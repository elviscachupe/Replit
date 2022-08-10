#Este programa recibe los dos apellidos y nombres y con ellos crea un correo electronico


a=str(input("Ingrese primer nombre: "))
b=str(input("Ingrese segundo nombre: "))
c=str(input("Ingrese primer apellido: "))
d=str(input("Ingrese segundo apellido: "))

e=a[0]+b[0]+"."+c+d+"@baco.com"

f=e.lower()

g=f.replace(" ","")

print("El correo asignado es: ",f)
