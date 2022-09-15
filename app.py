from flask import Flask
from flask import render_template,request,redirect,url_for
from graph import GraphModel

cidades = {'Porto Velho':[
                ('Rio Branco',544),
                ('Manaus',901),
                ('Boa Vista',1686),
                ('Cuiabá',1456),
            ],
            'Rio Branco':[('Porto Velho',544)],
            'Boa Vista':[('Porto Velho',1686)],
            'Manaus':[
                ('Palmas',1509),
                ('Porto Velho',901)
            ],
            'Macapá':[
                ('Belém',1000),
            ],
            'Belém':[
                ('Macapá',1000),
                ('São Luís',1610),
                ('Palmas',1610)
            ],
            'São Luís':[
                ('Belém',1610),
                ('Teresina',446),
                ('Palmas',964),
            ],
            'Palmas':[
                ('Belém',973),
                ('Teresina',1401),
                ('São Luís',964),
                ('Cuiabá',1029),
                ('Brasília',620),
            ],
            'Cuiabá':[
                ('Porto Velho',1456),
                ('Palmas',620),
                ('Goiânia',934),
                ('Campo Grande',934),
            ],
            'Goiânia':[
                ('Cuiabá',934),
                ('Campo Grande',935),
                ('Brasília',209),
                ('Belo Horizonte',906),
            ],
            'Brasília':[
                ('Goiânia',209),
                ('Palmas',973),
                ('Salvador',1443),
                ('Fortaleza',2200),
            ],
            'Fortaleza':[
                ('Teresina',634),
                ('Brasília',2200),
                ('Salvador',1389),
                ('Aracajú',815),
                ('Maceió',1075),
                ('Recife',800),
                ('João Pessoa',688),
                ('Natal',537)
            ],
            'Campo Grande':[
                ('Cuiabá',694),
                ('Goiânia',935),
                ('Belo Horizonte',935),
                ('Curitiba',991)
            ],
            'Natal':[
                ('João Pessoa',151),
                ('Fortaleza',537)
            ],
            'João Pessoa':[
                ('Natal',151),
                ('Recife',120),
                ('Fortaleza',688)
            ],
            'Recife':[
                ('João Pessoa',120),
                ('Maceió',202),
                ('Fortaleza',800)
            ],
            'Maceió':[
                ('Recife',202),
                ('Aracajú',201),
                ('Fortaleza',1075),
            ],
            'Aracajú':[
                ('Salvador',356),
                ('Maceió',201),
                ('Fortaleza',815),
            ],
            'Salvador':[
                ('Brasília',1060),
                ('Aracajú',356),
                ('Fortaleza',1389),
            ],
            'Belo Horizonte':[
                ('Vitória',524),
                ('Goiânia',906),
                ('Campo Grande',906),
                ('Rio de Janeiro',906),
                ('São Paulo',586)
            ],
            'Vitória':[
                ('Belo Horizonte',524),
                ('Rio de Janeiro',741)
            ],
            'Rio de Janeiro':[
                ('Vitória',741),
                ('Belo Horizonte',906),
                ('São Paulo',429)
            ],
            'São Paulo':[
                ('Rio de Janeiro',429),
                ('Belo Horizonte',586),
                ('Curitiba',338),
            ],
            'Curitiba':[
                ('Florianópolis',300),
                ('Campo Grande',780),
                ('São Paulo',338),
                ('Porto Alegre',546),
            ],
            'Florianópolis':[
                ('Curitiba',300),
                ('Porto Alegre',376),
            ],
            'Porto Alegre':[
                ('Florianópolis',376),
                ('Curitiba',546),
            ]  
        }

capitais_lista = [
    'Manaus',
    'Rio Branco',
    'Campo Grande',
    'Macapá',
    'Brasília',
    'Boa Vista',
    'Cuiabá',
    'Palmas',
    'São Paulo',
    'Teresina',
    'Rio de Janeiro',
    'Belém',
    'Goiânia',
    'Salvador',
    'Florianópolis',
    'São Luís',
    'Maceió',
    'Porto Alegre',
    'Curitiba',
    'Belo Horizonte',
    'Fortaleza',
    'Recife',
    'João Pessoa',
    'Aracajú'
]

capitais_lista = sorted(capitais_lista)


app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("homepage.html")

def shortest_path(graph,start,end):
    bala = graph.find_shortest_path(start,end)
    return bala   

@app.route('/menor_distancia',methods = ['POST'])
def menor_distancia():
    origem = request.form.get("origem")
    destino = request.form.get("destino")

    graph = GraphModel(cidades)

    shortest = shortest_path(graph,origem,destino)

    print(shortest)


    print(origem)

    return "sou fashion"
