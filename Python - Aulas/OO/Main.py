from ClassesBancos import ContaCorrente, CartaoCredito

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
minha_conta._limite = 100
minha_conta.consulta_limite()
minha_conta.aumentar_limite(aumento='100')
minha_conta.aumentar_limite(aumento=-50)
minha_conta.realizar_pagamento(valor_pagamento=100)
minha_conta.consulta_limite()
minha_conta.realizar_pagamento(valor_pagamento=110)
minha_conta.consulta_limite()
minha_conta.realizar_pagamento(valor_pagamento=110)
print(minha_conta._transacoes)
print('\n---------------------------\n')
conta_do_menino._limite = 100
conta_do_menino.transferir_limite(limite_envio=110, conta_destino=minha_conta)
minha_conta.consulta_limite()
conta_do_menino.consulta_limite()
