class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.status = None
        self.tipo = None

    def ligar(self):
        print('Ligando veiculo...')
    def andar(self):
        print("Vrum Vrum...")
    def desligar(self):
        print('Desligando veiculo...')

    def getMarca(self):
        return self.marca 
    def setMarca(self, marca):
        self.marca = marca

    def getModelo(self):
        return self.modelo
    def setModelo(self, modelo):
        self.modelo = modelo

    def getAno(self):
        return self.ano
    def setAno(self,ano):
        self.ano = ano 

    def getStatus(self):
        return self.status
    def setStatus(self, status):
        self.status = status

    def getTipo(self):
        return self.tipo
    def setTipo(self, tipo):
        self.tipo = tipo


class Moto(Veiculo):                       
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)

    def dar_grau(self):
        print('Bo-lo-lo pa pa')


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
        
    def cantar_pneu(self):
        print('Vrum-vrum')

