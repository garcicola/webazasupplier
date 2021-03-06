import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import  dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pathlib
import dash_bootstrap_components as dbc
import dash_table
import xlrd
import openpyxl

# CREAR DASH

app= dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO])


app.layout = html.Div([
    # represents the URL bar, doesn't render anything
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

index_page = html.Div([
    html.Br(),
    html.Br(),
    dcc.Link('Productos', href='/page-1',style={'text-align': 'left', 'color': 'black', 'fontSize': 25}),
    html.Br(),
    dcc.Link('Prueba de Concepto', href='/page-2',style={'text-align': 'left', 'color': 'black', 'fontSize': 25}),

    html.Br(),

    dbc.Card([
            dbc.Col([
                dbc.Card([
                    dbc.CardImg(src=app.get_asset_url('Azurian Analytica.png'),
                            top=False,
                            className = 'align-self-center',
                            style={'height':'30%', 'width':'30%'})
                    ])
                ]),
            dbc.Col([
                html.H3("Portafolio de productos", style={'text-align': 'center', 'color': 'darkblue', 'fontSize': 100})
                ])
        ]),

    html.Br(),

        dbc.Row([
            dbc.Col([
                dbc.CardImg(
                    src=app.get_asset_url('truck.png'),
                    top=False,
                    style={'height':'80%', 'width':'80%'})
                ]),
            dbc.Col([
                html.Br(),
                html.H5("&", style={'text-align': 'left', 'color': 'darkblue', 'fontSize': 50}),
                html.H5("Prueba de concepto", style={'text-align': 'left', 'color': 'darkblue', 'fontSize': 50}),
                html.H5("Comercializadores", style={'text-align': 'left', 'color': 'darkblue', 'fontSize': 50})
                ])
        ]),

    html.Br()

],style={'background-color':'white'})

page_1_layout = html.Div([
    dcc.Link('Prueba de Concepto', href='/page-2',style={'text-align': 'left', 'color': 'black', 'fontSize': 25}),
    html.Br(),
    dcc.Link('Inicio', href='/',style={'text-align': 'left', 'color': 'black', 'fontSize': 25}),

#T??tulo de la p??gina
    html.Br(),
    html.H1('Productos',style={'text-align': 'center', 'color': 'black', 'fontSize': 80}),
    html.Br(),
    html.Br(),
    #Analisis de clientes
    html.Br(),
    html.H3("An??lisis de Clientes", style={'text-align': 'center', 'color': 'darkblue', 'fontSize': 60,'background-color':'ivory'}),
    html.Br(),
    html.Br(),
    html.H3("La anal??tica de datos permite conocer el comportamiento en detalle de los clientes, clasificarlos por sus caracter??sticas m??s relevantes y conocer como influenciar su comportamiento futuro", style={'text-align': 'center', 'color': 'darkblue', 'fontSize': 30}),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Br(),
                dbc.CardImg(src=app.get_asset_url('SEG.gif'),
                            top=True,
                            className = 'align-self-center',
                            style={'height':'15%', 'width':'15%'}),
                html.H3("Segmentaci??n",style={'color': 'darklBlue', 'textAlign': 'center', 'fontSize': 40}),
                html.Br(),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H1("??Qu?? es?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "La segmentaci??n de los clientes se puede hacer teniendo en cuenta m??ltiples variables simult??neamente,lo que permite obtener segmentos m??s asociados a patrones de compra y no solo caracter??sticas geogr??ficas, socioecon??micas o de marca."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("??Qu?? produce el an??lisis?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Grupos de clientes o puntos de venta de caracter??sticas similares que pueden ser sujetos de estrategias distintas, m??s individualizadas."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ]),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            html.H1("??Qui??n se beneficia?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Mercadeo: Permite conocer al cliente por sus patrones de compra, generando una clasificaci??n m??s real y ??til."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20}),
                            html.Br(),
                            html.H3( "Ventas: Un cliente mejor identificado permite optimizar su potencial de compras."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("??Insumo para que?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Estrategias de fidelizaci??n, promociones de productos especificos por tipo de cliente, identificaci??n de tendencias por segmentos, entre otros ."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ])
                    ]),
                    dbc.Row([]),
                    ])
            ])
        ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Br(),
                dbc.CardImg(src=app.get_asset_url('RFM.gif'),
                            top=True,
                            className = 'align-self-center',
                            style={'height':'15%', 'width':'15%'}),
                html.H3("An??lisis RFM",style={'color': 'darklBlue', 'textAlign': 'center', 'fontSize': 40}),
                html.Br(),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H1("??Qu?? es?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "R=Recency (Reciente), F=Frecuency(Frecuencia),M=Monetary (Monetario). Este m??todo de segmentaci??n clasifica los clientes bajo los tres criterios."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("??Qu?? produce el an??lisis?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Segmenta el portafolio de clientes identificando su lealtad y valor para la organizaci??n."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ]),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            html.H1("??Qui??n se beneficia?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Mercadeo: Permite conocer al cliente por sus patrones de compra y su aporte econ??mico a la organizaci??n."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20}),
                            html.Br(),
                            html.H3( "Ventas: Permite calificar economicante al cliente."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("??Insumo para que?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Estrategias de fidelizaci??n, promociones de productos especificos por tipo de cliente, identificaci??n de tendencias por segmentos, entre otros ."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ])
                    ]),
                    dbc.Row([]),
                    ])
            ])
        ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Br(),
                dbc.CardImg(src=app.get_asset_url('CLV.gif'),
                            top=True,
                            className = 'align-self-center',
                            style={'height':'15%', 'width':'15%'}),
                html.H3("Customer lifetime value",style={'color': 'darklBlue', 'textAlign': 'center', 'fontSize': 40}),
                html.Br(),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H1("??Qu?? es?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Este m??todo de estima el valor promedio del costo de un cliente, siendo ??til para determinar el costo m??ximo que se debe invertir via mercadeo, promociones, publicidad, etc."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("??Qu?? produce el an??lisis?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Determina de manera precisa la relaci??n costo beneficio de un cliente con la organizaci??n."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ]),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            html.H1("??Qui??n se beneficia?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Mercadeo: Permite entender el cliente en una relaci??n de corto y largo plazo."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20}),
                            html.Br(),
                            html.H3( "Financiero: Permite cuantificar el valor econ??mico de un cliente para la organizaci??n."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("??Insumo para que?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Campa??as de promociones, estrategias de fidelizaci??n, entre otras, cuantificables y rentables ."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ])
                    ]),
                    dbc.Row([]),
                    ])
            ])
        ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Br(),
                dbc.CardImg(src=app.get_asset_url('Churn.gif'),
                            top=True,
                            className = 'align-self-center',
                            style={'height':'15%', 'width':'15%'}),
                html.H3("Churn an??lisis",style={'color': 'darklBlue', 'textAlign': 'center', 'fontSize': 40}),
                html.Br(),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H1("??Qu?? es?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Este m??todo determina la tasa de p??rdida probable de los clientes y sus variables relevantes."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("??Qu?? produce el an??lisis?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Determina la probabilidad de p??rdida de un cliente ."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ]),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            html.H1("??Qui??n se beneficia?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Mercadeo: Permite entender las variables que llevan a la p??rdida de un cliente."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20}),
                            html.Br(),
                            html.H3( "Ventas: Permite anticipar el impacto en ventas, de la posible p??rdida de demanda."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("??Insumo para que?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Campa??as de retenci??n y estrategias de fidelizaci??n, entre otras."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ])
                    ]),
                    dbc.Row([]),
                    ])
            ])
        ]),
    #Analisis de productos
    html.Br(),
    html.H3("An??lisis de Productos", style={'text-align': 'center', 'color': 'darkred', 'fontSize': 60,'background-color':'ivory'}),
    html.Br(),
    html.H3("A trav??s de la anal??tica de datos se pueden identificar las din??micas de comportamiento de los productos y sus relaciones.", style={'text-align': 'center', 'color': 'darkred', 'fontSize': 20}),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Br(),
                dbc.CardImg(src=app.get_asset_url('Canastas.gif'),
                            top=True,
                            className = 'align-self-center',
                            style={'height':'15%', 'width':'15%'}),
                html.H3("Canastas",style={'color': 'darklBlue', 'textAlign': 'center', 'fontSize': 40}),
                html.Br(),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H1("??Qu?? es?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Este m??todo identifica las relaciones entre los productos que compran los clientes."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("??Qu?? produce el an??lisis?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Muestra las combinaciones de productos que se complementan entre si y cuales son los perfiles de clientes de cada grupo."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ]),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            html.H1("??Qui??n se beneficia?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Mercadeo: Clasifica los grupos de clientes y sus productos asociados, entendiendo cuales tienen mayor potencial para ser adquiridos por los distintos tipos de clientes."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20}),
                            html.Br(),
                            html.H3( "Ventas: Identifica productos complementarios, sustitutos, productos que motivan la compra de otros."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("??Insumo para que?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Distribuci??n de productos en g??ndolas, promociones 2x1, ofertas de productos, etc."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ])
                    ]),
                    dbc.Row([]),
                    ])
            ])
        ]),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Br(),
                dbc.CardImg(src=app.get_asset_url('Caracteristicas.gif'),
                            top=True,
                            className = 'align-self-center',
                            style={'height':'15%', 'width':'15%'}),
                html.H3("An??lisis de caracter??sticas",style={'color': 'darklBlue', 'textAlign': 'center', 'fontSize': 40}),
                html.Br(),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H1("??Qu?? es?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Identifica las caracter??sticas que motivan las ventas de los productos, en funci??n de los segmentos de clientes."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("??Qu?? produce el an??lisis?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Permite identificar las caracter??sticas que generan relaci??n con los compradores."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ]),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            html.H1("??Qui??n se beneficia?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Mercadeo: Permite gestionar los atributos de los productos para generar una relaci??n mas profunda con los distintos segmentos."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20}),
                            html.Br(),
                            html.H3( "Ventas: Permite ampliar atributos iguales o similares de otros productos o marcas."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("??Insumo para que?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Ofertas de productos, promociones, estrategias de fidelizaci??n, ventas cruzadas etc."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ])
                    ]),
                    dbc.Row([]),
                    ])
            ])
        ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Br(),
                dbc.CardImg(src=app.get_asset_url('Proyeccion.gif'),
                            top=True,
                            className = 'align-self-center',
                            style={'height':'15%', 'width':'15%'}),
                html.H3("Proyecci??n de demanda",style={'color': 'darklBlue', 'textAlign': 'center', 'fontSize': 40}),
                html.Br(),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H1("??Qu?? es?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Estima la demanda futura de los productos."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("??Qu?? produce el an??lisis?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Proyecci??n de las cantidades por demandar en los siguientes periodos."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ]),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            html.H1("??Qui??n se beneficia?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Compras: Permite gestionar inventarios de una manera m??s precisa y eficiente."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20}),
                            html.Br(),
                            html.H3( "Ventas: Entender la din??mica futura de la demanda y poder influenciarla a trav??s de estrategias."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("??Insumo para que?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Proyecci??n financiera de PyG, Ofertas de productos, promociones,etc."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ])
                    ]),
                    dbc.Row([]),
                    ])
            ])
        ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Br(),
                dbc.CardImg(src=app.get_asset_url('Elasticidad.gif'),
                            top=True,
                            className = 'align-self-center',
                            style={'height':'15%', 'width':'15%'}),
                html.H3("Elasticidad de precio",style={'color': 'darklBlue', 'textAlign': 'center', 'fontSize': 40}),
                html.Br(),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H1("??Qu?? es?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Determima la sensibilidad de la intenci??n de la demanda derivada de cambios del precio del producto."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("??Qu?? produce el an??lisis?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "La curva de demanda de los productos ."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ]),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            html.H1("??Qui??n se beneficia?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Mercadeo: Conoce la sensibilidad de la demanda de los productos de cada uno de los segmentos de clientes  ."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20}),
                            html.Br(),
                            html.H3( "Ventas: Establecer la naturaleza de la demanda dada los cambios del precio."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("??Insumo para que?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Optimizaci??n de precios, Ofertas de productos, promociones,etc."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ])
                    ]),
                    dbc.Row([]),
                    ])
            ])
        ]),

