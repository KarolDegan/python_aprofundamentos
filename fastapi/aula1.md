 O pip é usado para instalar bibliotecas Python que você usa dentro de um programa Python.
 O pipx é usado para instalar ferramentas feitas em Python que você usa no terminal, como programas de linha de comando.
  Poetry é um gerenciador de projetos para Python.
       poetry new nome_pacote: já estrutura um pacote com confs iniciais
       poetry install vai instalar todas as dependências do projeto listadas no arquivo pyproject.toml.

 python -i <seu_arquivo.py> vai abrir um terminal iterativo com o documento
 poetry add 'fastapi[standard]' 
   Adiciona o pacote fastapi como dependência do seu projeto. Esse comando atualiza seu pyproject.toml
   Ao instalar com [standard], você está pedindo para que o Poetry instale o fastapi e também alguns pacotes que são úteis junto com ele, como:
       uvicorn[standard];python-multipart;jinja2;httpx;email-validator

*petry shell:* abrir um shell (terminal) dentro do ambiente virtual criado pelo Poetry para o seu projeto Python.

*erramentas de desenvolvimento:*
    taskipy: ferramenta usada para criação de comandos. Como executar a aplicação, rodar os testes, etc.
    pytest: ferramenta para escrever e executar testes
    ruff: Uma ferramenta que tem duas funções no nosso código:
        a. Um analisador estático de código (um linter), para dizer se não estamos infringido alguma boa prática de programação;
        b. Um formatador de código. Para seguirmos um estilo único de código. Vamos nos basear na PEP-8.
    poetry add --group dev pytest pytest-cov taskipy ruff