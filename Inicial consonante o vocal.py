#Este programa pide una palabra e identifica si inicia con vocal o consonante


palabra=str(input("Ingrese una palabra: "))
letra=palabra[0]

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
