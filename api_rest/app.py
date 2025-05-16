# https://www.youtube.com/watch?v=1_nQ5A2HcgU
from itertools import count
from typing import Optional

from flask import Flask, request, jsonify # jsonify transformar em jason
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request # são classes auxiliares da biblioteca flask-pydantic-spec, usadas para declarar o formato esperado da requisição e da resposta, com validação automática e geração de documentação (Swagger).

from pydantic import BaseModel, Field # Pydantic é uma biblioteca Python que valida dados com base em tipos e regras definidas.
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage


app = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='Live de Python')
spec.register(app)

banco = TinyDB(storage=MemoryStorage)

c = count()

class QueryPessoa(BaseModel):
    id: Optional[int]
    nome: Optional[str]
    idade: Optional[int]

class Pessoa(BaseModel):
    id: Optional[int] = Field(default_factory=lambda: next(c))
    nome: str
    idade: int

class Pessoas(BaseModel):
    pessoas: list[Pessoa]
    count: int

#GET
@app.get('/pessoas')
@spec.validate(
    query=QueryPessoa,
    resp=Response(HTTP_200=Pessoas)
)
def buscar_todas_pessoas():
    """Retorna todas as Pessoas da base de dados."""
    query = request.context.query.dict(exclude_none=True)
    todas_as_pessoas = banco.search(
        Query().fragment(query)
    )
    return jsonify(
        Pessoas(
            pessoas=todas_as_pessoas,
            count=len(todas_as_pessoas)
        ).dict()
    )

@app.get('/pessoas/<int:id>') #rota / endpoint / recurso/ URI
@spec.validate(resp=Response(HTTP_200=Pessoas))                  #Response: API vai retornar(como saída) um JSON no formato Pessoa
def buscar_pessoa(id): #buscar                                  #Request:  API espera receber(como entrada) um JSON no formato Pessoa 
    """Retorna todas as pessoas de uma base de dados"""
    try:
        cursor = Query()
        pessoa = banco.search(cursor.id == id)[0]
    except IndexError:
        return {'message': 'Pessoa not found!'}, 404
    return jsonify(Pessoa(**pessoa).dict())


#POST
@app.post('/pessoas')
@spec.validate(body=Request(Pessoa), resp=Response(HTTP_201=Pessoa))
def inseir_pessoa():
    """Insere uma pessoa no banco de dados!"""
    body = request.context.body.dict()
    banco.insert(body)
    return body

#PUT
@app.put('/pessoas/<int:id>')
@spec.validate(body=Request(Pessoa), resp=Response('HTTP_204'))
def altera_pessoa(id):
    """Altera uma pessoa no banco de dados"""
    cursor = Query()
    body = request.context.body.dict()
    # alterar o banco, buscando pelo id do parametro (mandado)
    banco.update(body,cursor.id == id)
    return jsonify(body)

#DELETE
@app.delete('/pessoas/<int:id>')
@spec.validate( resp=Response('HTTP_204'))
def deleta_pessoa(id):
    """Deleta uma pessoa no banco de dados"""
    cursor = Query()
    # alterar o banco, buscando pelo id do parametro (mandado)
    banco.remove(cursor.id == id)
    return jsonify({})