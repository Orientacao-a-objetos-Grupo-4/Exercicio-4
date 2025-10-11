#Importando as classes
from Moto import moto
from Carro import carro
from Cliente import cliente

# Criando Instancia de Cliente
print("----- Cliente ------")
cliente = cliente("Pedro Paulo")
print(cliente)

# Criando Carro
print("---- Carro -----")
carro = carro("Honda Fit","ABC-1234",50.00)
diasCarro = 5
aluguelCarro = carro.Calcular_Aluguel(diasCarro);
print(f"Cálculo para {diasCarro} dias: R${aluguelCarro:.2f} (Diária: R${carro.get_valor():.2f})")
print(carro)

# Criando instâncias de moto
moto1 = moto("MOT-3421", 30.00) 
moto2 = moto("MTO-2345", 45.00)

# --- Teste da Moto 1 (Disponível) ---
print("--- Moto 1 (Disponível) ---")
print(moto1)

# 1. Cálculo de aluguel por 5 dias (Regra de +20%)
dias_curto = 5
valor_curto = moto1.calcularAluguel(dias_curto)
print(f"Cálculo para {dias_curto} dias: R${valor_curto:.2f} (Diária: R${moto1.get_valor():.2f})")

# 2. Alugar a moto por 5 dias
moto1.alugar("Carlos", dias_curto)
print(moto1)
print(f"Histórico: {moto1.get_historico()}")

# 3. Devolver
moto1.devolvido()
