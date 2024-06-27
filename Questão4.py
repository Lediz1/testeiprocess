"""Questão 4
Considerando as seguintes entradas: produto (dois caracteres), marca (um caracter), valor (inteiro). Implementar um 
método que retorne verdadeiro ou falso seguindo as seguintes regras:
Se o valor for menor que 5, a marca não for "A", "B" ou "C" e produto igual a "AB" ou "BA", rejeitar.
Se o produto for composto de dois dígitos iguais e valor entre 10 e 30, rejeitar.
Se a marca for "A" rejeitar.
Se valor acima de 50, deve rejeitar.
Outros casos devem ser aceitos.
"""


class ValidadorProduto:
    """
    Classe para validar produtos com regras em métodos separados.
    """

    def __init__(self, produto, marca, valor):
        """Inicializa o validador com os dados do produto."""
        self.produto = produto
        self.marca = marca
        self.valor = valor

    def validar(self):
        """Aplica todas as regras de validação."""
        return (
            self._regra_valor_marca_produto() and
            self._regra_digitos_iguais() and
            self._regra_marca_a() and
            self._regra_valor_maximo()
        )

    def _regra_valor_marca_produto(self):
        """Regra 1: Valor < 5, marca != "A", "B" ou "C", e produto = "AB" ou "BA" """
        return not (self.valor < 5 and self.marca not in ["A", "B", "C"] and self.produto in ["AB", "BA"])

    def _regra_digitos_iguais(self):
        """Regra 2: Produto com dois dígitos iguais e 10 <= valor <= 30"""
        return not (self.produto[0] == self.produto[1] and 10 <= self.valor <= 30)

    def _regra_marca_a(self):
        """Regra 3: Marca = "A" """
        return self.marca != "A"

    def _regra_valor_maximo(self):
        """Regra 4: Valor > 50"""
        return self.valor <= 50


# Exemplos de uso 
validador1 = ValidadorProduto("AB", "D", 3)
print(validador1.validar())  # False

validador2 = ValidadorProduto("EF", "B", 45)
print(validador2.validar())  # True