#Analisis de proveedores
    html.Br(),
    html.H3("An??lisis de Proveedores", style={'text-align': 'center', 'color': 'purple', 'fontSize': 60,'background-color':'ivory'}),
    html.Br(),
    html.H3("A trav??s de la anal??tica de datos se puede analizar el comportamiento de los proveedores, en t??rminos de demanda de productos, rentabilidad, calidad, tiempos de entrega,etc; para la toma de decisiones ??ptimas.", style={'text-align': 'center', 'color': 'purple', 'fontSize': 20}),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Br(),
                dbc.CardImg(src=app.get_asset_url('Inventarios.gif'),
                            top=True,
                            className = 'align-self-center',
                            style={'height':'15%', 'width':'15%'}),
                html.H3("Manejo de inventarios",style={'color': 'darklBlue', 'textAlign': 'center', 'fontSize': 40}),
                html.Br(),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H1("??Qu?? es?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Un sistema de administraci??n de inventarios donde se optimizan y rentabilizan los proveedores ."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("??Qu?? produce el an??lisis?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Un sistema, que basado en las caracter??sticas de los proveedores y sus productos optimiza su manejo de tiempos, demandas y rentabilidades."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ]),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            html.H1("??Qui??n se beneficia?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Compras: Desarrolla un sistema de administraci??n de su gesti??n."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20}),
                            html.Br(),
                            html.H3( "Ventas: Al optimizar los inventarios permite la posibilidad incluir mayor variedad de productos adicionales."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("??Insumo para que?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Gesti??n integral de inventarios."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ])
                    ]),
                    dbc.Row([]),
                    ])
            ])
        ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Br(),
                dbc.CardImg(src=app.get_asset_url('Transporte.gif'),
                            top=True,
                            className = 'align-self-center',
                            style={'height':'15%', 'width':'15%'}),
                html.H3("Log??stica de transporte",style={'color': 'darklBlue', 'textAlign': 'center', 'fontSize': 40}),
                html.Br(),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H1("??Qu?? es?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Un sistema de administraci??n de tiempos y movimientos para optimizar las rutas, productos y entregas  ."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("??Qu?? produce el an??lisis?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Un sistema de optimizaci??n de tiempos y moviemintos log??sticos."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ]),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            html.H1("??Qui??n se beneficia?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Compras: Optimizaci??n y ahorros del proceso log??stico y de transporte."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20}),
                            html.Br(),
                            html.H3( "Financiero: Reducci??n de costos y aumento de la rentabilidad."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("??Insumo para que?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Gesti??n integral de recursos log??sticos."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ])
                    ]),
                    dbc.Row([]),
                    ])
            ])
        ]),

