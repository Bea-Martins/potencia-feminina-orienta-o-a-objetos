class MinhaCasa:
  def __init__(self, nome):
    self.nome = nome
    print(f'MinhaClasse: Chamou o construtor padrão {nome}')

  def __del__(self):
    print(f'MinhaClasse: Chamou o destrutor de {self.nome}')

print()
print('Começou a execução do programa')
object1 = MinhaCasa('objeto1')
print()
del object1
print('Vai terminar a execução do programa')
exit()