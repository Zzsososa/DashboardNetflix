import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd

# Paso 1: Cargar el dataset
df = pd.read_csv("netflix-titles (1).csv")

# Paso 2: Los 10 directores con más películas/series en Netflix
top_directors = df['director'].value_counts().head(10)

# Paso 3: Comparativa de la cantidad de series vs películas
series_vs_movies = df['type'].value_counts()

# Paso 4: Comparativa de las 5 clasificaciones con más títulos
top_listed_in = df['listed_in'].value_counts().head(5)

# Crear la aplicación Dash
app = dash.Dash(__name__)

# Layout del dashboard
app.layout = html.Div([
    html.H1("Dashboard de Netflix"),
    
    html.Div([
        html.Div([
            dcc.Graph(
                id='top-directors',
                figure={
                    'data': [
                        go.Bar(
                            x=top_directors.values,
                            y=top_directors.index,
                            orientation='h'
                        )
                    ],
                    'layout': go.Layout(
                        title='Top 10 Directores con más películas/series en Netflix',
                        xaxis={'title': 'Cantidad de películas/series'},
                        yaxis={'title': 'Director'}
                    )
                }
            )
        ], className='six columns'),
        
        html.Div([
            dcc.Graph(
                id='series-vs-movies',
                figure={
                    'data': [
                        go.Bar(
                            x=series_vs_movies.index,
                            y=series_vs_movies.values
                        )
                    ],
                    'layout': go.Layout(
                        title='Cantidad de series vs películas en Netflix',
                        xaxis={'title': 'Tipo'},
                        yaxis={'title': 'Cantidad'}
                    )
                }
            )
        ], className='six columns'),
    ], className='row'),
    
    html.Div([
        dcc.Graph(
            id='top-listed-in',
            figure={
                'data': [
                    go.Bar(
                        x=top_listed_in.values,
                        y=top_listed_in.index,
                        orientation='h'
                    )
                ],
                'layout': go.Layout(
                    title='Top 5 Clasificaciones con más títulos en Netflix',
                    xaxis={'title': 'Cantidad de títulos'},
                    yaxis={'title': 'Clasificación'}
                )
            }
        )
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
