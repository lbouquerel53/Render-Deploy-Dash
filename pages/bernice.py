from dash import Dash, html, dcc, callback, Input, Output, register_page
import dash_bootstrap_components as dbc
import plotly.express as px


register_page(__name__, name='Bernice')

# Recuperation du dataset Gapminder
df = px.data.gapminder()

# Recuperation du minimum et du maximum des annees disponibles
min_year, max_year = df.year.min(), df.year.max()

# Creation des markers pour le slider sur les annees
slider_marks = {str(year): str(year) for year in df.year.unique()}

# Recuperation de la liste des continents 
opt_continent = df.continent.unique()

# Creation des options du radio items pour l'activation du logarithme sur l'axe des x
opt_log = [{'label': 'Activée', 'value': True}, {'label': 'Désactivée', 'value': False}]

#-----------------------------------------------------------------------#
# Interface                                                             #
#-----------------------------------------------------------------------#

layout = html.Div([

    # Titre de l'application
    html.H1("Gapminder dataset : Checklist & Slider"),

    dbc.Accordion([
        dbc.AccordionItem(
            title="Sélection des continents", 
            children=[dcc.Checklist(id='checklist', options=opt_continent, value=opt_continent, inline=True)]
        ),

        dbc.AccordionItem(
            title="Transformation logarithmique du PIB par tête (gdpPercap)",
            children=[dcc.RadioItems(id='radio', options=opt_log, value=True)]
        ),

        dbc.AccordionItem(
            title="Sélection de l'année",
            children=[dcc.Slider(id='slider', min=min_year , max=max_year , value=max_year,
               marks=slider_marks, step = None)]
        )
    ]),

    # Affichage du graphique LifeExp by GDPperCap
    dcc.Graph(id='graph-gdp', figure={})

])

#-----------------------------------------------------------------------#
# Serveur                                                               #
#-----------------------------------------------------------------------#

@callback(
    Output('graph-gdp', 'figure'),
    Input('slider', "value"),
    Input('checklist', "value"),
    Input('radio', 'value')
)
def update_graph(year_value, continent_value, log_boolean):
    df_update = df[(df.year == year_value) & df.continent.isin(continent_value)]
    fig = px.scatter(df_update, 
                     x="gdpPercap",
                     y="lifeExp", 
                     size="pop",
                     color="continent",
                     hover_name="country",
                     log_x=log_boolean,
                     size_max=60,
                     title=f'Life expectancy by GDP per capita and population in {year_value}')
    if log_boolean:
        fig.update_xaxes(type="log", range=[2,5])
    else :
        fig.update_xaxes(range=[-5000,50000])
    fig.update_yaxes(range=[20, 100])

    return fig
