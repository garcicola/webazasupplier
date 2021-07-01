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

#Título de la página
    html.Br(),
    html.H1('Productos',style={'text-align': 'center', 'color': 'black', 'fontSize': 80}),
    html.Br(),
    html.Br(),
    #Analisis de clientes
    html.Br(),
    html.H3("Análisis de Clientes", style={'text-align': 'center', 'color': 'darkblue', 'fontSize': 60,'background-color':'ivory'}),
    html.Br(),
    html.Br(),
    html.H3("La analítica de datos permite conocer el comportamiento en detalle de los clientes, clasificarlos por sus características más relevantes y conocer como influenciar su comportamiento futuro", style={'text-align': 'center', 'color': 'darkblue', 'fontSize': 30}),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Br(),
                dbc.CardImg(src=app.get_asset_url('SEG.gif'),
                            top=True,
                            className = 'align-self-center',
                            style={'height':'15%', 'width':'15%'}),
                html.H3("Segmentación",style={'color': 'darklBlue', 'textAlign': 'center', 'fontSize': 40}),
                html.Br(),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H1("¿Qué es?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "La segmentación de los clientes se puede hacer teniendo en cuenta múltiples variables simultáneamente,lo que permite obtener segmentos más asociados a patrones de compra y no solo características geográficas, socioeconómicas o de marca."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("¿Qué produce el análisis?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Grupos de clientes o puntos de venta de características similares que pueden ser sujetos de estrategias distintas, más individualizadas."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ]),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            html.H1("¿Quién se beneficia?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Mercadeo: Permite conocer al cliente por sus patrones de compra, generando una clasificación más real y útil."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20}),
                            html.Br(),
                            html.H3( "Ventas: Un cliente mejor identificado permite optimizar su potencial de compras."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("¿Insumo para que?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Estrategias de fidelización, promociones de productos especificos por tipo de cliente, identificación de tendencias por segmentos, entre otros ."
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
                html.H3("Análisis RFM",style={'color': 'darklBlue', 'textAlign': 'center', 'fontSize': 40}),
                html.Br(),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H1("¿Qué es?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "R=Recency (Reciente), F=Frecuency(Frecuencia),M=Monetary (Monetario). Este método de segmentación clasifica los clientes bajo los tres criterios."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("¿Qué produce el análisis?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Segmenta el portafolio de clientes identificando su lealtad y valor para la organización."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ]),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            html.H1("¿Quién se beneficia?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Mercadeo: Permite conocer al cliente por sus patrones de compra y su aporte económico a la organización."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20}),
                            html.Br(),
                            html.H3( "Ventas: Permite calificar economicante al cliente."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("¿Insumo para que?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Estrategias de fidelización, promociones de productos especificos por tipo de cliente, identificación de tendencias por segmentos, entre otros ."
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
                            html.H1("¿Qué es?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Este método de estima el valor promedio del costo de un cliente, siendo útil para determinar el costo máximo que se debe invertir via mercadeo, promociones, publicidad, etc."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("¿Qué produce el análisis?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Determina de manera precisa la relación costo beneficio de un cliente con la organización."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ]),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            html.H1("¿Quién se beneficia?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Mercadeo: Permite entender el cliente en una relación de corto y largo plazo."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20}),
                            html.Br(),
                            html.H3( "Financiero: Permite cuantificar el valor económico de un cliente para la organización."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("¿Insumo para que?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Campañas de promociones, estrategias de fidelización, entre otras, cuantificables y rentables ."
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
                html.H3("Churn análisis",style={'color': 'darklBlue', 'textAlign': 'center', 'fontSize': 40}),
                html.Br(),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H1("¿Qué es?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Este método determina la tasa de pérdida probable de los clientes y sus variables relevantes."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("¿Qué produce el análisis?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Determina la probabilidad de pérdida de un cliente ."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ]),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            html.H1("¿Quién se beneficia?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Mercadeo: Permite entender las variables que llevan a la pérdida de un cliente."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20}),
                            html.Br(),
                            html.H3( "Ventas: Permite anticipar el impacto en ventas, de la posible pérdida de demanda."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("¿Insumo para que?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Campañas de retención y estrategias de fidelización, entre otras."
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
    html.H3("Análisis de Productos", style={'text-align': 'center', 'color': 'darkred', 'fontSize': 60,'background-color':'ivory'}),
    html.Br(),
    html.H3("A través de la analítica de datos se pueden identificar las dinámicas de comportamiento de los productos y sus relaciones.", style={'text-align': 'center', 'color': 'darkred', 'fontSize': 20}),
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
                            html.H1("¿Qué es?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Este método identifica las relaciones entre los productos que compran los clientes."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("¿Qué produce el análisis?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Muestra las combinaciones de productos que se complementan entre si y cuales son los perfiles de clientes de cada grupo."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ]),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            html.H1("¿Quién se beneficia?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Mercadeo: Clasifica los grupos de clientes y sus productos asociados, entendiendo cuales tienen mayor potencial para ser adquiridos por los distintos tipos de clientes."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20}),
                            html.Br(),
                            html.H3( "Ventas: Identifica productos complementarios, sustitutos, productos que motivan la compra de otros."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("¿Insumo para que?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Distribución de productos en góndolas, promociones 2x1, ofertas de productos, etc."
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
                html.H3("Análisis de características",style={'color': 'darklBlue', 'textAlign': 'center', 'fontSize': 40}),
                html.Br(),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H1("¿Qué es?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Identifica las características que motivan las ventas de los productos, en función de los segmentos de clientes."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("¿Qué produce el análisis?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Permite identificar las características que generan relación con los compradores."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ]),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            html.H1("¿Quién se beneficia?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Mercadeo: Permite gestionar los atributos de los productos para generar una relación mas profunda con los distintos segmentos."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20}),
                            html.Br(),
                            html.H3( "Ventas: Permite ampliar atributos iguales o similares de otros productos o marcas."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("¿Insumo para que?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Ofertas de productos, promociones, estrategias de fidelización, ventas cruzadas etc."
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
                html.H3("Proyección de demanda",style={'color': 'darklBlue', 'textAlign': 'center', 'fontSize': 40}),
                html.Br(),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H1("¿Qué es?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Estima la demanda futura de los productos."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("¿Qué produce el análisis?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Proyección de las cantidades por demandar en los siguientes periodos."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ]),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            html.H1("¿Quién se beneficia?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Compras: Permite gestionar inventarios de una manera más precisa y eficiente."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20}),
                            html.Br(),
                            html.H3( "Ventas: Entender la dinámica futura de la demanda y poder influenciarla a través de estrategias."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("¿Insumo para que?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Proyección financiera de PyG, Ofertas de productos, promociones,etc."
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
                            html.H1("¿Qué es?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Determima la sensibilidad de la intención de la demanda derivada de cambios del precio del producto."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("¿Qué produce el análisis?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "La curva de demanda de los productos ."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ]),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            html.H1("¿Quién se beneficia?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Mercadeo: Conoce la sensibilidad de la demanda de los productos de cada uno de los segmentos de clientes  ."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20}),
                            html.Br(),
                            html.H3( "Ventas: Establecer la naturaleza de la demanda dada los cambios del precio."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("¿Insumo para que?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Optimización de precios, Ofertas de productos, promociones,etc."
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
    html.H3("Análisis de Proveedores", style={'text-align': 'center', 'color': 'purple', 'fontSize': 60,'background-color':'ivory'}),
    html.Br(),
    html.H3("A través de la analítica de datos se puede analizar el comportamiento de los proveedores, en términos de demanda de productos, rentabilidad, calidad, tiempos de entrega,etc; para la toma de decisiones óptimas.", style={'text-align': 'center', 'color': 'purple', 'fontSize': 20}),
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
                            html.H1("¿Qué es?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Un sistema de administración de inventarios donde se optimizan y rentabilizan los proveedores ."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("¿Qué produce el análisis?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Un sistema, que basado en las características de los proveedores y sus productos optimiza su manejo de tiempos, demandas y rentabilidades."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ]),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            html.H1("¿Quién se beneficia?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Compras: Desarrolla un sistema de administración de su gestión."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20}),
                            html.Br(),
                            html.H3( "Ventas: Al optimizar los inventarios permite la posibilidad incluir mayor variedad de productos adicionales."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("¿Insumo para que?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Gestión integral de inventarios."
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
                html.H3("Logística de transporte",style={'color': 'darklBlue', 'textAlign': 'center', 'fontSize': 40}),
                html.Br(),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H1("¿Qué es?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Un sistema de administración de tiempos y movimientos para optimizar las rutas, productos y entregas  ."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("¿Qué produce el análisis?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Un sistema de optimización de tiempos y moviemintos logísticos."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ])
                        ]),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            html.H1("¿Quién se beneficia?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Compras: Optimización y ahorros del proceso logístico y de transporte."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20}),
                            html.Br(),
                            html.H3( "Financiero: Reducción de costos y aumento de la rentabilidad."
                            , style={'text-align': 'center', 'color': 'black','fontSize':20})
                        ]),
                        dbc.Col([
                            html.H1("¿Insumo para que?", style={'color': 'RoyalBlue', 'textAlign': 'center','color': 'black','fontSize':30}),
                            html.Br(),
                            html.H3( "Gestión integral de recursos logísticos."
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
    html.H3("Los productos pueden influenciar múltiples KPI's simulateneamente .", style={'text-align': 'center', 'color': 'saddlebrown', 'fontSize': 40}),
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