# from models.veiculo import Veiculo
# from models.moto import Moto
# from models.carro_combustao import CarroCombustao
# from models.carro_eletrico import CarroEletrico
from models.carro_hibrido import CarroHibrido

# Instancia um carro a combustão
""" uno = CarroCombustao(
    marca = "FIAT",
    modelo = "UNO MILLE",
    ano = 1999,
    cor = "Branco",
    placa = "IAA-1234",
    volume_motor = 1.0,
    n_portas = 2,
    n_cilindros = 4,
    volume_tanque = 5,
    volume_total_tanque = 50
)
print(uno.exibir_informacoes()) """

# Instancia um veiculo
""" corolla = Veiculo(
    modelo = "Corolla",
    marca = "Toyota",
    ano = 2020,
    cor = "Prata",
    placa = "III1B34"
)
print(corolla.exibir_informacoes()) """

# Instancia uma moto
""" cg125 = Moto(
    modelo="CG 124",
    marca="Honda",
    ano=1982,
    cor="Amarela",
    placa="III-1234",
    cilindradas=125,
    n_cilindros=1,
    tipo_motor="4 tempos",
    tipo_partida="mecânica"
)
print(cg125.exibir_informacoes()) """

# Instancia um carro hibrido
h6 = CarroHibrido(
    marca="GWM",
    modelo="H6",
    ano=2024,
    cor="Preto",
    placa="ABC-1234",
    n_portas=4,
    volume_motor=1.5,
    n_cilindros=4,
    volume_tanque=30,
    volume_total_tanque=50,
    capacidade_bateria=100,
    carga_bateria=90,
    n_motores=1,
    potencia_motor=204,
    tipo='plug-in'
)

# Teste com a classe CarroHibrido
print(h6.exibir_informacoes())
h6.abastecer(10)
h6.recarregar(10)
print(h6.exibir_informacoes())