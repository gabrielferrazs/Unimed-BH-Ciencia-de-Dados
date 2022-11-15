perna = input(str("Digite a perna: esqueda, direita, nenhuma ou ambas: "))

if perna == 'esquerda':
    print("Ingles")

elif perna == 'direita':
    print("Frances")

elif perna == 'nenhuma':
    print("Portugues")

elif perna == 'ambas':
    print("Caiu!")

else:
    print("Digite novamente")



while True: 
    try: 
      perna = input()
      
      if perna == "esquerda":
        print("Ingles")
      
      elif perna == "direita":
        print("Frances")
      
      elif perna == "nenhuma":
       print("Portugues")

      elif perna == "ambas":
        print("Caiu!")
  
           # TODO:  Programe aqui dentro as condições necessárias para satisfazer o problema
           # e imprima a saída de acordo com a situação das pernas do papagaio
    except EOFError: 
        break