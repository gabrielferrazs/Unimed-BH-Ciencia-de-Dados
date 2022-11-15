# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar
#entrada = input().split()

#distancia = int(entrada[0])
#diametro1 = int(entrada[1])
#diametro2 = int(entrada[2])

# TODO: Calcule o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 casas decimais no espaço #em branco abaixo:

distancia = float(input("Digite a distancia: "))
diametro1 = float(input("Digite o priemiro diametro: "))
diametro2 = float(input("Digite o segundo diametro: "))

# Calculo
# basta dividir a distância entre os dois Palantír’s, pela soma do diâmetro dos mesmos

resultado_icm = round(distancia / (diametro1 + diametro2),2)
print(f"O ICM é de: {resultado_icm}")