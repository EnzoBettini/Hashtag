import datetime as datetime
from random import randint
import pytz

class ContaCorrente:
    """
    Cria um objeto para gerenciar a conta corrente

    Attributes:
        nome (string): Nome do Cliente
        cpf (string): CPF do cliente
        limite (float): Limite da conta
        emergencial_ativo (Boolean): Verifica se o limite emergencial esta ativo
        num_conta (int): Numero da conta
        transacoes (list): todas as transacoes feitas

    """


    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        return fuso_BR

    def __init__(self, nome, cpf, num_conta):
        self._nome = nome
        self._limite = 0
        self._cpf = cpf
        self.emergencial_ativo = False
        self.num_conta = num_conta
        self._transacoes = []
        self._cartoes = []

    def consulta_limite(self):
        if self._limite < 0:
            print(f'{self._nome} esta usando o limite emergencial, seu limite é de: {self._limite}')
        else:
            print(f'O seu limite é: {self._limite}')

    def aumentar_limite(self, aumento):
        if float(aumento) < 0:
            print('Diminuir limite não permitido')
        else:
            self._limite = self._limite + float(aumento)
            print(f'O seu novo limite é: {self._limite}')

    def _verificar_emergencial(self):
        return self.emergencial_ativo

    def _adicionar_transacao(self, valor):
        self._transacoes.append(f'Data: {datetime.datetime.now(self._data_hora()):%d/%m/%Y %H:%M:%S} ----- Valor: {valor}')

    def realizar_pagamento(self, valor_pagamento):
        check = self._verificar_emergencial()
        if check == False:
            if float(valor_pagamento) > self._limite * 1.1:
                print('Compra negada, maior que limite liberado')
            elif float(valor_pagamento) <= (self._limite * 1.1) and float(valor_pagamento) > self._limite:
                self._limite -= float(valor_pagamento)
                self.emergencial_ativo = True
                self._adicionar_transacao(valor=float(valor_pagamento))
                print('Utilizando o limite emergencial de 10% para pagamento')
            else:
                self._limite -= float(valor_pagamento)
                self._adicionar_transacao(valor=float(valor_pagamento))
                print('Compra realizada')
        else:
            print('limite emergencial já foi ativado, não é possivel realizar a compra sem antes quitar o que já foi comprado')

    def transferir_limite(self, limite_envio, conta_destino):
        check = self._verificar_emergencial()
        if check == False:
            if float(limite_envio) > self._limite * 1.1:
                print('envio negado, maior que limite liberado')
            elif float(limite_envio) <= (self._limite * 1.1) and float(limite_envio) > self._limite:
                self._limite -= float(limite_envio)
                self.emergencial_ativo = True
                print('Utilizando o limite emergencial de 10% para envio de limite')
                conta_destino._limite += float(limite_envio)
            else:
                self._limite -= float(limite_envio)
                print('envio de limite realizado')
                conta_destino._limite += float(limite_envio)
        else:
            print('limite emergencial já foi ativado, não é possivel realizar a compra sem antes quitar o que já foi comprado')

    def limite_cartao(self, limite_entrada):
        aux = self._limite - limite_entrada
        if aux <=0:
            return 0
        else:
            self._limite = self._limite - limite_entrada
            return limite_entrada

class CartaoCredito:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        return fuso_BR

    @staticmethod
    def _definir_data():
        data = datetime.datetime.now(CartaoCredito._data_hora())
        data_final = data.replace(year=data.year+4)
        return data_final


    def __init__(self, titular, conta_corrente, limite_cartao):
        self._numero = randint(425680000000000, 425689999999999)
        self._titular = titular
        self._validade = f'{CartaoCredito._definir_data():%m/%y}'
        self._cvv = randint(000, 999)
        self._senha = 1234
        self._limite_cartao = conta_corrente.limite_cartao(limite_cartao)
        self._conta_corrente = conta_corrente
        conta_corrente._cartoes.append(self)

    @property
    def Senha(self):
        return self._senha

    @Senha.setter
    def Senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print('Senha inválida')



minha_conta = ContaCorrente(nome='enzo', cpf=12345678900, num_conta=000000)
minha_conta._limite = 150
conta_do_menino = ContaCorrente(nome='conta do menino', cpf=12345678900, num_conta=000000)

cartao = CartaoCredito(titular='bobson', conta_corrente=minha_conta, limite_cartao=50)

minha_conta._cartoes[0].Senha = '12345'
print(minha_conta._cartoes[0]._senha)

#.__dict__ lista tudo em formato de dicionario

print(minha_conta._cartoes[0]._numero)
print(minha_conta._cartoes[0]._limite_cartao)
print(minha_conta._cartoes[0]._validade)
print(minha_conta._cartoes[0]._numero)
print(minha_conta._cartoes[0]._titular)
print(minha_conta._cartoes[0]._cvv)
print(minha_conta._limite)

#teste consulta_limite
# minha_conta._limite = 100
# minha_conta.consulta_limite()
# minha_conta.aumentar_limite(aumento='100')
# minha_conta.aumentar_limite(aumento=-50)
# minha_conta.realizar_pagamento(valor_pagamento=100)
# minha_conta.consulta_limite()
# minha_conta.realizar_pagamento(valor_pagamento=110)
# minha_conta.consulta_limite()
# minha_conta.realizar_pagamento(valor_pagamento=110)
# print(minha_conta._transacoes)
# print('\n---------------------------\n')
# conta_do_menino._limite = 100
# conta_do_menino.transferir_limite(limite_envio=110, conta_destino=minha_conta)
# minha_conta.consulta_limite()
# conta_do_menino.consulta_limite()

