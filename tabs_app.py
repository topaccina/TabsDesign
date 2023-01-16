from dash import Dash, html, dcc, get_asset_url
import dash_bootstrap_components as dbc

#me = html.Img(src=get_asset_url('me.png'))
linkedinCard = dbc.Card([
    dbc.CardImg(src='assets/me.png', top=True),
    dbc.CardBody(
        [html.H1([html.A(html.I(className="bi bi-linkedin"), href='', target='__blank__'), " Laura L.", ], className="text-nowrap"),
            html.H3(" Happy Lifelong Learner",
                    className="text-primary"),
            html.Div("Wonderland Inc."),
            html.Div("EveryWhereLand Str.",
                     className="small"),
         ]
    )],
    className="my-2",
)

app = Dash(__name__, meta_tags=[
    {"name": "viewport", "content": "width=device-width"}], external_stylesheets=[dbc.icons.BOOTSTRAP])

app.layout = html.Div([
    html.Div([
        dcc.Tabs([
            dcc.Tab(label='First Tab', value='tab1', id='tab1', className='custom-tab', selected_className='custom-tab--selected',
                    children=[html.Div([linkedinCard], className='card-container-flex')]),
            dcc.Tab(label='Second Tab', value='tab2', id='tab2', className='custom-tab', selected_className='custom-tab--selected',
                    children=[]),
            dcc.Tab(label='Third Tab', value='tab3', id='tab3', className='custom-tab', selected_className='custom-tab--selected',
                    children=[]),
        ], className='custom-tabs', value='tab1')
    ], className='main-container')


])

if __name__ == '__main__':
    app.run(debug=True)
