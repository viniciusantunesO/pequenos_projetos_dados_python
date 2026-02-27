# Análise de Transações Bancárias

Projeto de análise de dados utilizando Python e Pandas, com foco em simular um cenário bancário real.  
O objetivo é analisar transações de clientes, identificar padrões de consumo e treinar operações fundamentais usadas no dia a dia de um analista de dados.

---

## Objetivo do Projeto

- Simular um conjunto de transações bancárias
- Explorar e entender os dados
- Calcular métricas importantes para o negócio
- Identificar clientes de alto gasto
- Analisar gastos por estado e categoria
- Detectar possíveis outliers (valores fora do padrão)

---

## Dataset

O dataset foi **gerado artificialmente** para fins educacionais, simulando transações reais de clientes bancários.

### Principais colunas:
- `cliente_id`: identificador do cliente
- `estado`: estado do cliente
- `categoria`: categoria do gasto (Alimentação, Transporte, Lazer, etc.)
- `valor`: valor da transação
- `data`: data da transação
- `nivel_gasto`: classificação do gasto (Baixo, Médio, Alto)

---

## Etapas da Análise

### 1. Criação do DataFrame
- Geração de dados simulados
- Estruturação em DataFrame com Pandas

### 2. Exploração dos Dados
- Visualização das primeiras linhas (`head`)
- Análise de informações gerais (`info`)
- Estatísticas descritivas (`describe`)

### 3. Tratamento Inicial
- Verificação de valores nulos
- Análise da distribuição dos dados

### 4. Análises Realizadas
- Total gasto por cliente
- Cliente que mais gastou
- Média de gastos por estado
- Agrupamento de gastos por categoria
- Criação de coluna de classificação de gasto
- Identificação de possíveis outliers

---

## Tecnologias Utilizadas

- Python
- Pandas
- NumPy