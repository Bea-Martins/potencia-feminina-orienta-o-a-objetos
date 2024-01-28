def cardapio():
  comida = 'hamburguer'
  print(comida)

cardapio()
# cardapio(comida) erro

bebida = 'refrigerante'
def cardapio():
  global bebida # permite alterar a variável global
  comida = 'hamburguer'
  bebida = 'suco'
  print('comida:', comida)
  print('bebida:', bebida)

cardapio()
print('bebida:', bebida)