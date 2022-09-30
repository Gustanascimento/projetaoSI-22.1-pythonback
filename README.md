# projetaoSI-22.1-pythonback

Aplicação para realizar armazenamento de imagens

## Instalação

> Python ^3.10

> Django
> Django RestFrameWork

    - Full REST

## Setup

1. Clone o repositório
    
    $ git clone git@github.com:Gustanascimento/projetaoSI-22.1-pythonback.git
    $ cd projetaosi-22.1-pythonback

2. Instalação Poetry

    Linux/Windows Bash
        
        $ curl -sSL https://install.python-poetry.org | python3 -

    Windows Shell

        $ (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

#### Para mais informações, consultar [Documentação Oficial Poetry](https://python-poetry.org/docs/ "Introdução")

3. Instalação de dependências

    $ poetry Shell
    $ poetry install

4. Executar projeto local

    Terminal

        $ python manage.py runserver 8000:8000

    Docker

        $ docker build .
        $ docker image ls

        $ docker run -d -p 8000:8000 --name projetao "id do resultado mais recente do comando acima"

    Após isso, acessar por meio do http://localhost:8000