#KPIs
    html.Br(),
    html.H3("KPI's", style={'text-align': 'center', 'color': 'saddlebrown', 'fontSize': 60,'background-color':'ivory'}),
    html.Br(),
    html.H3("Los productos pueden influenciar m??ltiples KPI's simulateneamente .", style={'text-align': 'center', 'color': 'saddlebrown', 'fontSize': 40}),
    html.Br(),
    dbc.Row([
        dbc.Col([],width=1),
        dbc.Col([
            dbc.CardImg(src=app.get_asset_url('Diapositiva1.JPG'),
                    top=True,
                    className='align-self-center',
                    style={'height': '100%', 'width': '100%'}),
            ],width=10),
        dbc.Col([],width=1)
    ]),
    dbc.Row([
        dbc.Col([],width=1),
        dbc.Col([
            dbc.CardImg(src=app.get_asset_url('Diapositiva2.JPG'),
                    top=True,
                    className='align-self-center',
                    style={'height': '100%', 'width': '100%'}),
            ],width=10),
        dbc.Col([],width=1)
    ]),



    dcc.Link('Prueba de Concepto', href='/page-2',style={'text-align': 'left', 'color': 'black', 'fontSize': 25}),
    html.Br(),
    dcc.Link('Inicio', href='/',style={'text-align': 'left', 'color': 'black', 'fontSize': 25}),



    ],style={'background-color':'white'})


@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    #elif pathname == '/page-2':
    #   return page_2_layout
    else:
        return index_page
    # You could also return a 404 "URL not found" page here


if __name__ == '__main__':
    app.run_server(debug=True)