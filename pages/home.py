from dash import html, register_page
import dash_bootstrap_components as dbc

register_page(__name__, path='/', name='Accueil')

layout = html.Div([
    # Hero Card
    dbc.Card([
        dbc.CardBody([
            html.H1("🚀 Projet Dash - Application Multi-Pages", className="display-5 text-primary font-weight-bold mb-3"),
            html.P(
                "Bienvenue sur notre application interactive de visualisation de données construite avec Python, Dash et Plotly Express.",
                className="lead text-dark mb-3"
            ),
            html.Hr(),
            html.P(
                "Cette application regroupe différents modules d'analyse et de données interactifs créés par les membres de l'équipe.",
                className="text-muted mb-0"
            )
        ])
    ], className="mb-4 shadow-sm border-0"),

    # Grid of Pages Overview
    html.H3("📌 Explorez les différentes pages", className="mb-3 text-secondary"),
    
    dbc.Row([
        # Card 1: Page 1 (Louis)
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5("📈 Page 1 (Louis)", className="mb-0 text-white"), className="bg-primary"),
                dbc.CardBody([
                    html.P("Évolution boursière des géants de la technologie (GAFAM & Netflix).", className="card-text fw-bold"),
                    html.Ul([
                        html.Li("Jeu de données : Stocks (Plotly)"),
                        html.Li("Sélection multi-entreprises"),
                        html.Li("Graphiques temporel (lignes) et comparatif (barres)")
                    ], className="small text-muted mb-3"),
                    dbc.Button("Accéder à la Page 1", href="/page-1", color="primary", outline=True, size="sm")
                ])
            ], className="h-100 shadow-sm")
        ], md=4, className="mb-4"),

        # Card 2: Bernice
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5("📊 Page Bernice", className="mb-0 text-white"), className="bg-success"),
                dbc.CardBody([
                    html.P("Analyse de l'espérance de vie et du PIB mondial par Accordéon.", className="card-text fw-bold"),
                    html.Ul([
                        html.Li("Jeu de données : Gapminder"),
                        html.Li("Filtres sous forme d'Accordéon Bootstrap"),
                        html.Li("Checklist continents, échelle Log, Slider années")
                    ], className="small text-muted mb-3"),
                    dbc.Button("Accéder à la page Bernice", href="/bernice", color="success", outline=True, size="sm")
                ])
            ], className="h-100 shadow-sm")
        ], md=4, className="mb-4"),

        # Card 3: Ilona
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5("📑 Page Ilona", className="mb-0 text-white"), className="bg-info"),
                dbc.CardBody([
                    html.P("Analyse de l'espérance de vie et du PIB mondial par Onglets.", className="card-text fw-bold"),
                    html.Ul([
                        html.Li("Jeu de données : Gapminder"),
                        html.Li("Filtres sous forme d'Onglets (Tabs Bootstrap)"),
                        html.Li("Checklist continents, échelle Log, Slider années")
                    ], className="small text-muted mb-3"),
                    dbc.Button("Accéder à la page Ilona", href="/ilona", color="info", outline=True, size="sm")
                ])
            ], className="h-100 shadow-sm")
        ], md=4, className="mb-4"),
    ]),

    # Technical Architecture & Features Card
    dbc.Card([
        dbc.CardBody([
            html.H4("🛠️ Architecture & Technologies", className="text-dark mb-3"),
            dbc.Row([
                dbc.Col([
                    html.H6("Technologies clés :", className="fw-bold text-primary"),
                    html.Ul([
                        html.Li("Dash Multi-Page Framework (use_pages=True)"),
                        html.Li("Plotly Express pour la génération de graphiques interactifs"),
                        html.Li("Dash Bootstrap Components pour le design moderne")
                    ])
                ], md=6),
                dbc.Col([
                    html.H6("Structure du projet :", className="fw-bold text-primary"),
                    html.Ul([
                        html.Li("app.py : point d'entrée principal et barre latérale de navigation"),
                        html.Li("pages/ : modules autonomes pour chaque page de l'application"),
                        html.Li("assets/ : logo et styles CSS personnalisés")
                    ])
                ], md=6)
            ])
        ])
    ], className="shadow-sm border-0 mt-2")
])