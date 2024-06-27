""" Questão 1
Problema FizzBuzz:
Escreva um método que imprime os números de 1 a 50. Mas para múltiplos de três escreva "Fizz" ao 
invés do número e para múltiplos de cinco escreva "Buzz". Para números múltiplos de três e cinco imprima "FizzBuzz".

"""

def fizzbuzz():
    resultados = ["FizzBuzz", "Fizz", "Buzz","FizzBuzz"]
    for num in range(1, 51):

        indice = (num % 3 == 0) + 2 * (num % 5 == 0)  # Calcula o índice na lista
        print(resultados[indice] if indice else num)  # Imprime o resultado ou o número

fizzbuzz()