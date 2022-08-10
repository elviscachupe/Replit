#Este programa nos pide un numero y muesta la mitad de un diamante con la cantidad que ingesamos


i=int(input("Ingrese una cantidad: "))
t=i
y=i+1
m=y

for y in range ( 0, m):
  for n in range ( 0, y):
    print("# ", end="")
  print()
