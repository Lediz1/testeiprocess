""" Questão 3
Implementar uma interface de entrada, com dois campos ambos numéricos, aceitando valores de 1 a 5.
No primeiro, se o valor for igual a 3,4 ou 5 deve sinalizar "Correto".
No segundo, se o valor for menor que o primeiro deve sinalizar "Correto".
Criar um botão/ação, que ao ser disparado, sinaliza a soma dos dois valores.
"""


import tkinter as tk
from tkinter import messagebox

class Interface:
    def __init__(self, master):
        self.master = master
        master.title("Verificador de Valores")

        # Campos de entrada
        tk.Label(master, text="Valor 1 (1-5):").grid(row=0)
        tk.Label(master, text="Valor 2 (1-5):").grid(row=1)

        self.valor1 = tk.Entry(master)
        self.valor2 = tk.Entry(master)

        self.valor1.grid(row=0, column=1)
        self.valor2.grid(row=1, column=1)

        # Botão
        tk.Button(master, text="Verificar e Somar", command=self.verificar_e_somar).grid(row=2, columnspan=2)

    def verificar_e_somar(self):
        try:
            valor1 = int(self.valor1.get())
            valor2 = int(self.valor2.get())

            if not (1 <= valor1 <= 5 and 1 <= valor2 <= 5):
                raise ValueError("Valores fora do intervalo permitido (1-5).")

            resultado1 = "Correto" if valor1 in [3, 4, 5] else "Incorreto"
            resultado2 = "Correto" if valor2 < valor1 else "Incorreto"

            soma = valor1 + valor2

            messagebox.showinfo("Resultados", 
                                f"Valor 1: {resultado1}\nValor 2: {resultado2}\nSoma: {soma}")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

root = tk.Tk()
interface = Interface(root)
root.mainloop()