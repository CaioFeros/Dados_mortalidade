import pandas as pd
import matplotlib.pyplot as plt

# nome do arquivo a ser importado
nome_arquivo = "casos_resumido.csv"

# importando a base de dados
base_dados = pd.read_csv(nome_arquivo,sep = ",")
print(base_dados['date'][0])

# exibindo o cabeçalho dos dados
print(base_dados.head(0))

# mostrando a média das colunas
print(f"Média de mortes: {base_dados['confirmed'].mean()}")
print(f"Máximo de mortes: {base_dados['confirmed'].max()}")
print(f"Mínimo de mortes: {base_dados['confirmed'].min()}")

# selecionando dados para análise
casos = base_dados["confirmed"]
mortes = base_dados["deaths"]

print(mortes)

# Criando colunas normalizadas
base_dados['deaths_norm'] = base_dados['deaths'] /base_dados['deaths'].abs().max()

base_dados['confirmed_norm'] = base_dados['confirmed'] /base_dados['confirmed'].abs().max()

# Exibindo dados 
print(f"Mortes confirmadas: {mortes[0]}\
      \nCasos confirmados: {casos[0]}")
print(base_dados.head(0))

# Exibindo gráficos
#plt.plot(mortes)
#plt.show()

# to set the plot size
#plt.figure(figsize=(16, 8), dpi=150)
  
# using plot method to plot open prices.
# in plot method we set the label and color of the curve.
#base_dados['confirmed'].plot(label='Casos', color='blue')
base_dados['confirmed_norm'].plot(label='Casos', color='blue')
#base_dados['deaths'].plot(label='Mortes', color='red')
base_dados['deaths_norm'].plot(label='Mortes', color='red')
 
# adding title to the plot
plt.title('Caso e Mortes no Período')
  
# adding Label to the x-axis
plt.xlabel('Tempos')
  
# adding legend to the curve
plt.legend()

plt.show()
