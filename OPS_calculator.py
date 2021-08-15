# IMPORT MODULES
import dash
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from datetime import datetime as dt
import subprocess

try:
    subprocess.run("lsof -t -i tcp:8080 | xargs kill -9", shell=False) # kill the server
except Exception as e:
    print(e)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO])
app.layout = html.Div(children=[
                            dbc.Row([
                                dbc.Col(html.H1("OPS score calulator", style={'textAlign': 'center'}),
                                        width=12)
                            ]),
                            dbc.Row([
                                html.H3("Oriëntatie & geheugen",style={ "display": "inline-block", 'textAlign': 'center', "width": "100%",}),
                                ]),
                            dbc.Row(children=[
                                        html.H5("Komt de kandidaat vergeetachtig over? ",
                                                 style={ "display": "inline-block", 'textAlign': 'center', "width": "50%",}),
                                        dcc.RadioItems(
                                            options=[
                                                {'label': 'Ja', 'value': '1'},
                                                {'label': 'Twijfel', 'value': '2'},
                                                {'label': 'Nee', 'value': '3'}
                                            ],
                                            value='3',
                                            # labelStyle={'display': 'inline-block', 'text-align': 'center','width': '100%'},
                                            style={'display': 'inline-block', 'text-align': 'center','display': 'flex', 'justify-content': 'space-evenly', 'width': '30%'},
                                        ),
                            ],
                            )
                        ])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080, debug=True, use_reloader=False)
