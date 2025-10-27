# 🚗 Exercício Relâmpago Surpresa: Velozes e Furiosos 🏁  

---

## 📚 Tema: Orientação a Objetos  
### Edição Especial — Corrida da Programação 🏎️💨  

---

## 📊 Diagrama de Classes

Observe o diagrama abaixo, que apresenta os conceitos de **herança** e **associação** entre classes:  
<img width="494" height="391" alt="Captura de tela 2025-10-26 210227" src="https://github.com/user-attachments/assets/e914cc82-5111-472a-ad45-afe08485cc01" />


<br/>
<img width="494" height="392" alt="image" src="https://github.com/user-attachments/assets/1c92224b-0bf1-4f19-bf07-3724ff2e2aad" />

---

## 🧩 O que devo fazer?

Com base no diagrama e nas observações apresentadas, implemente o sistema de **aluguel de veículos** conforme as regras abaixo:

---

## 🚘 Classe `Veiculo`

### 🔹 Atributos:
- `placa`
- `valor`
- `alugado` *(boolean — indica se o veículo está alugado ou não)*
- `historico` *(lista com registros de aluguel e devolução)*

### 🔹 Métodos:
- `__init__(self, placa, valor)`
- `alugar(self, cliente, dias)`
- `devolver(self)`
- `listarHistorico(self)`

### 🔹 Regras:
a) Um veículo **não pode ser alugado** se já estiver alugado.  
b) Um veículo **não pode ser devolvido** se não estiver alugado.  
c) Ao **alugar ou devolver**, atualizar o atributo `alugado` e registrar o evento no histórico.  

---

## 🚗 Classe `Carro` (herda de `Veiculo`)

### 🔹 Atributos:
- `modelo`

### 🔹 Método:
- `calcularAluguel(self, dias)`  
  → Valor total = `valor * dias`

---

## 🏍️ Classe `Moto` (herda de `Veiculo`)

### 🔹 Atributos:
- `modelo`

### 🔹 Método:
- `calcularAluguel(self, dias)`  
  → Valor total = `valor * dias`  
  → Se `dias > 30`, adicionar **10%**  
  → Se `dias > 40`, adicionar **20%**

---

## 👤 Classe `Cliente`

### 🔹 Atributos:
- `nome`

### 🔹 Método:
- `__init__(self, nome)`

---

## 💡 Exemplo de Entrada e Saída

**Entrada (exemplo de uso no código):**

```python
cliente1 = Cliente("Marco")
cliente2 = Cliente("Antonio")

carro1 = Carro("Celta", "ABC123", 100)
carro2 = Carro("Onix", "XYZ987", 120)
moto1 = Moto("MT07", "MOT123", 80)

carro1.alugar(cliente1, 5)
carro1.devolver()
carro2.alugar(cliente2, 15)
moto1.alugar(cliente1, 40)
moto1.devolver()

carro1.listarHistorico()
moto1.listarHistorico()
```

**Saída esperada (exemplo):**

```
Veículo ABC123 alugado para Marco por 5 dias (R$500)
Veículo ABC123 devolvido por Marco
Veículo XYZ987 alugado para Antonio por 15 dias (R$1800)
Veículo MOT123 alugado para Marco por 40 dias (R$3840)
Veículo MOT123 devolvido por Marco
```

---

## 🏁 Dicas para a corrida:

- 🚦 Teste cada método separadamente antes de integrar tudo.  
- 🧠 Utilize listas para armazenar o histórico dos veículos.  
- 🔄 Lembre-se de atualizar o atributo `alugado` sempre que o estado mudar.  
- 🧾 Implemente o método `listarHistorico` de forma que exiba o histórico completo de aluguéis e devoluções.  

---

### 👨‍💻 Objetivo:
Dominar **herança**, **associação** e **encapsulamento** através de um cenário prático e divertido!  
