# 📈 Previsão do Dólar com ARIMA

Este projeto utiliza dados do Yahoo Finance para obter a cotação do dólar nos últimos 10 anos e gerar uma previsão para os próximos 30 dias utilizando o modelo ARIMA. 📊💵

## 📌 Funcionalidades

✅ Coleta automática dos dados do dólar desde 2015 usando o Yahoo Finance  
✅ Processamento e visualização dos dados históricos  
✅ Treinamento de um modelo ARIMA para previsão  
✅ Geração de gráficos interativos para análise  

## 🚀 Tecnologias Utilizadas

- Python 🐍
- Pandas 🗂️
- NumPy 🔢
- Matplotlib 📊
- Statsmodels 📈
- Yahoo Finance API 🌎

## 📥 Instalação

1. Clone este repositório:
   ```sh
   git clone https://github.com/VictorJeremias/previsao-dolar.git
   ```

2. Acesse o diretório do projeto:
   ```sh
   cd previsao-dolar
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## 🏗️ Como Usar

1. Execute o script principal:
   ```sh
   python dolar_prev.py
   ```
2. O código baixará os dados do dólar, treinará o modelo e gerará previsões para os próximos 30 dias.
3. Os resultados serão exibidos em gráficos interativos.

## 📊 Exemplo de Saída

O script exibirá gráficos como este:

![Gráfico de Previsão](https://via.placeholder.com/800x400.png?text=Previsao+do+Dolar)

## 📌 Ajuste dos Parâmetros do ARIMA

Os parâmetros do modelo ARIMA `(p, d, q)` podem ser ajustados no seguinte trecho do código:

```python
modelo = sm.tsa.ARIMA(dados, order=(5, 1, 0))
```

Onde:
- `p`: Número de defasagens (lags)
- `d`: Número de diferenciações
- `q`: Número de termos da média móvel

Ajuste esses valores para melhorar a precisão da previsão.


