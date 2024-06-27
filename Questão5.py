"""
Compactador:
Escreva dois métodos, um que recebe uma String de zeros e uns e comprime ela da seguinte maneira:
11100110000 -> 31202140
Outro que recebe a String comprimida e escreve ela descomprimida:
31202140 -> 11100110000

"""


class Compactador:
    def __init__(self):
        self.comprimido = ""
        self.contador = 1
        self.caractere_atual = ""  # Inicializa como string vazia

    def comprimir(self, binario):
        if not all(c in "01" for c in binario):  # Verifica se todos os caracteres são 0 ou 1
            raise ValueError("A string binária deve conter apenas 0s e 1s")

        self.caractere_atual = binario[0]  # Define o primeiro caractere aqui

        for i in range(1, len(binario)):
            if binario[i] == self.caractere_atual:
                self.contador += 1
            else:
                self.comprimido += str(self.contador) + self.caractere_atual
                self.caractere_atual = binario[i]
                self.contador = 1

        self.comprimido += str(self.contador) + self.caractere_atual
        return self.comprimido

    def descomprimir(self, comprimido):
        if not all(c.isdigit() for c in comprimido):  # Verifica se os caracteres nas posições são dígitos
            raise ValueError("A string comprimida deve conter apenas números")
        
        binario = ""
        for i in range(0, len(comprimido), 2):
            contador = int(comprimido[i])
            caractere = comprimido[i + 1]
            binario += caractere * contador
        return binario
    

    
# Exemplo de uso
# Instancia a classe
compactador = Compactador()

# Exemplo de compressão
binario = "111001100001111"
comprimido = compactador.comprimir(binario)
print(f"Comprimido: {comprimido}")  # Saída: Comprimido: 31202140

# Exemplo de descompressão
descomprimido = compactador.descomprimir(comprimido)
print(f"Descomprimido: {descomprimido}")  # Saída: Descomprimido: 11100110000