#Este programa pide el ancho y el alto de un terreno y nos dice cual es el Area de este, también nos pregunta si queremos hacer el calculo de otro terreno o ya no


pre=1 
def area (x,y):
    x=float(input("Ingrese ancho del terreno: "))
    y=float(input("Ingrese altura del terreno: "))
    res=x*y
    print("El area del terreno es de: ", res)


  
while pre == 1:
   area(1,2)
   
   pre=int(input("Quiere continuar? 1. Si, 2. No "))
   if pre == 2:
      break
   elif pre == 1: 
      pre= 1
   
   else:
    print("Ingrese una opcion correcta ")
    pre=int(input("Quiere continuar? Si. 1, No. 2 "))
