from .veiculo import Veiculo

class Moto(Veiculo):
    def __init__(
        self,
        marca: str,
        modelo: str,
        ano: int,
        cor: str,
        placa: str,
        cilindradas: int,
        n_cilindros: int,
        tipo_motor: str,
        tipo_partida: str
    ):
        Veiculo.__init__(self, marca, modelo, ano, cor, placa) # ou: super().__init__(...)
        self.cilindradas = cilindradas
        self.n_cilindros = n_cilindros 
        self.tipo_motor = tipo_motor
        self.tipo_partida = tipo_partida
        
    def exibir_informacoes(self):
        infos = Veiculo.exibir_informacoes(self)
        infos += f"Cilindradas: {self.cilindradas}\n"
        infos += f"N Cilindros: {self.n_cilindros}\n"
        infos += f"Tipo de motor: {self.tipo_motor}\n"
        infos += f"Tipo partida: {self.tipo_partida}"
        return infos