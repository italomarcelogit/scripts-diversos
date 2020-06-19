import dash
import dash_core_components as dcc
import dash_html_components as html
import dataset as myds


KPI1 = myds.KPI1
KPI2 = myds.KPI2


KPI31 = myds.KPI31 # Product top 1 - name - 2019
KPI32 = myds.KPI32 # Product top 1 - units - 2019

KPI41 = myds.KPI41 # Product top 1 - name - 2019
KPI42 = myds.KPI42 # Product top 1 - units - 2019

# data graphOne - bar -
xg1 = myds.xg1 # return product names
yg1 = myds.yg1 # return product units

# data graphTwo
xg2 = myds.xg2 # return months 2019 jan to dec
yg2 = myds.yg2 # return

# data to line sales person
# data to card best sales person
nomeV = myds.nomeV
pmvStr = f'Produto mais vendido: {myds.pmv.index[0]} - {myds.pmv.QTDE[0]} units'
mfStr = f'Maior faturamento: US${myds.mf.TOTAL.values}. Ref.: {myds.mf.index[0]}/2019 '
# data to sales numbers
xg3 = myds.tvpmpv.index
yg3 = myds.tvpmpv.values

#         success     primary    info     warning     danger
cores = ['#00bc8c', '#28415b', '#217dbb','#c87f0a', '#dc2c1a']


app = dash.Dash(__name__, external_stylesheets=['https://bootswatch.com/3/darkly/bootstrap.css'])

app.layout = html.Div([
    # row 1 - linha 1
    html.Div([
        html.H1('DASHBOARD - VENDAS - 2019')
    ], className='col-xs-12'),

    # row 2 - linha 2 - creating filter
    html.Div([
        html.Nav([
            html.Div([
                html.P('Filtro: ', className='navbar-brand')
            ], className='navbar-header'),
            html.Div([
                html.Label('Produto'),
                html.Select([
                    html.Option('A', value='A'),
                    html.Option('B', value='B')
                ], className='form-control')
            ], className='col-xs-2'),
            html.Div([
                html.Label('Cat. Produto'),
                html.Select([
                    html.Option('A', value='A'),
                    html.Option('B', value='B', selected='selected')
                ], className='form-control')
            ], className='col-xs-2'),
            html.Div([
                html.Label('Vendedor'),
                html.Select([
                    html.Option('Ana', value='A'),
                    html.Option('Beatriz', value='B', selected='selected'),
                    html.Option('Carlos', value='C', selected='selected')
                ], className='form-control')
            ], className='col-xs-2'),
            html.Div([
                html.Br(),
                html.Button('Filtrar', type='submit', className='btn btn-default')
            ], className='col-xs-2'),

        ], className='nav navbar-default'),
    ], className='col-xs-12 well'),

    # row 3 - linha 3 - showing 4 kpis
    html.Div([
        # indicador 1 - kpi 1
        html.Div([
            html.Div([
                html.Div([
                    html.H4('Qtde. Vendida', className='panel-title text-center')
                ], className='panel-heading'),
                html.Div([
                    html.H1(KPI1, className='text-center')
                ])
            ], className='panel panel-warning')
        ], className='col-xs-3'),
        # indicador 2 - kpi 2
        html.Div([
            html.Div([
                html.Div([
                    html.H4('Total  Vendido', className='panel-title text-center')
                ], className='panel-heading'),
                html.Div([
                    html.H1(KPI2, className='text-center')
                ])
            ], className='panel panel-success')
        ], className='col-xs-3'),
        # indicador 3 - kpi 3
        html.Div([
            html.Div([
                html.Div([
                    html.H4('Melhor Produto', className='panel-title text-center')
                ], className='panel-heading'),
                html.Div([
                    html.H1(f' {KPI31} - {KPI32} units', className='text-center')
                ])
            ], className='panel panel-info')
        ], className='col-xs-3'),
        # indicador 4 - kpi 4
        html.Div([
            html.Div([
                html.Div([
                    html.H4('Produto em alerta', className='panel-title text-center')
                ], className='panel-heading'),
                html.Div([
                    html.H1(f'{KPI41} - {KPI42} units', className='text-center')
                ])
            ], className='panel panel-info')
        ], className='col-xs-3'),

    ], className='col-xs-12 well'),

    # row 4 - linha 4 - graphs top 5 and sales year 2019
    html.Div([
        # graph Bar
        html.Div([
            dcc.Graph(
                id='graphOne',
                figure={
                    'data': [{
                        'x': xg1, 'y': yg1, 'type': 'bar',
                        'marker': {'color': cores},
                        'name': 'Produtos'
                    }],
                    'layout': {
                        'title': 'Top 5 Products - 2019',
                        'showlegend': False,
                        'showgrid': False,
                        # background transparent
                        'plot_bgcolor': 'rgba(0,0,0,0)',
                        'paper_bgcolor': 'rgba(0,0,0,0)',
                        'font': {'color': 'white'}
                    }
                }
            )
        ], className='col-xs-4'),

        # graph Lines
        html.Div([
            dcc.Graph(
                id='graphTwo',
                figure={
                    'data': [{
                        'x': xg2, 'y': yg2, 'type': 'line',
                        'marker': {'color': cores[3]},
                        'name': 'Vendas'
                    }],
                    'layout': {
                        'title': 'Vendas - Faturamento 2019',
                        'showlegend': True,
                        'xaxis': {'showgrid': False},
                        'yaxis': {'showgrid': True},
                        # background transparent
                        'plot_bgcolor': 'rgba(0,0,0,0)',
                        'paper_bgcolor': 'rgba(0,0,0,0)',
                        'font': {'color': 'white'}
                    }
                }
            )
        ], className='col-xs-8'),

    ], className='col-xs-12 well'),

    # row 5 - linha 5 - best sales person
    html.Div([
        # card best salesperson - melhor vendedor
        html.Div([
            html.H4('DESTAQUE 2019', className='text-center'),
            html.Br(),
            html.Img(src='https://www.fiscalti.com.br/wp-content/uploads/2020/05/default-user-image-365x365.png',
                     width='70px', height='70px'),
            html.H2(f'Vendedor: {nomeV}'),
            html.H5(pmvStr),
            html.H5(mfStr)

        ], className='col-xs-4 jumbotron'),
        html.Div([
            html.Div([
                dcc.Graph(
                    id='graphThree',
                    figure={
                        'data': [{
                            'x': xg3, 'y': yg3, 'type': 'line',
                            'marker': {'color': cores[0]},
                            'name': 'Vendas'
                        }],
                        'layout': {
                            'title': f'Vendedor {nomeV} - Faturamento 2019 ',
                            'showlegend': True,
                            'xaxis': {'showgrid': False},
                            'yaxis': {'showgrid': True},
                            # background transparent
                            'plot_bgcolor': 'rgba(0,0,0,0)',
                            'paper_bgcolor': 'rgba(0,0,0,0)',
                            'font': {'color': 'white'}
                        }
                    }
                )
            ], className='col-xs-8'),
        ])
    ], className='col-xs-12 well'),

], className='col-xs-12')


# this code will be in my github (description this video)
# thankyou!!!!

if __name__ == '__main__':
    app.run_server(debug=True)
