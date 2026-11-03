# Registro de Testes — Análise de Serviços Laboratoriais

## 1. Objetivo

Este documento registra os testes funcionais realizados no MVP de Análise de Serviços Laboratoriais, desenvolvido com Python, Pandas e Streamlit.

Os testes têm como objetivo verificar o funcionamento das funcionalidades implementadas, identificar limitações e registrar os resultados observados.

## 2. Ambiente de testes

- Linguagem: Python
- Biblioteca de análise: Pandas
- Framework da aplicação: Streamlit
- Fonte de dados: arquivo CSV com dados fictícios
- Tipo de teste: testes funcionais manuais

## 3. Testes realizados

| ID  | Funcionalidade           | Resultado esperado                                                | Resultado obtido                                                                                                                 |
|-----|--------------------------|-------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| T01 | Carregamento da base CSV | Carregar e exibir os registros                                    | Aprovado: a aplicação carregou o arquivo CSV e exibiu os registros sem erros.                                                    |
| T02 | Total de serviços        | Exibir a quantidade total de registros                            | Aprovado: o indicador apresentou corretamente a quantidade total de registros da base.                                           |
| T03 | Distribuição por tipo    | Apresentar a quantidade de serviços por categoria                 | Aprovado: o gráfico apresentou corretamente a quantidade de serviços em cada categoria.                                          |
| T04 | Qualidade dos dados      | Identificar datas ausentes, datas inconsistentes e tipos ausentes | Aprovado: os três indicadores apresentaram corretamente as quantidades de problemas inseridos intencionalmente na base fictícia. |
| T05 | Cálculo de duração       | Calcular a diferença entre as datas de início e conclusão         | Aprovado: a aplicação calculou corretamente as durações dos serviços válidos em dias corridos.                                   |
| T06 | Indicadores gerais       | Calcular média, mediana e maior duração                           | Aprovado: os indicadores foram calculados corretamente, considerando apenas os registros válidos.                                |
| T07 | Comparação por tipo      | Apresentar média e mediana para cada categoria                    | Aprovado: os gráficos e a tabela comparativa apresentaram corretamente as estatísticas de cada tipo de serviço.                  |
| T08 | Filtro interativo        | Atualizar os registros e indicadores conforme o tipo selecionado  | Aprovado: os registros, a média e a mediana foram atualizados corretamente para as três categorias.                              |

## 4. Limitações conhecidas

- A aplicação utiliza dados fictícios para fins acadêmicos.
- As durações são calculadas em dias corridos.
- Não existe integração com sistemas laboratoriais externos.
- A aplicação não utiliza modelos de Machine Learning.
- Registros com datas ausentes ou inconsistentes não participam dos cálculos de duração.

## 5. Considerações finais

Os testes funcionais têm como finalidade verificar se as funcionalidades implementadas atendem aos requisitos definidos para o MVP.

Os resultados e limitações registrados permitem avaliar o estado atual do produto e identificar possíveis melhorias para versões futuras.