class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Agência com o caixa abaixo do minimo')
        else:
            print('O valor de caixa esta ok')

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Dinheiro acima do caixa disponivel na agencia')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))

class AgenciaVirtual(Agencia):

    def __init__ (self, site, telefone, cnpj, numero):
        self.site = site
        super().__init__(telefone, cnpj, numero)

class AgenciaComum(Agencia):

    def __init__ (self, site, telefone, cnpj, numero):
        self.site = site
        super().__init__(telefone, cnpj, numero)

class AgenciaPremium(Agencia):

    def __init__ (self, site, telefone, cnpj, numero):
        self.site = site
        super().__init__(telefone, cnpj, numero)
        self.caixa = 12783493874

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            return super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('Cliente nao tem patrimonio suficiente pa a a agencia')



agencia1 = AgenciaVirtual(telefone=111, cnpj=111, numero=111, site='www.aoaoaoao.com.br')
agencia2 = AgenciaPremium(telefone=111, cnpj=111, numero=111, site='www.aoaoaoao.com.br')

print(agencia1.site)

agencia1.caixa = 1000000

agencia1.verificar_caixa()

agencia1.emprestar_dinheiro(50, 111111, 0.02)

print(agencia1.emprestimos)

agencia1.adicionar_cliente('bobson', '111.111.111-11', 0.02)
agencia2.adicionar_cliente('bobson', '111.111.111-11', 0.02)
agencia2.adicionar_cliente('cliente cuiudo', '111.111.111-11', 100000000000015651)

print(agencia1.clientes)
print(agencia2.clientes)
