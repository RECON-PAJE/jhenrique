# RECON.PAJE

## Requerimentos

- Python 3.12.4
- PostgreSQL 16.2

## Configurando o ambiente Backend 

Baixe o repositório com a branch desejada:

    $git clone <url> -b <branch>

### UNIX - Linux archlinux 6.9.6-arch1-1

Crie o ambiente virtual e o ative:        

    $python -m venv path/to/venv
    $source path/to/venv/bin/activate

### VSCode - 1.91.0

Instale a extensão Python do VSCode fornecida pela Microsoft:

    https://marketplace.visualstudio.com/items?itemName=ms-python.python

Selecione o interpretador Python 3.12.4 pela interface do VSCode

Crie o ambiente virtual e o ative:        

    $python -m venv path/to/venv
    $source path/to/venv/bin/activate

   
### Instalando requisitos

Instale as dependências do Python com o seguinte comando:

    $pip install -r requirements.txt


## Configuração das Variáveis do banco de dados (PostgreSQL)

Este projeto requer a configuração de algumas variáveis de ambiente para o PostgreSQL funcionar corretamente com a aplicação. Você pode configurá-las usando export ou criando um arquivo .env.

Configuração usando export:

    $export DB_NAME={nome_do_banco_de_dados}
    $export DB_USER={usuario_do_banco_de_dados}
    $export DB_PASSWORD={senha_do_banco_de_dados}
    $export DB_HOST={endereco_do_banco_de_dados}
    $export DB_PORT={porta_do_banco_de_dados}

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

    $python manage.py makemigrations
    $python manage.py migrate

Crie um superusuário para acessar o painel de administração:
    
    $python manage.py createsuperuser
    
        Email: admin@admin.com
        Nome: recon.admin
        Password: recon.admin
        Password (again): recon.admin
        Superuser created successfully.

E por fim, execute o servidor Django:

    $python manage.py runserver
        
        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).
        July 04, 2024 - 16:32:32
        Django version 5.0.4, using settings 'Reconpaje.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CONTROL-C.


