class TV:

    cor = 'preta' #COR FIXA

    def __init__(self, Tamanho):
        self.ligado = False
        self.tamanho = Tamanho
        self.canal = 'Netflix'
        self.volume = 10
        pass

    def mudar_canal(self):
        self.canal = 'Globo'

    def escolher_canal(self, novo_canal):
        self.canal = novo_canal


#TESTANDO CRIAÇÃO DE INSTANCIAS
tv_sala = TV(Tamanho=55)
print(tv_sala.tamanho)
tv_quarto = TV(Tamanho=66)
print(tv_quarto.tamanho)

# TESTANDO mudar_canal
print(tv_sala.canal)
tv_sala.mudar_canal()
print(tv_sala.canal)

# TESTANDO escolher_canal
print(tv_sala.canal)
tv_sala.escolher_canal('Youtube')
print(tv_sala.canal)

#MUDANDO A COR DA CLASSE INTEIRA
print(tv_sala.cor)
print(tv_quarto.cor)

TV.cor = 'branca'

print(tv_sala.cor)
print(tv_quarto.cor)
