""" Questão 2
Implemente um método para percorrer um array, verificando se o número é par. Se for verdadeiro, 
multiplicar por dois, e se algum for maior que 50 retornar verdadeiro. Criar outro método seguindo 
os mesmos requisitos, porém para números ímpares, e o valor de teste para verdadeiro é 40.
"""

class ArrayProcessor:
    def __init__(self, arr):
        self.arr = arr

    def process_array(self):
        par_maior_50 = self._process_condition(lambda x: x % 2 == 0, 2, 50)
        impar_maior_40 = self._process_condition(lambda x: x % 2 != 0, 1, 40)
        return par_maior_50, impar_maior_40

    def _process_condition(self, condition_func, multiplier, threshold):
        for i, num in enumerate(self.arr):
            if condition_func(num):
                self.arr[i] *= multiplier
                if self.arr[i] > threshold:
                    return True
        return False

# Exemplo de uso
arr = [1, 2, 3, 5, 8, 13, 21, 34, 55]
processor = ArrayProcessor(arr)
par_result, impar_result = processor.process_array()

print("Par maior que 50:", par_result)  # Saída: Par maior que 50: True
print("Ímpar maior que 40:", impar_result)  # Saída: Ímpar maior que 40: False
print("Array modificado:", arr)  # Saída: Array modificado: [1, 4, 3, 5, 16, 13, 21, 68, 55]