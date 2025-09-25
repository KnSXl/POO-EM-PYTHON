class Veiculo:                                                               #
    """
    Classe base para implementação de um sistema de frota
    """
    def __init__(
        self,
        marca: str,
        modelo: str,
        ano: int,
        cor: str,
        placa: str
    ):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.placa = placa

    def exibir_informacoes(self):
        infos  = f"Modelo: {self.modelo},\n" 
        infos += f"marca: {self.marca},\n" 
        infos += f"ano: {self.ano},\n" 
        infos += f"cor: {self.cor},\n" 
        infos += f"placa: {self.placa}\n"
        return 