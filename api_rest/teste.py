from tinydb import TinyDB, Query 

banco_teste = TinyDB('bancoteste.json')

#criando tabelas
usuarios = banco_teste.table('usuarios')
produtos = banco_teste.table('produtos')

#JSON (e TinyDB) exige que as chaves dos dicionários sejam strings
#inserir dados no default
banco_teste.insert({'nome': 'Jaja', 'idade': 33})
banco_teste.insert({'nome': 'Ivan', 'idade': 53})
banco_teste.insert({'aaa': 'agadma', 'jovem': 'agata', '99': 'vitor'})

#inserindo dados nas tabelas específicas
usuarios.insert({'nome': 'Ana', 'idade': 24, 'profissão': 'escavadora'})
produtos.insert({'nome': 'Manga', 'validade': '22/12/2026'})

# Busca
Pessoa = Query()
resultado = banco_teste.search(Pessoa.idade == 33)
print(resultado)

#Atualizar dados
banco_teste.update({'idade': 31}, Pessoa.nome == 'Jaja')
print(banco_teste.all())

#remover dados
banco_teste.remove(Pessoa.nome == 'Jaja')
print(banco_teste.all())