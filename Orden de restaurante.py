#El funcionamiento de mi programa es que va preguntando sobre lo que queremos comer en nuestra orden y al finalizar el programa muestra el total de ordenes que se 
#hicieron, tambíen deberia de mostrar el porcentaje de ordenes y debe mostrar que ingrediente no lleva cada orden print("¿Desea ordenar?")
ORDEN=float(input("1.si  2.no "))
CONTADOR=0
SINLECHUGA=0
SINTOMATE=0
SINTORTAEXTRA=0
ENCOMBO=0
SINCOMBO=0
CONPAPAS=0
CONAROS=0
COLA=0
SPRITEE=0
PEPSII=0
UPP=0



while ORDEN==1:
  
  print("¿Desea torta de carne?")
  CARNE=float(input("1.si  2.no "))
  
  print("¿Desea una torta de carne extra?")
  CARNEE=float(input("1.si  2.no "))
  if CARNEE==2:
    SINTORTAEXTRA=SINTORTAEXTRA+1

  print("¿Desea tocino?")
  TOCINO=float(input("1.si  2.no "))
  
  print("¿Desea lechuga?")
  LECHUGA=float(input("1.si  2.no "))
  if LECHUGA==2:
    SINLECHUGA=SINLECHUGA+1

  print("¿Desea tomate?")
  TOMATE=float(input("1.si  2.no "))
  if TOMATE==2:
    SINTOMATE=SINTOMATE+1
  
  print("¿Desea cebolla?")
  CEBOLLA=float(input("1.si  2.no "))
  
  print("¿Desea mayonesa?")
  MAYONESA=float(input("1.si  2.no "))
  
  print("¿Desea mostaza?")
  MOSTAZA=float(input("1.si  2.no "))
  
  print("¿Desea ketchup?")
  KETCHUP=float(input("1.si  2.no "))
  
  print("¿Desea papas?")
  PAPAS=float(input("1.si  2.no "))
  if PAPAS==1:
    CONPAPAS=CONPAPAS+1
  
  print("¿Desea aros de cebolla?")
  AROS=float(input("1.si  2.no "))
  if AROS==1:
    CONAROS=CONAROS+1
  
  print("¿Desea coccacola?")
  COCA=float(input("1.si  2.no "))
  if COCA==1:
    COLA=COLA+1
  
  print("¿Desea sprite?")
  SPRITE=float(input("1.si  2.no "))
  if SPRITE==1:
    SPRITEE=SPRITEE+1
  
  print("¿Desea pepsi?")
  PEPSI=float(input("1.si  2.no "))
  if PEPSI==1:
    PEPSII=PEPSII+1
  
  print("¿Desea 7up?")
  UP=float(input("1.si  2.no "))
  if UP==1:
    UPP=UPP+1

  CONTADOR=CONTADOR+1
  
  print("¿Desea otra orden?")
  ORDEN=float(input("1.si  2.no "))


    
if ORDEN==2:
  
  print("El total de ordenes es: ",CONTADOR)
  
  print("El porcentaje de ordenes sin lechuga es: ", 100*SINLECHUGA/CONTADOR)

  print("El porcentaje de ordenes sin tomate es: ", 100*SINTOMATE/CONTADOR)

  print("El porcentaje de ordenes sin torta extra es: ", 100*SINTORTAEXTRA/CONTADOR)

  print("El porcentaje de ordenes sin tomate es: ", 100*ENCOMBO/CONTADOR)

  print("El porcentaje de ordenes sin tomate es: ", 100*SINCOMBO/CONTADOR)

  print("Porcentaje de ordenes con papas: ", 100*CONPAPAS/CONTADOR,"con aros de cebolla: ", 100*CONAROS/CONTADOR)

  print("El total de ordenes con cocacola es: ",COLA)
  
  print("El total de ordenes con sprite es: ",SPRITEE)
  
  print("El total de ordenes con pepsi es: ",PEPSII)
  
  print("El total de ordenes con 7up es: ",UPP)

n1=str(input("Ingrese nombre de persona que hizo el reporte: "))
print("___________________________________________________________")



