num = int(input("Digite: "))
lista = [25, 10, 5, 1]
resultado = []
cont = True
while cont:
  if num >= 25:
    resultado.append(25)
    num = num - 25
  elif num >= 10:
    resultado.append(10)
    num = num - 10
  elif num >= 5:
    resultado.append(5)
    num = num - 5
  elif num >= 1:
    resultado.append(1)
    num = num - 1
  else:
    cont = False

print(resultado)
