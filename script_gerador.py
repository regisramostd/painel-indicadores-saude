
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
df = pd.read_csv("indicadores_por_cidade.csv")

# Redefinir o índice
df = df.set_index("Cidade").T

# Plot
plt.figure(figsize=(12, 6))
sns.set(style="whitegrid")
sns.lineplot(data=df)
plt.title("Painel Analítico de Indicadores Populacionais de Saúde", fontsize=14)
plt.ylabel("Prevalência (%)")
plt.xlabel("Indicador de Saúde")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("painel_analitico_indicadores.png")
