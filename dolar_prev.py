import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import yfinance as yf
from datetime import datetime, timedelta

# Definir período de coleta de dados
hoje = datetime.today()
data_inicio = "2015-01-01"
data_fim = hoje.strftime('%Y-%m-%d')

# Baixar os dados do Yahoo Finance
dados = yf.download('BRL=X', start=data_inicio, end=data_fim)

# Verificar se os dados foram carregados corretamente
if dados.empty:
    print("Erro ao carregar os dados do Yahoo Finance.")
else:
    # Renomear colunas
    dados = dados[['Close']]
    dados.columns = ['cotacao_dolar']
    
    # Exibir estatísticas básicas
    print("Valores estatísticos:\n", dados.describe())
    
    # Ordenar por data
    dados = dados.sort_index()
    
    # Visualizar os dados
    plt.figure(figsize=(12, 5))
    plt.plot(dados, label='Cotação do Dólar')
    plt.xlabel('Ano')
    plt.ylabel('Valor do Dólar (R$)')
    plt.legend()
    plt.title('Histórico do Dólar desde 2015')
    plt.show()

    # Criar modelo ARIMA para previsão
    def treinar_modelo_arima(dados):
        modelo = sm.tsa.ARIMA(dados, order=(5, 1, 0))  # Ajuste os parâmetros conforme necessário
        modelo_ajustado = modelo.fit()
        return modelo_ajustado

    # Treinar o modelo
    modelo_arima = treinar_modelo_arima(dados)

    # Fazer previsão para os próximos 30 dias
    previsao = modelo_arima.forecast(steps=30)

    # Exibir previsão
    plt.figure(figsize=(12, 5))
    plt.plot(dados, label='Cotação do Dólar')
    plt.plot(pd.date_range(dados.index[-1], periods=30, freq='D'), previsao, label='Previsão', linestyle='dashed')
    plt.xlabel('Ano')
    plt.ylabel('Valor do Dólar (R$)')
    plt.legend()
    plt.title('Previsão do Dólar para os próximos 30 dias')
    plt.show()