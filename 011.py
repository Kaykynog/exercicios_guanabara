#Conversor de medidas 
metro = float(input('DIgite um valor para ser convertido: '))

km = metro / 1000
hec = metro / 100
dam = metro / 10
dm = metro * 10
cm = metro * 100
mm = metro * 1000

print(f' em metro: {metro} \n , em km: {km} \n , em hec {hec} \n , em dam {dam} \n , em dm {dm} \n em cm {cm,} \n em mm {mm}')
