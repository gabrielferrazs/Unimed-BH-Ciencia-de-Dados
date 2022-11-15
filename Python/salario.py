salario = int(input()) 

if (salario <= 600.00):
    novo_salario = round(salario * 1.17, 2)
    diferenca = round(novo_salario - salario,2)
    percentual = 17
    print("Novo salario é de: ", novo_salario)
    print("A diferença é de: ", diferenca)
    print("O percentual de aumento é de: ", percentual, "%")

elif (salario > 600.01 and 900.00):
    novo_salario = round(salario * 1.13, 2)
    diferenca = round(novo_salario - salario,2)
    percentual = 13
    print("Novo salario é de: ", novo_salario)
    print("A diferença é de: ", diferenca)
    print("O percentual de aumento é de: ", percentual, "%")

elif (salario > 900.01 and 1500.00):
    novo_salario = round(salario * 1.12, 2)
    diferenca = round(novo_salario - salario,2)
    percentual = 12
    print("Novo salario é de: ", novo_salario)
    print("A diferença é de: ", diferenca)
    print("O percentual de aumento é de: ", percentual, "%")

elif (salario > 1500.01 and 2000.00): 
    novo_salario = round(salario * 1.10, 2)
    diferenca = round(novo_salario - salario,2)
    percentual = 10
    print("Novo salario é de: ", novo_salario)
    print("A diferença é de: ", diferenca)
    print("O percentual de aumento é de: ", percentual, "%")

else: 
    novo_salario = round(salario * 1.05, 2)
    diferenca = round(novo_salario - salario,2)
    percentual = 5
    print("Novo salario é de: ", novo_salario)
    print("A diferença é de: ", diferenca)
    print("O percentual de aumento é de: ", percentual, "%")