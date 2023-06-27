# Sequencia de Fibonacci

n = int(input('Quantos termos você que mostrar? '))
t1 = 0 
t2 = 1
contador = 3
print(t1)
print(t2)
while contador <= n:
    t3 = t1 + t2 
    print(t3)
    t1 = t2
    t2 = t3
    contador += 1
    
