import random
from estagios_forca import stages, logo
from palavras_forca import lista_forca
from replit import clear

palavra = random.choice(lista_forca).lower()

vidas = 6
print(logo)
lista_palavra = len(palavra)
repeticao = []
display = []

for _ in palavra:
    display.append("_")
fim_jogo = False  

while fim_jogo == False:
  
  letra = input("Escolha uma letra ").lower()
  clear()
  if letra not in repeticao: 
    for posicao in range(0, lista_palavra):
      letras = palavra[posicao]
      if letras == letra:
        display[posicao] = letra
        
    if letra not in palavra:
      vidas -= 1
      print(f"a letra {letra} não está na palavra e voce acabou de perder uma vida")
  else:
    print(f"A letra {letra} ja foi usada")
  repeticao.append(letra)
  
  print(stages[vidas])    
  print(f"Voce tem {vidas} vidas")
     
  print(f"{' '.join(display)}")
  
  if "_" not in display:
    fim_jogo = True
    print("VOCE GANHOU") 
  elif vidas == 0:
    fim_jogo = True
    print("VOCE PERDEU")
    print(f"a palavra era {palavra}")
    

     
        

  
        



    

