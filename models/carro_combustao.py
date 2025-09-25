from .veiculo import Veiculo

class CarroCombustao(Veiculo):
    """
    Classe que implementa métodos espefícicos para veículos que 
    possuem combustão interna
    Args:
        Veiculo (classe): classe pai Veículo
    """
    def __init__(
        self,
        marca: str,
        modelo: str,
        ano: int,
        cor: str,
        placa: str,
        volume_motor: float,
        n_portas: int,
        n_cilindros: int,
        volume_tanque: float,
        volume_total_tanque: float
    ):
        """
        Construtor da Classe Carro Combustao
        Args:
            marca (str): _description_
            modelo (str): _description_
            ano (int): _description_
            cor (str): _description_
            placa (str): _description_
            volume_motor (float): _description_
            n_portas (int): _description_
            n_cilindros (int): _description_
            volume_tanque (float): _description_
        """
        Veiculo.__init__(self, marca, modelo, ano, cor, placa)
        self.volume_motor = volume_motor
        self.n_portas = n_portas
        self.n_cilindros = n_cilindros
        self.volume_tanque = volume_tanque
        self.volume_total_tanque = volume_total_tanque
        
    def exibir_informacoes(self):
        infos = Veiculo.exibir_informacoes(self)
        infos += f"Volume Motor: {self.volume_motor},\n" 
        infos += f"Número de portas: {self.n_portas},\n" 
        infos += f"Número de cilindros: {self.n_cilindros},\n" 
        infos += f"Volume total do Tanque: {self.volume_total_tanque},\n"
        infos += f"Volume Atual do Tanque: {self.volume_tanque}, \n"
        return infos
    
    def abastecer(self, volume):
        if volume < 0:
            print("Volume inválido! Deve ser maior do que zero!")
            return
        if self.volume_tanque < self.volume_total_tanque:
            if self.volume_tanque + volume <= self.volume_total_tanque:
                self.volume_tanque += volume
            else:
                print("O tanque não suporta totalmente o abastecimento!")
        else:
            print("Tanque cheio!")