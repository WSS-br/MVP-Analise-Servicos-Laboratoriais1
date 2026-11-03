# Análise de Serviços Laboratoriais

## 1. Sobre o projeto

Este projeto consiste em um Produto de Dados desenvolvido como parte do Projeto Integrador III do curso de Ciência de Dados.

A aplicação tem como objetivo analisar os tempos de execução de serviços laboratoriais, permitindo visualizar informações, identificar problemas de qualidade nos dados e comparar durações entre diferentes tipos de serviço.

A proposta é oferecer uma ferramenta de apoio à análise e ao planejamento de atividades laboratoriais, facilitando a compreensão dos tempos de execução dos serviços.

**Importante:** a base utilizada nesta versão contém dados fictícios, desenvolvidos exclusivamente para fins acadêmicos e de demonstração. Portanto, os resultados não representam o desempenho real de um laboratório.

## 2. Funcionalidades

A aplicação disponibiliza os seguintes recursos:

- Carregamento e visualização dos registros de serviços laboratoriais.
- Exibição da quantidade total de serviços.
- Contagem de serviços por tipo.
- Identificação de datas de conclusão ausentes.
- Identificação de registros com data de conclusão anterior à data de início.
- Identificação de registros sem tipo de serviço informado.
- Cálculo da duração dos serviços em dias corridos.
- Cálculo da média e da mediana das durações.
- Identificação da maior duração registrada.
- Comparação das durações médias e medianas por tipo de serviço.
- Filtro interativo para selecionar um tipo de serviço e visualizar suas estatísticas.

## 3. Tecnologias utilizadas

- **Python:** linguagem de programação utilizada no desenvolvimento.
- **Pandas:** manipulação, organização e análise dos dados.
- **Streamlit:** desenvolvimento da interface interativa da aplicação.

## 4. Estrutura do projeto

```text
MVP_laboratorio/
│
├── dados/
│   └── base_ficticia_servicos_laboratorio.csv
│
├── app.py
├── requirements.txt
└── README.md
```

**Descrição dos arquivos:**

- `app.py`: código principal da aplicação.
- `requirements.txt`: dependências necessárias para executar o projeto.
- `dados/base_ficticia_servicos_laboratorio.csv`: base de dados utilizada pela aplicação.
- `README.md`: documentação do projeto.

## 5. Como executar a aplicação

### Pré-requisitos

- Python instalado.
- Pip instalado.
- Arquivos do projeto disponíveis localmente.

### Instalação

Primeiro, clone ou baixe o repositório e acesse a pasta do projeto.

Crie um ambiente virtual:

```bash
python3 -m venv .venv
```

Ative o ambiente virtual no Linux:

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

### Execução

Na raiz do projeto, execute:

```bash
streamlit run app.py
```

A aplicação será disponibilizada localmente pelo Streamlit. O endereço de acesso será exibido no terminal.

## 6. Dados utilizados

A aplicação utiliza um arquivo CSV contendo registros fictícios de serviços laboratoriais.

Os dados possuem as seguintes informações:

| Campo                 | Descrição                                     |
|-----------------------|-----------------------------------------------|
| `id_servico`          | Identificador do serviço                      |
| `tipo_servico`        | Categoria do serviço realizado                |
| `produto_equipamento` | Produto ou equipamento relacionado ao serviço |
| `data_inicio`         | Data de início do serviço                     |
| `data_conclusao`      | Data de conclusão do serviço                  |

A duração é calculada pela diferença entre a data de conclusão e a data de início, considerando dias corridos.

## 7. Tratamento e qualidade dos dados

Antes do cálculo das durações, a aplicação verifica se os registros possuem datas de início e conclusão preenchidas e se a data de conclusão não é anterior à data de início.

Os registros que não atendem a essas condições são excluídos dos cálculos de duração.

A aplicação também apresenta indicadores relacionados a datas de conclusão ausentes, datas inconsistentes e tipos de serviço não informados.

## 8. Limitações conhecidas

- A aplicação utiliza uma base fictícia, não representando dados operacionais reais.
- Os cálculos consideram dias corridos, não horas ou dias úteis.
- A aplicação não possui integração com sistemas laboratoriais externos.
- Não utiliza modelos de Machine Learning ou mecanismos de previsão.
- Os resultados dependem da qualidade e da consistência dos dados fornecidos.

## 9. Possíveis melhorias futuras

- Implementação de filtros adicionais.
- Identificação e sinalização de durações atípicas.
- Desenvolvimento de novas visualizações.
- Integração com bancos de dados.
- Ampliação das análises estatísticas.
- Implementação de métodos de previsão de tempos de execução.

## 10. Finalidade acadêmica

Este projeto foi desenvolvido para demonstrar a aplicação de conceitos de Ciência de Dados na análise de informações relacionadas a serviços laboratoriais, integrando preparação de dados, análise exploratória e desenvolvimento de uma aplicação interativa.