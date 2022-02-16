# Clinica-KabaDor
Aplicação Web para uma Clínica Médica desenvolvida com Django. Trabalho 2 – Laboratório de Engenharia de Software I

## Integrantes do Grupo 

- DANILO GONÇALVES CUSTÓDIO
    - matrícula: 20193016039
- EDUARDO MARTINS GOMES PEREIRA
    - matrícula: 20193001546
- FELIPE MARTINS LEMOS DE MORAIS
    - matrícula: 20193001045
- MARCUS VINICIUS DURÃES ZUBA FERNANDES
    - matrícula: 20193001822

## Configuração do projeto

Após clonar o repositório, execute os seguintes passos na raiz do projeto:

- Crie um ambiente virtual para o projeto
    - `mkdir env`
    - `pip install virtualenv`
    - `virtualenv env/clinicakabador`

- Ative o ambiente virtual (faça isso sempre antes de executar o projeto)
    - `source env/clinicakabador/bin/activate`
    - Obs: caso queira desativar o ambiente virtual, basta executar `deactivate`

- Instale os pacotes necessários no ambiente virtual 
    - `pip install -r requirements.txt`

- Execute as migrations para que o seu banco de dados local seja criado (faça isso sempre para manter o seu banco atualizado)
    - `python manage.py migrate`

- Crie um usuário de administrador para acessar a parte privada da aplicação e o painel de admin do Django:
    - `python manage.py createsuperuser`

- Execute o server
    - `python manage.py runserver`

- O projeto será hosteado e poderá ser acessado em [localhost:8000](http://localhost:8000)

- Para acessar o painel de admin do Django, basta acessar [localhost:8000/admin](http://localhost:8000) 