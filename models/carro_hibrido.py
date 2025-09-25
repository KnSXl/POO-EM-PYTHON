from .carro_combustao import CarroCombustao
from .carro_eletrico import CarroEletrico

class CarroHibrido(CarroCombustao, CarroEletrico):
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
        volume_total_tanque: float,
        potencia_motor: float,
        n_motores: int,
        capacidade_bateria: float,
        carga_bateria: float,
        tipo = str
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
        CarroCombustao.__init__(
            self,
            marca = marca,
            modelo = modelo,
            ano = ano,
            cor = cor,
            placa = placa,
            n_portas = n_portas,
            volume_motor = volume_motor,
            n_cilindros = n_cilindros,
            volume_tanque = volume_tanque,
            volume_total_tanque = volume_total_tanque,
        )
        CarroEletrico.__init__(
            self,
            marca = marca,
            modelo = modelo,
            ano = ano,
            cor = cor,
            placa = placa,
            n_portas = n_portas,
            potencia_motor = potencia_motor,
            n_motores = n_motores,
            carga_bateria = carga_bateria,
            capacidade_bateria = capacidade_bateria,
        )
        self.tipo = tipo
        
    def exibir_informacoes(self):
        infos = CarroCombustao.exibir_informacoes(self)
        infos_eletrico = CarroEletrico.exibir_informacoes(self)
        infos_eletrico = infos_eletrico.split('Potencia')
        infos += "Potencia" + infos_eletrico[1]
        infos += f"Tipo de carro hibrido {self.tipo},\n"
        return infos