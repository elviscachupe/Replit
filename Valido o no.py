#Este programa nos pide un usuario y contraseña y nos dice si son validos o no


u = str(input("Ingrese su usuario: "))
c=str(input("Ingrese su contraseña: "))

y=u[-3:]

p=y.isdigit()
pv=str(p)

r = c.count(str(" "))

if (len(u))<=10 and pv=="True" and r<=0:
 print("Usuario válido")
else:
  print("Usuario inválido")

count=0
may=0
min=0
while count < len(c):
  letra = c[count]
  if letra.isupper() == True:
    may +=1
  else:
    min +=1
  count += 1
  
if  (len(c))>= 5 and may>=1 and min>=1:
  print("Contraseña valida")
else:
  print("Constraseña invalida")
