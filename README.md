# Estudo Flask

## Descrição

Este é um estudo sobre desenvolvimento de site utilizando o framework `flask`

## Objetivo

Este estudo tem como finalidade o desenvolvimento de uma PWA utilizando dessa tecnologia

## Primeiros Passos

## Instalando Flask

> [Documentação Original](https://flask.palletsprojects.com/en/2.2.x/installation/)

### Criando ambiente Virtual

1. Com o vsCode aberto inicialize o terminal **cmd**
   - `Ctrl+'`
1. No terminal **cmd** execute o comando a seguir:

   ```ps
      mkdir myproject
      cd myproject
      py -3 -m venv venv
   ```

### Ativando o Ambiente Virtual

```ps
.\venv\Scripts\activate
```

### Instalando

```ps
pip install flask
```

### Instalando Requisitos

```ps
python -m pip install -r requirements.txt
```

### Criando arquivo de Requisitos

1. Com o vsCode aberto inicialize o terminal **cmd**
   - `Ctrl+'`
1. No terminal **cmd** execute o comando a seguir:

   ```ps
   python -m pip freeze > requirements.txt
   ```

### Criando arquivo app.py

## MVP - Hello Word

### Colocando o site no ar

```py
from flask import Flask

app = Flask(__name__)

@app. route("/")
def index():
   return "Hello world!"

if __name__ == "__main__":
   app. run()
```

> O terminal deve indicar o endereço no qual a pagina será exibida, geralmente: `http://127.0.0.1:5000`

### Instalando banco de dados SQL-Alchemy

```ps
pip install flask-sqlalchemy
```

## Efetuando o deploy do site

## Padrões

- Pastas

## Referencias

- [Como Criar e Publicar um Site em Python com Flask](https://www.youtube.com/watch?v=K2ejI4z8Mbg)
- [Curso de Flask](https://www.youtube.com/watch?v=Pz9rayiDHW0&list=PL3BqW_m3m6a05ALSBW02qDXmfDKIip2KX)
