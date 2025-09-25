from .veiculo import Veiculo

class CarroEletrico(Veiculo):
    """
    Classe que implementa métodos espefícicos para veículos elétricos
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
        potencia_motor: float,
        n_portas: int,
        n_motores: int,
        capacidade_bateria: float,
        carga_bateria: float
    ):
        """
        Construtor da Classe Carro Elétrico
        Args:
            marca (str): _description_
            modelo (str): _description_
            ano (int): _description_
            cor (str): _description_
            placa (str): _description_
            potencia_motor (float): _description_
            n_portas (int): _description_
            n_motores (int): _description_
            capacidade_bateria (float): _description_
            carga_bateria (float): _description_
        """
        Veiculo.__init__(self, marca, modelo, ano, cor, placa)
        self.potencia_motor = potencia_motor
        self.n_portas = n_portas
        self.n_motores = n_motores
        self.capacidade_bateria = capacidade_bateria
        self.carga_bateria = carga_bateria
        
    def exibir_informacoes(self):
        infos = Veiculo.exibir_informacoes(self)
        infos += f"Potencia do Motor: {self.potencia_motor},\n" 
        infos += f"Número de portas: {self.n_portas},\n" 
        infos += f"Número de motores: {self.n_motores},\n" 
        infos += f"Capacidade da bateria: {self.capacidade_bateria},\n"
        infos += f"Carga atual da bateria: {self.carga_bateria},\n"
        return infos
    
    def recarregar(self, energia):
        if energia < 0:
            print("Energia inválida!")
            return
        if self.carga_bateria < self.capacidade_bateria:
            if self.carga_bateria + energia <= self.capacidade_bateria:
                self.carga_bateria += energia
            else:
                print("A bateria não suporta totalmente a recarga!")
        else:
            print("Bateria Cheia!!")