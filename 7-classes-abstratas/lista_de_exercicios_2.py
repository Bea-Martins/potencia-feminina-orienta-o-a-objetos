# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
# Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os requisitos abaixo.

# 1. Cada conta corrente pode ter um ou mais clientes como titular.
# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
#    Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela 
#    fizer um depósito, aumentaremos o saldo.
# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda
#    mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até
#    -renda_mensal.
# 5. Clientes homens por enquanto não têm direito a cheque especial.

# Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança", "propriedades", "encapsulamento" e "classe abstrata".

from abc import ABC, abstractmethod

class ModeloConta(ABC):
  def __init__(self, cliente, numero_conta):
    self.cliente = cliente
    self.__numero_conta = numero_conta

  @abstractmethod
  def sacar(self, valor):
    pass

  @abstractmethod
  def depositar(self, valor):
    pass

  @abstractmethod
  def extrato(self, valor):
    pass

  @abstractmethod
  def saldo(self, valor):
    pass

  @abstractmethod
  def apresentar_conta(self, valor):
    pass

class ContaCorrente(ModeloConta):
  def __init__(self, cliente, numero_conta):
    super().__init__(cliente, numero_conta)


class Cliente:
  def __init__(self, nome, telefone, sexo, renda_mensal):
    self.nome = nome
    self.telefone = telefone
    self.sexo = sexo
    self.renda_mensal = renda_mensal
    


# beatriz = Cliente('Beatriz','11987654321','feminino','30000')
# conta_mozoes = ContaCorrente(beatriz, 1)
# print(conta_mozoes)
