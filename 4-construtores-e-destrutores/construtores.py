class MinhaCasa1:
  def __init__(self):
    print('MinhaClasse1: Chamou o construtor padrão')

class MinhaCasa2:
  pass # não faz nada

class MinhaCasa3:
  def __init__(self, param): #construtor parametrizado
    print(f'MinhaClasse3: Chamou o construtor parametrizado com o parâmetro {param}')

object1 = MinhaCasa1()
object2 = MinhaCasa2()
object3 = MinhaCasa3('meu objeto')