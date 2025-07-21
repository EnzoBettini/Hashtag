import datetime as datetime
import pytz

class ContaCorrente:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        return fuso_BR

    def __init__(self, nome, cpf, num_conta):
        self.nome = nome
        self.limite = 0
        self.cpf = cpf
        self.emergencial_ativo = False
        self.num_conta = num_conta
        self.transacoes = []

    def consulta_limite(self):
        if self.limite < 0:
            print(f'{self.nome} esta usando o limite emergencial, seu limite é de: {self.limite}')
        else:
            print(f'O seu limite é: {self.limite}')

    def aumentar_limite(self, aumento):
        if float(aumento) < 0:
            print('Diminuir limite não permitido')
        else:
            self.limite = self.limite + float(aumento)
            print(f'O seu novo limite é: {self.limite}')

    def _verificar_emergencial(self):
        return self.emergencial_ativo

    def _adicionar_transacao(self, valor):
        self.transacoes.append(f'Data: {datetime.datetime.now(self._data_hora()):%d/%m/%Y %H:%M:%S} ----- Valor: {valor}')

    def realizar_pagamento(self, valor_pagamento):
        check = self._verificar_emergencial()
        if check == False:
            if float(valor_pagamento) > self.limite * 1.1:
                print('Compra negada, maior que limite liberado')
            elif float(valor_pagamento) <= (self.limite * 1.1) and float(valor_pagamento) > self.limite:
                self.limite -= float(valor_pagamento)
                self.emergencial_ativo = True
                self._adicionar_transacao(valor=float(valor_pagamento))
                print('Utilizando o limite emergencial de 10% para pagamento')
            else:
                self.limite -= float(valor_pagamento)
                self._adicionar_transacao(valor=float(valor_pagamento))
                print('Compra realizada')
        else:
            print('limite emergencial já foi ativado, não é possivel realizar a compra sem antes quitar o que já foi comprado')

    def transferir_limite(self, limite_envio, conta_destino):
        check = self._verificar_emergencial()
        if check == False:
            if float(limite_envio) > self.limite * 1.1:
                print('envio negado, maior que limite liberado')
            elif float(limite_envio) <= (self.limite * 1.1) and float(limite_envio) > self.limite:
                self.limite -= float(limite_envio)
                self.emergencial_ativo = True
                print('Utilizando o limite emergencial de 10% para envio de limite')
                conta_destino.limite += float(limite_envio)
            else:
                self.limite -= float(limite_envio)
                print('envio de limite realizado')
                conta_destino.limite += float(limite_envio)
        else:
            print('limite emergencial já foi ativado, não é possivel realizar a compra sem antes quitar o que já foi comprado')


minha_conta = ContaCorrente(nome='enzo', cpf=12345678900, num_conta=000000)
conta_do_menino = ContaCorrente(nome='conta do menino', cpf=12345678900, num_conta=000000)


#teste consulta_limite
minha_conta.limite = 100
minha_conta.consulta_limite()
minha_conta.aumentar_limite(aumento='100')
minha_conta.aumentar_limite(aumento=-50)
minha_conta.realizar_pagamento(valor_pagamento=100)
minha_conta.consulta_limite()
minha_conta.realizar_pagamento(valor_pagamento=110)
minha_conta.consulta_limite()
minha_conta.realizar_pagamento(valor_pagamento=110)
print(minha_conta.transacoes)
print('\n---------------------------\n')
conta_do_menino.limite = 100
conta_do_menino.transferir_limite(limite_envio=110, conta_destino=minha_conta)
minha_conta.consulta_limite()
conta_do_menino.consulta_limite()

