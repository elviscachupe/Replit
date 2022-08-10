#Este programa identifica si la palabra se escribe igual de forma normal a forma inversa y si es igual entonces quiere decir que es un palidromo


x=str(input("Ingrese una palabra para saber si es palidromo: "))
if str(x) == "".join(reversed(x)):
  print("Palindromo")
else:
  print("No es palidromo")
