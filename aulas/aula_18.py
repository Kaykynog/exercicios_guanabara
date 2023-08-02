# # brincando com listas compostas
# galera = [['Kayky', 19], ['Julia', 19], ['Alfredo', 35]]
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade')

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0,5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else: 
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade...')