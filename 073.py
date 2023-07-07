# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros 
# colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem 
# de colocação. Depois mostre:

# a) Os 5 primeiros times.

# b) Os últimos 4 colocados.

# c) Times em ordem alfabética.

# d) Em que posição está o time da Chapecoense.

classificação =(
    "São Paulo", "Bahia", "Gremio", "Fortaleza",
    "Botafogo", "Flamengoo", "Fluminense", "Bragantino",
    "Internacional", "Atletico-PR", "Atletico_MG", "Cruzeiro",
    "Santos", "Cuiaba", "Corinthians","Palmeiras", "Goias", "Coritiba",
    "Chapecoense", "Vasco",
)
print(f'5 Primeiros: {classificação[0:5]}')
print(f'4 Ultimos: {classificação[-4:]}')
print(f'Em ordem Alfabética: {sorted(classificação)}')
print(f'Posição da chape: {classificação.index("Chapecoense")}')
