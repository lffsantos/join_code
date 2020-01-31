
Código Simples para busca de funcionario e cargo

  
  

1. clone o respositório.

2. crie um virtualenvo com Python 3.6.

3. Ative o virtualenv.

4. Instale as dependências.

5. Configure a instância .env

  

```console

git clone https://github.com/lffsantos/join_code.git join_code

cd join_code

virtualenv --python=python3.6 .venv

source .venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py loaddata core.json

python manage.py runserver

```

## Simple Demo
[http://localhost:8000/](http://localhost:8000/)
  

## API 

"pessoas": "http://localhost:8000/api/pessoas/",
	- Filtra por "Nome, admissão, cargo"  
	- Ordenação por: (Id, Nome, cargo, admissão)

"cargos": "http://localhost:8000/api/cargos/"
     - Filtra por "Nome"  
	- Ordenação por: (Id, cargo)

"total por cargo": [http://localhost:8000/total-por-cargo/](http://localhost:8000/total-por-cargo/)

"usuário mais antigo": [http://localhost:8000/mais-antigo/](http://localhost:8000/mais-antigo/)