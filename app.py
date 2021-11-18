import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import random


app = dash.Dash(
    __name__,
    meta_tags=[{'name': 'viewport', 'content': 'width=device-width'}],
)

server = app.server

app.title = 'Multiplication Quiz'

app.config.update({
    'suppress_callback_exceptions': True,
})

global_factor_1 = 4
factor_2 = random.randint(1,12)

app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [

                    ],
                ),
                html.Div(
                    [
                        html.Button(['Start'],
                                    n_clicks=0,
                                    id='start-button',
                                    className='button',
                                    style={'display': 'inline-block',
                                           'fontSize': '18px'},
                                   ),
                    ],
                    id='start-button-container',
                    style={'display': 'inline-block'}
                ),
                html.Div(
                    [

                    ],
                ),
            ],
            style={'marginTop': '75px',
                   'marginRight': '5px',
                   'marginLeft': '5px',
                   'display': 'flex',
                   'justifyContent': 'space-between'}
        ),
        html.Div(
            [
                html.Label(
                    [
                        global_factor_1
                    ],
                    id='factor-1-container',
                    style={'display': 'inline-block',
                           'width': '45%',
                           'textAlign': 'right'
                          },
                ),
                html.Label(
                    [
                        'x'
                    ],
                    id='multiplication-sign',
                    style={'display': 'inline-block',
                           'width': '8%'
                          },
                ),
                html.Label(
                    [
                        factor_2
                    ],
                    id='factor-2-container',
                    style={'display': 'inline-block',
                           'width': '45%',
                           'textAlign': 'left'
                          },
                ),
            ],
            id='factor-container',
            style={'marginTop': '75px',
                   'width': '80%',
                   'display': 'flex',
                   'textAlign': 'center',
                   'justifyContent': 'space-between'}
        ),
        html.Div(
            [
                dcc.Input(id='answer-input', n_submit=0, placeholder='Enter the product', autoComplete='off')
            ],
            id='answer-container',
            style={'display': 'inline-block', 'textAlign': 'center'}
        ),
        html.Div([
                html.Label(
                    [
                        'Score'
                    ],
                    id='score-label',
                    style={'display': 'inline-block',
                           'width': '100%',
                           'textAlign': 'center',
                          },
                ),
        ],
            id='score-label-container',
            style={'marginTop': '75px',
                   'width': '100%',
                   'display': 'flex',
                   'textAlign': 'center',
                   'justifyContent': 'space-between'}
        ),
        html.Div(
            [
                html.Label(
                    [
                        '0'
                    ],
                    id='correct-container',
                    style={'display': 'inline-block',
                           'width': '45%',
                           'textAlign': 'right'
                          },
                ),
                html.Label(
                    [
                        '/'
                    ],
                    id='div-sign',
                    style={'display': 'inline-block',
                           'width': '8%'
                          },
                ),
                html.Label(
                    [
                        '0'
                    ],
                    id='total-container',
                    style={'display': 'inline-block',
                           'width': '45%',
                           'textAlign': 'left'
                          },
                ),
            ],
            id='score-container',
            style={'marginTop': '75px',
                   'width': '80%',
                   'display': 'flex',
                   'textAlign': 'center',
                   'justifyContent': 'space-between'}
        ),
        # hidden divs
        html.Div([
            dcc.Input(id='correct-val', value=0),
            dcc.Input(id='total-val', value=0),
        ],
            style={'display': 'none'}
        ),
    ],
    style = {
        'textAlign': 'center',
        'fontFamily': 'Arial, Helvetica, sans-serif',
        'fontSize': '140px',
        'fontWeight': 'bold',
    },
)

@app.callback(
    [Output('start-button-container', 'style'),
     Output('factor-container', 'style'),
     Output('answer-container', 'style'),
     Output('score-container', 'style'),
     Output('score-label-container', 'style')],
    Input('start-button', 'n_clicks')
)
def show_contents(n_clicks):
    if n_clicks > 0:
        start_button_style = {'display': 'none'}
        main_container_style = {'marginTop': '75px',
                                'marginRight': '5px',
                                'marginLeft': '5px',
                                'display': 'flex',
                                'justifyContent': 'space-between'}
        answer_style={'display': 'inline-block', 'textAlign': 'center'}
        score_container_style = {'marginTop': '15px',
                                'marginRight': '5px',
                                'marginLeft': '5px',
                                'display': 'flex',
                                 'fontSize': '22px',
                                'justifyContent': 'space-between'}
        score_label_container_style = {'marginTop': '75px',
                                'marginRight': '5px',
                                'marginLeft': '5px',
                                'display': 'flex',
                                 'fontSize': '22px',
                                'justifyContent': 'space-between'}
    else:
        start_button_style = {'display': 'inline-block'}
        main_container_style = {'marginTop': '75px',
                                'marginRight': '5px',
                                'marginLeft': '5px',
                                'display': 'none',
                                'justifyContent': 'space-between'}
        answer_style={'display': 'none', 'textAlign': 'center'}
        score_container_style = {'marginTop': '15px',
                                'marginRight': '5px',
                                'marginLeft': '5px',
                                'display': 'none',
                                 'fontSize': '22px',
                                'justifyContent': 'space-between'}
        score_label_container_style = {'marginTop': '75px',
                                'marginRight': '5px',
                                'marginLeft': '5px',
                                'display': 'none',
                                 'fontSize': '22px',
                                'justifyContent': 'space-between'}

    return [start_button_style,
            main_container_style,
            answer_style,
            score_container_style,
            score_label_container_style]

@app.callback(
    [Output('factor-1-container', 'children'),
     Output('factor-2-container', 'children'),
     Output('answer-input', 'value'),
     Output('correct-val', 'value'),
     Output('total-val', 'value')],
    [Input('answer-input', 'n_submit'),
     State('answer-input', 'value'),
     State('factor-1-container', 'children'),
     State('factor-2-container', 'children'),
     State('correct-val', 'value'),
     State('total-val', 'value')],
)
def check_answer(n_submit, answer, val_1, val_2, correct, total):
    factor_1_children = val_1
    factor_2_children = val_2
    if n_submit > 0:
        if answer is None or answer == '':
            total = str(int(total)+1)
        else:
            if int(val_1[0])*int(val_2[0])-int(answer)==0:
                switch = random.randint(0,1)
                factor_1 = global_factor_1
                factor_2 = random.randint(1,12)
                product = factor_1 * factor_2
                if switch:
                    factor_1, factor_2 = factor_2, factor_1
                factor_1_children = [str(factor_1)]
                factor_2_children = [str(factor_2)]
                answer = None
                correct = str(int(correct)+1)
                total = str(int(total)+1)
            else:
                answer = None
                total = str(int(total)+1)

    return factor_1_children, factor_2_children, answer, correct, total

@app.callback(
    [Output('correct-container', 'children'),
     Output('total-container', 'children')],
    [Input('correct-val', 'value'),
     Input('total-val', 'value')]
)
def update_score(correct, total):
    return [[correct], [total]]

if __name__ == '__main__':
    # app.run_server(debug=False, host='10.0.2.15', port='8050')
    app.run_server(debug=False)


