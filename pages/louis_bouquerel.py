from dash import html, dcc, register_page, callback, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

register_page(__name__, name='Valeurs Boursières', path='/page-1')

# Chargement du jeu de données des valeurs boursières Tech (Stocks dataset)
df_stocks = px.data.stocks()

# Dictionnaire pour des noms d'entreprises conviviaux
COMPANY_NAMES = {
    'GOOG': 'Google (Alphabet)',
    'AAPL': 'Apple',
    'AMZN': 'Amazon',
    'MSFT': 'Microsoft',
    'NFLX': 'Netflix',
    'FB': 'Meta (Facebook)'
}

company_options = [{'label': name, 'value': code} for code, name in COMPANY_NAMES.items()]
default_companies = ['GOOG', 'AAPL', 'AMZN', 'MSFT']

layout = html.Div([
    dbc.Card([
        dbc.CardBody([
            html.H2("📈 Évolution Boursière des Géants de la Tech", className="card-title text-primary font-weight-bold mb-2"),
            html.P(
                "Visualisation de l'évolution relative de la valeur en bourse des grandes entreprises technologiques (base 1.0 au début de la période).",
                className="card-text text-muted"
            )
        ])
    ], className="mb-4 shadow-sm"),

    dbc.Card([
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    html.Label("Sélectionner les entreprises :", className="fw-bold mb-1"),
                    dcc.Dropdown(
                        id='stocks-company-dropdown',
                        options=company_options,
                        value=default_companies,
                        multi=True,
                        placeholder="Choisir une ou plusieurs entreprises...",
                        className="mb-3"
                    )
                ], md=7),
                dbc.Col([
                    html.Label("Type de graphique :", className="fw-bold mb-1"),
                    dcc.RadioItems(
                        id='stocks-chart-type',
                        options=[
                            {'label': ' Évolution temporelle (Courbes)', 'value': 'line'},
                            {'label': ' Niveau actuel / récent (Barres)', 'value': 'bar'}
                        ],
                        value='line',
                        inputClassName="me-1",
                        labelClassName="me-3"
                    )
                ], md=5)
            ]),
            dcc.Graph(id='stocks-graph', config={'displayModeBar': True})
        ])
    ], className="shadow-sm")
])

@callback(
    Output('stocks-graph', 'figure'),
    [Input('stocks-company-dropdown', 'value'),
     Input('stocks-chart-type', 'value')]
)
def update_stocks_graph(selected_companies, chart_type):
    if not selected_companies:
        fig = px.line(title="Veuillez sélectionner au moins une entreprise.")
        fig.update_layout(template="plotly_white")
        return fig

    if chart_type == 'line':
        # Graphique en lignes : évolution temporelle
        fig = px.line(
            df_stocks,
            x='date',
            y=selected_companies,
            title="Évolution relative du cours de bourse",
            labels={
                'date': 'Date',
                'value': 'Valeur relative (Base 1.0)',
                'variable': 'Entreprise'
            },
            template="plotly_white"
        )
        
        # Remplacer les codes d'action par les vrais noms dans la légende
        fig.for_each_trace(lambda trace: trace.update(name=COMPANY_NAMES.get(trace.name, trace.name)))
        fig.update_layout(height=500, margin=dict(l=40, r=40, t=60, b=40))
        
    else:
        # Graphique en barres : dernière valeur enregistrée
        latest_row = df_stocks.iloc[-1]
        latest_data = [
            {'Entreprise': COMPANY_NAMES.get(c, c), 'Valeur': latest_row[c]}
            for c in selected_companies
        ]
        
        fig = px.bar(
            latest_data,
            x='Entreprise',
            y='Valeur',
            color='Entreprise',
            text_auto='.2f',
            title=f"Valeur relative à la dernière date ({latest_row['date']})",
            labels={'Valeur': 'Valeur relative'},
            template="plotly_white"
        )
        fig.update_layout(height=500, margin=dict(l=40, r=40, t=60, b=40), showlegend=False)

    return fig


