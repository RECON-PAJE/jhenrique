# RECON.PAJE

## Requerimentos

- Python 3.12.4
- PostgreSQL

## Configurando o ambiente

Ative o ambiente virtual (caso esteja utilizando):

    source path/to/venv/bin/activate  # Linux/macOS
    path\to\venv\Scripts\activate      # Windows

Instale as dependências do Python com o seguinte comando:

    pip install -r requirements.txt


## Configuração das Variáveis de Ambiente

Este projeto requer a configuração de algumas variáveis de ambiente para o PostgreSQL funcionar corretamente com a aplicação. Você pode configurá-las usando export ou criando um arquivo .env.

Configuração usando export:

    export DB_NAME={nome_do_banco_de_dados}
    export DB_USER={usuario_do_banco_de_dados}
    export DB_PASSWORD={senha_do_banco_de_dados}
    export DB_HOST={endereco_do_banco_de_dados}
    export DB_PORT={porta_do_banco_de_dados}

Configuração usando um arquivo .env:

Crie um arquivo chamado .env na raiz do seu projeto e adicione as seguintes variáveis de ambiente:

    DB_NAME={nome_do_banco_de_dados}
    DB_USER={usuario_do_banco_de_dados}
    DB_PASSWORD={senha_do_banco_de_dados}
    DB_HOST={endereco_do_banco_de_dados}
    DB_PORT={porta_do_banco_de_dados}

Substitua os valores entre chaves pelos valores correspondentes do seu ambiente.

## Uso

Se estiver rodando a primeira vez, faça as migrações dos modelos:

    python manage.py makemigrations
    python manage.py migrate

E por fim, execute o servidor Django:

    python manage.py runserver
