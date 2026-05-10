import numpy as np
from numpy.ma.extras import average

    #Exercício 1
manha = np.array([10,15,30])
tarde = np.array([20,8,0])
resultado = round(average(manha) + average(tarde), 1)
print(f"Média pluviométrica diária registrada em 14/04/2026: \n"
      f"{resultado}mm")

    #Exercício 2
estoque_ini = np.array([5,5,5])
estoque_vend = np.array([2,1,0])
estoque_fin = estoque_ini - estoque_vend
print(f"Quantidade total de produtos vendidos: {estoque_vend}")
print(f"Quantidade total de produtos final: {estoque_fin}")

    #Exercício 3
arr1 = np.random.randn(3,2)
print(f"Matriz inicial 1: {arr1} \n")
arr2 = np.random.randn(3,2)
print(f"Matriz inicial 2: {arr2} \n")

m = arr1 * arr2
print(f"Matriz final: {m}")

    #Exercício 4
salario = np.array([
    [2500.50, 3100.00, 4200.75],  # Primeira linha (ex: Setor A)
    [5300.00, 6100.20, 7500.00],  # Segunda linha (ex: Setor B)
    [8200.50, 9400.00, 10500.00]  # Terceira linha (ex: Diretoria)
])
salario_reajustado = salario * 1.10
print(salario)
print(salario_reajustado)

