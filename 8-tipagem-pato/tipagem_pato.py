a = 1
print(type(a))

a = 'Maria'
print(type(a))
# python possui tipagem dinâmica
# python é uma liguagem interpretada

class Ave():
  def andar(self):
    print('andando')

  def voar(self):
    print('voando')

class Calopsita(Ave):
  def piar(self):
    print('piuuu piuuu')

class Pato(Ave):
  def quack(self):
    print('quack quack')

  def nadar(self):
    print('nadando')

def executar_pato(animal):
  animal.quack()
  animal.andar()
  animal.voar()
  animal.nadar()

def executar_calopsita(animal):
  animal.piar()
  animal.andar()
  animal.voar()

pato = Pato()
calopsita = Calopsita()

executar_pato(pato)
# executar_pato(calopsita)
executar_calopsita(calopsita)