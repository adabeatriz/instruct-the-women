class Estacionamento:
    def __init__(self):
        self.vaga_carro = 25
        self.vaga_moto = 25
        self.carro_para_vaga = 0
        self.moto_para_vaga = self
        self.total_vaga_livres_carro = self.vaga_carro
        self.total_vaga_livres_moto = self.vaga_moto

    def __str__(self) -> str:
        return(f'vaga carro: {self.vaga_carro}, vaga moto {self.vaga_moto}, \
            carro em espera {self.carro_para_vaga}, moto em espera: {self.moto_para_vaga}, \
            total vaga livre carro: {self.total_vaga_livres_carro}, total vaga livre moto: {self.total_vaga_livres_moto}')
        
    def estacionar_carro(self):
        if self.total_vaga_livres_carro <= self.vaga_carro:
            self.total_vaga_livres_carro -= 1

    def estacionar_moto(self):
        if self.total_vaga_livres_moto <= self.vaga_moto:
            self.total_vaga_livres_moto -= 1

    def remover_carro(self):
        self.total_vaga_livres_carro += 1

    def remover_moto(self):
        self.total_vaga_livres_moto += 1

    def estado_do_estacionamento(self):
        if self.total_vaga_livres_carro == 0:
            print("Estacionamento de carro Lotado")
            self.carro_para_vaga += 1
        elif self.total_vaga_livres_moto== 0:
            print("Estacionamento de moto Lotado")
            self.moto_para_vaga += 1
        else: 
            print("Há Vaga")

class Vaga:
    def __init__(self, id, tipo, placa):
        self.id = id
        self.tipo = tipo
        self.livre = True
        self.placa = placa

    def __str__(self) -> str:
        return(f'Id {self.id}, tipo {self.tipo}, placa {self.placa}, vaga livre: {self.livre}')
    
    def ocupar(self):
        if self.livre:
            self.livre = False
    
    def desocupar(self):
        if not self.livre:
            self.livre = True

class Automovel:
    def __init__(self, placa):
        self.placa = placa
        self.estacionado = False

    def estacionar(self):
        self.estacionado = True

    def sair_da_vaga(self):
        if not self.estacionado:
            self.estacionado = False

    def __str__(self) -> str:
        return(f'Placa {self.placa} status {self.estacionado}')

class Carro(Automovel):
    def __init__(self, placa):
        super().__init__(placa)

class Moto(Automovel):
    def __init__(self, placa):
        super().__init__(placa)

