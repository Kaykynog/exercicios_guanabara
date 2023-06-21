# Mesma coisa do 63, porém agora com a opção de escolha do usuario 
# Refazendo o desafio de progressão aritmetica com while

n = int(input('Digite um numero para obter sua PA: '))
r = int(input('Qual é a razão ? '))
count = 0
adicao = 1
while adicao != 0:
    n = n + r 
    count += 1
    print(n)
    adicao = int(input('Digite quantos termos a mais deseja, ou zero para sair '))
    for c in range(0, adicao):
        n = n + r 
        print(n)



    
                
                   
