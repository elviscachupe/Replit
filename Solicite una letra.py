#Este es un programa que nos ayuda a identificar cuando una letra es vocal o consonante


letra=str(input("Ingrese una letra para saber si es vocal o consonante"))

if letra >= "0" or letra <= "0":
  print("No ingrese numeros")
if (len(letra)) > 1:
  print("Ingrese solo una letra")
elif (len(letra)) == 1:
  if letra == "a" or letra == "A":
    print("La letra es vocal")
  elif letra == "e" or letra == "E":
    print("La letra es vocal")
  elif letra == "i" or letra == "I":
    print("La letra es vocal")
  elif letra == "o" or letra == "O":
    print("La letra es vocal")
  elif letra == "u" or letra == "U":
    print("La letra es vocal")
  else:
    print("La letra es consonante")
