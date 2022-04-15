# IMPORT MODULES
import dash
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_bootstrap_components as dbc


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO])
server = app.server
app.layout = html.Div(children=[
                            dbc.Row([
                                dbc.Col(html.H1("OPS score calculator", style={'textAlign': 'center'}),
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
                                            id='1',
                                            value='',
                                            # labelStyle={'display': 'inline-block', 'text-align': 'center','width': '100%'},
                                            style={'display': 'inline-block', 'text-align': 'center','display': 'flex', 'justify-content': 'space-evenly', 'width': '30%'},
                                        ),
                            ],),
                            dbc.Row(children=[
                                        html.H5("Maakt de kandidaat een verwarde indruk?",
                                                 style={ "display": "inline-block", 'textAlign': 'center', "width": "50%",}),
                                        dcc.RadioItems(
                                            options=[
                                                {'label': 'Ja', 'value': '1'},
                                                {'label': 'Twijfel', 'value': '2'},
                                                {'label': 'Nee', 'value': '3'}
                                            ],
                                            id='2',
                                            value='',
                                            # labelStyle={'display': 'inline-block', 'text-align': 'center','width': '100%'},
                                            style={'display': 'inline-block', 'text-align': 'center','display': 'flex', 'justify-content': 'space-evenly', 'width': '30%'},
                                        ),
                            ],),
                            dbc.Row(children=[
                                html.H5("Heeft de kandidaat een gestoorde oriëntatie in tijd en/ of plaats? ",
                                        style={"display": "inline-block", 'textAlign': 'center', "width": "50%", }),
                                dcc.RadioItems(
                                    options=[
                                        {'label': 'Ja', 'value': '1'},
                                        {'label': 'Twijfel', 'value': '2'},
                                        {'label': 'Nee', 'value': '3'}
                                    ],
                                    id='3',
                                    value='',
                                    # labelStyle={'display': 'inline-block', 'text-align': 'center','width': '100%'},
                                    style={'display': 'inline-block', 'text-align': 'center', 'display': 'flex',
                                           'justify-content': 'space-evenly', 'width': '30%'},
                                ),
                            ], ),
                            dbc.Row(children=[
                                html.H3("O-Score", style={"display": "inline-block", 'textAlign': 'center', "width": "50%", }),
                                html.H3("outcome", id='output-O',
                                        style={"display": "inline-block", 'textAlign': 'center', "width": "30%", }, )
                            ]),
                            dbc.Row([
                                html.H3("Praktische vaardigheden & aandacht", style={"display": "inline-block", 'textAlign': 'center', "width": "100%", }),
                            ]),
                            dbc.Row(children=[
                                html.H5("Komt de kandidaat traag over? ",
                                        style={"display": "inline-block", 'textAlign': 'center', "width": "50%", }),
                                dcc.RadioItems(
                                    options=[
                                        {'label': 'Ja', 'value': '1'},
                                        {'label': 'Twijfel', 'value': '2'},
                                        {'label': 'Nee', 'value': '3'}
                                    ],
                                    id='4',
                                    value='',
                                    # labelStyle={'display': 'inline-block', 'text-align': 'center','width': '100%'},
                                    style={'display': 'inline-block', 'text-align': 'center', 'display': 'flex',
                                           'justify-content': 'space-evenly', 'width': '30%'},
                                ),
                            ], ),
                            dbc.Row(children=[
                                html.H5(" Heeft de kandidaat moeite met het uitvoeren van dagelijkse praktische handelingen? ",
                                        style={"display": "inline-block", 'textAlign': 'center', "width": "50%", }),
                                dcc.RadioItems(
                                    options=[
                                        {'label': 'Ja', 'value': '1'},
                                        {'label': 'Twijfel', 'value': '2'},
                                        {'label': 'Nee', 'value': '3'}
                                    ],
                                    id='5',
                                    value='',
                                    # labelStyle={'display': 'inline-block', 'text-align': 'center','width': '100%'},
                                    style={'display': 'inline-block', 'text-align': 'center', 'display': 'flex',
                                           'justify-content': 'space-evenly', 'width': '30%'},
                                ),
                            ], ),
                            dbc.Row(children=[
                                html.H5("Verwaarloost de kandidaat zijn/ haar uiterlijk?",
                                        style={"display": "inline-block", 'textAlign': 'center', "width": "50%", }),
                                dcc.RadioItems(
                                    options=[
                                        {'label': 'Ja', 'value': '1'},
                                        {'label': 'Twijfel', 'value': '2'},
                                        {'label': 'Nee', 'value': '3'}
                                    ],
                                    id='6',
                                    value='',
                                    # labelStyle={'display': 'inline-block', 'text-align': 'center','width': '100%'},
                                    style={'display': 'inline-block', 'text-align': 'center', 'display': 'flex',
                                           'justify-content': 'space-evenly', 'width': '30%'},
                                ),
                            ], ),
                            dbc.Row(children=[
                                html.H3("P-Score", style={"display": "inline-block", 'textAlign': 'center', "width": "50%", }),
                                html.H3("outcome", id='output-P',
                                        style={"display": "inline-block", 'textAlign': 'center', "width": "30%", }, )
                            ]),
                            dbc.Row([
                                html.H3("Sociaal & persoonlijk functioneren ",
                                        style={"display": "inline-block", 'textAlign': 'center', "width": "100%", }),
                            ]),
                            dbc.Row(children=[
                                html.H5("Is de kandidaat snel afgeleid?",
                                        style={"display": "inline-block", 'textAlign': 'center', "width": "50%", }),
                                dcc.RadioItems(
                                    options=[
                                        {'label': 'Ja', 'value': '1'},
                                        {'label': 'Twijfel', 'value': '2'},
                                        {'label': 'Nee', 'value': '3'}
                                    ],
                                    id='7',
                                    value='',
                                    # labelStyle={'display': 'inline-block', 'text-align': 'center','width': '100%'},
                                    style={'display': 'inline-block', 'text-align': 'center', 'display': 'flex',
                                           'justify-content': 'space-evenly', 'width': '30%'},
                                ),
                            ], ),
                            dbc.Row(children=[
                                html.H5("Gedraagt de kandidaat zich inadequaat in het persoonlijk contact?",
                                        style={"display": "inline-block", 'textAlign': 'center', "width": "50%", }),
                                dcc.RadioItems(
                                    options=[
                                        {'label': 'Ja', 'value': '1'},
                                        {'label': 'Twijfel', 'value': '2'},
                                        {'label': 'Nee', 'value': '3'}
                                    ],
                                    id='8',
                                    value='',
                                    # labelStyle={'display': 'inline-block', 'text-align': 'center','width': '100%'},
                                    style={'display': 'inline-block', 'text-align': 'center', 'display': 'flex',
                                           'justify-content': 'space-evenly', 'width': '30%'},
                                ),
                            ], ),
                            dbc.Row(children=[
                                html.H5("Wijkt de zelfinschatting van de kandidaat af van uw eigen inschatting?",
                                        style={"display": "inline-block", 'textAlign': 'center', "width": "50%", }),
                                dcc.RadioItems(
                                    options=[
                                        {'label': 'Ja', 'value': '1'},
                                        {'label': 'Twijfel', 'value': '2'},
                                        {'label': 'Nee', 'value': '3'}
                                    ],
                                    id='9',
                                    value='',
                                    # labelStyle={'display': 'inline-block', 'text-align': 'center','width': '100%'},
                                    style={'display': 'inline-block', 'text-align': 'center', 'display': 'flex',
                                           'justify-content': 'space-evenly', 'width': '30%'},
                                ),
                            ], ),
                            dbc.Row(children=[
                                html.H3("S-Score", style={"display": "inline-block", 'textAlign': 'center', "width": "50%", }),
                                html.H3("outcome", id='output-S',
                                        style={"display": "inline-block", 'textAlign': 'center', "width": "30%", }, )
                            ]),
                            dbc.Row([
                                html.H3("", style={"display": "inline-block", 'textAlign': 'center', "width": "100%", }),
                            ]),
                            dbc.Row(children=[
                                html.H3("Totale Score", style={"display": "inline-block", 'textAlign': 'center', "width": "50%", }),
                                html.H3("outcome", id='output-OPS-total',
                                    style={"display": "inline-block", 'textAlign': 'center', "width": "30%", },)
                                ]),
    dbc.Row(children=[
        html.H2(""),
    ]),
dbc.Row(children=[
    dcc.Link("See the GitHub repo", href="https://github.com/KelvinKramp/medical-calculator",style={"display": "inline-block", 'textAlign': 'right', "width": "50%", }),
]),
dbc.Row(children=[
    dcc.Link("Read the Medium post", href="https://k-h-kramp.medium.com/ops-calculator-in-dash-with-python-d236f478f764",style={"display": "inline-block", 'textAlign': 'right', "width": "50%", }),
]),
                        ])


### CALLBACKS ## the numbers are LETTER O followed by a number
@app.callback(
    Output('output-OPS-total', 'children'),
    Output('output-O', 'children'),
    Output('output-P', 'children'),
    Output('output-S', 'children'),
    [Input('1', 'value'),
     Input('2', 'value'),
     Input('3', 'value'),
     Input('4', 'value'),
     Input('5', 'value'),
     Input('6', 'value'),
     Input('7', 'value'),
     Input('8', 'value'),
     Input('9', 'value')])
def calc(Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9):
    l = [Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9]
    l_total, l_o, l_p, l_s   = [], [], [], []
    for i in l:
        if i:
            l_total.append(int(i))
    for i in l[0:3]:
        if i:
            l_o.append(int(i))
    for i in l[3:6]:
        if i:
            l_p.append(int(i))
    for i in l[6:9]:
        if i:
            l_s.append(int(i))
    return sum(l_total),sum(l_o),sum(l_p),sum(l_s)

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080, debug=True, use_reloader=True)
