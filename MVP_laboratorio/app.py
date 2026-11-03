import streamlit as st
import pandas as pd

# Rodar no terminal: streamlit run app.py

st.title('Análise de Serviços Laboratoriais')
st.write('Ferramenta para análise dos tempos de execução de serviços laboratoriais')
st.write('Nota: dados fictícios.')

df = pd.read_csv('dados/base_ficticia_servicos_laboratorio.csv')

df['data_inicio'] = pd.to_datetime(df['data_inicio'])
df['data_conclusao'] = pd.to_datetime(df['data_conclusao'])

st.dataframe(
    df.style.format({
        'data_inicio': lambda x: x.strftime('%d/%m/%Y') if pd.notna(x) else '',
        'data_conclusao': lambda x: x.strftime('%d/%m/%Y') if pd.notna(x) else ''
    })
)

total_servicos = df.shape[0]

servicos_por_tipo = df['tipo_servico'].value_counts()

st.metric('Total de serviços', total_servicos)

st.write(servicos_por_tipo)

st.bar_chart(servicos_por_tipo)

condicao = (df['data_inicio'].notna() &
            df['data_conclusao'].notna() &
            (df['data_conclusao'] >= df['data_inicio']))

df_validos = df[condicao].copy()
df_validos['duracao_dias'] = (df_validos['data_conclusao'] - df_validos['data_inicio']).dt.days

st.write('Dados válidos',df_validos)

ausentes = df['data_conclusao'].isna().sum()
antes_inicio = (df['data_conclusao'] < df['data_inicio']).sum()
servicos_ausentes = df['tipo_servico'].isna().sum()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric('Data de conclusão ausente',ausentes)
with col2:
    st.metric('Dados inconsistentes',antes_inicio)
with col3:
    st.metric('Serviços ausentes',servicos_ausentes)

media_duracao = df_validos['duracao_dias'].mean()
mediana_duracao = df_validos['duracao_dias'].median()
maior_duracao = df_validos['duracao_dias'].max()

col4, col5, col6 = st.columns(3)
with col4:
    st.metric('Média de duração (dias)',f'{media_duracao:.2f}')
with col5:
    st.metric('Mediana de duração (dias)',f'{mediana_duracao:.2f}')
with col6:
    st.metric('Maior duração (dias)',f'{maior_duracao:.2f}')

duracao_por_tipo = df_validos.groupby('tipo_servico')['duracao_dias'].mean()
duracao_por_tipo_mediana = df_validos.groupby('tipo_servico')['duracao_dias'].median()

st.write('Duração média por tipo de serviço')
st.write(duracao_por_tipo)

st.bar_chart(duracao_por_tipo)

st.write('Duração mediana por tipo de serviço')
st.write(duracao_por_tipo_mediana)

st.bar_chart(duracao_por_tipo_mediana)

comparacao_duracoes = pd.DataFrame({
    'Média (dias)': duracao_por_tipo,
    'Mediana (dias)': duracao_por_tipo_mediana,
})

st.dataframe(comparacao_duracoes)

servicos_por_tipo = df['tipo_servico'].unique()

tipo_selecionado = st.selectbox('Selecione o tipo de serviço', servicos_por_tipo)

df_filtrado = df_validos[
    df_validos['tipo_servico'] == tipo_selecionado
].copy()

st.write(df_filtrado)

duracao_por_tipo = df_filtrado['duracao_dias'].mean()
duracao_por_tipo_mediana = df_filtrado['duracao_dias'].median()

col7, col8 = st.columns(2)

with col7:
    st.metric('Média (dias)', f'{duracao_por_tipo:.2f}')
with col8:
    st.metric('Mediana (dias)', f'{duracao_por_tipo_mediana:.2f}')