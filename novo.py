from modulefinder import packagePathMap
from re import template
import site
from fastapi import FastAPI, Request
import fastapi
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="site")

@app.get('/DadosCliente', response_class=HTMLResponse)
def DadosCliente(request: Request):

    clientsData = [
        {'nome':'admin', 'apelidos':'administrador', 'data_nascimento':'26/06/2022', 'morada':'Análise Sistemas, DETI, UA, Aveiro', 'codigo_postal':'3800-000', 'contribuinte':'000000000', 'tipo_conta':'Administrador'},
        {'nome':'Alex', 'apelidos':'Sério', 'data_nascimento':'16/05/1989', 'morada':'Análise Sistemas, DETI, UA, Aveiro', 'codigo_postal':'3800-111', 'contribuinte':'111111111', 'tipo_conta':'Administrador'},
        {'nome':'Rodrigo', 'apelidos':'Martins', 'data_nascimento':'?/?/????', 'morada':'Análise Sistemas, DETI, UA, Aveiro', 'codigo_postal':'3800-222', 'contribuinte':'222222222', 'tipo_conta':'Administrador'}
    ]

    context = {'request' : request, 'clients_data': clientsData}
    return templates.TemplateResponse("DadosCliente.html", context)