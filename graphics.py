# Autor: Lucas Cavalcante
# Atualizado em: 04/02/2023

import boa_dbm as boa

data_creditos = boa.credits_data

for i in range(len(data_creditos)):
    data_creditos[i][1] = abs( boa.credits_data[i][1] - boa.credits_data[i][0] )

labels = ['Falta Cumprir','Cumpridos']
colors = ['IndianRed','DarkSeaGreen']

from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Criando grade de plots, um elemento para cada tipo de atividade
fig = make_subplots(        rows=2, 
                            cols=2,
                            specs=[[{"type":"domain"},{"type":"domain"}],
                                    [{"type":"domain"},{"type":"domain"}]],
)

titulos = [['Atividades Obrigatórias','Atividades Optativas'],
            ['Atividades Optativas (Escolha Restrita)','Livre Escolha']]

# Adicionando gráficos na grade (Tentando portar para um método DRY)
iter = 0
for i in [1,2]:
    for j in [1,2]:
        fig.add_trace(go.Pie(
                    values=data_creditos[iter],
                    labels=labels,
                    title=titulos[i-1][j-1],
                    title_font_size=24,
                    marker_colors=colors),
                    row=i, col=j)
        iter+=1



fig.update_layout(height=700, width=700, showlegend=False, title='Créditos', title_font_size=36)


# Exportando para HTML
fig.write_html('boa_graph.html', auto_open=True)