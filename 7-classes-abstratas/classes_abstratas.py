from abc import ABC, abstractmethod

class BasePokemon(ABC):
  def __init__(self, nome):
    self.nome = nome
    self._nivel = 1
    self._experiencia = 0

  @abstractmethod
  def ataque_principal(self):
    pass
  @abstractmethod
  def passar_de_nivel(self):
    pass
  @abstractmethod
  def evoluir(self):
    pass

  @property
  @abstractmethod
  def tipo(self):
    pass

# Criar um objeto de uma classe abstrata gera um erro
#pokemon = BasePokemon('Pikachu', 'Elétrico')
  
class Pikachu(BasePokemon):
  def __init__(self, nome):
    super().__init__(nome)

  def ataque_principal(self):
    print(f'{self.nome} usou Choque do trovão!\n')
    self._experiencia += 2
    self.passar_de_nivel()

  def passar_de_nivel(self):
    if self._experiencia % 10 == 0:
      self._nivel += 1
      print(f'{self.nome} passou para o nível {self._nivel}\n')
      self.evoluir()

  def evoluir(self):
    if self._nivel == 25:
      print('!!!" Evoluiu para Raichu !!!!\n')
      self.nome = 'Raichu'

  @property
  def tipo(self):
    return 'Elétrico'
  
  def ataque_secundario(self):
    print(f'{self.nome} usou Surra de Calda!\n')
    self._experiencia += 2
    self.passar_de_nivel()

pokemon = Pikachu('Pikachu')
print(pokemon.nome + ' é um pokemon do tipo ' + pokemon.tipo)
for _ in range(73):
  pokemon.ataque_principal()
  pokemon.ataque_secundario()