# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.

class Carro:
  def __init__(self):
    self.ligado = False
    self.cor = 'preto'
    self.modelo = 'conversível'
    self.velocidade = 0
    self.velocidade_min = 0
    self.velocidade_max = 180

  def liga(self):
    self.ligado = True

  def desliga(self):
    self.ligado = False

  def acelera(self):
    if not self.ligado:
      return
    
    if self.velocidade < self.velocidade_max:
      self.velocidade += 10

  def desacelera(self):
    if not self.ligado:
      return
    
    if self.velocidade > self.velocidade_min:
      self.velocidade -= 10

  def __str__(self) -> str:
    return f'Carro - ligado {self.ligado} - cor {self.cor} - modelo {self.modelo} - velocidade {self.velocidade}'

# Crie uma instância da classe carro.
carro_bea = Carro()
carro_bea.liga()
print('carro_bea está ligado? {}'.format(carro_bea.ligado))
print()

# Faça o carro "andar" utilizando os métodos da sua classe.
for _ in range(3):
  carro_bea.acelera()
print('carro_bea velocidade: {}'.format(carro_bea.velocidade))
print()

# Faça o carro "parar" utilizando os métodos da sua classe.
for _ in range(3):
  carro_bea.desacelera()
print('carro_bea velocidade: {}'.format(carro_bea.velocidade))
print()