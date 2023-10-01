<h1 align="center">
    <img alt="Django + Fly.io" title="Django + Fly.io" src=".github/icon.png" width="75px" />
</h1>

<h2 align="center">
  	Django + Fly.io
</h2>

<p align="center">
	<a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
	<a href="#-descrição">Descrição</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
	<a href="#passo-a-passo">Passo a passo</a>
</p>

## 🤖 Tecnologias

Esse projeto está sendo desenvolvido com as seguintes tecnologias:

- [Docker](https://andrearruda-blog.vercel.app/install-docker-on-linux)
- [Django](https://www.djangoproject.com/)
- [Django-Rest-Framework](https://www.django-rest-framework.org/)
- [Fly.io](https://fly.io/dashboard)

## 💻 Descrição
**Exemplo de projeto Django para deploy em Fly.io**


## 🔧 Passo a passo

### Rodar local
```sh
make run

# or
docker-compose up
```

### Fly.io
#### Create account
https://fly.io/dashboard


#### Install fly
https://fly.io/docs/hands-on/install-flyctl/


#### Login
```sh
flyctl auth login
```

#### Criar App
```sh
flyctl apps create
```

#### Trocar o nome do app em __fly.toml__ :
```sh
app = "your-app-name"
```

#### Criar DB
```sh
flyctl postgres create
# só ir aceitando as configurações padrão

# GUARDAR
# <your-app-name>: nome da aplicação
# <your-app-name-name-db>: nome do cluster do banco

# cria banco de dados no cluster para a aplicação utilizar
flyctl postgres attach --app <your-app-name> <your-app-name-db>
```

#### Secrets
```
flyctl secrets set DATABASE_URL=postgres://your-app-name:xxx@xxx.your-app-name-db.internal:5432/your-app-name

flyctl secrets set ALLOWED_HOSTS=["your-app-name-name.fly.dev"]

flyctl secrets set CORS_ALLOWED_ORIGINS=["https://your-site.com"]
```

#### Deploy
```sh
flyctl deploy
```

#### Migrate
```sh
flyctl ssh console -C 'python manage.py migrate'
flyctl ssh console -C 'python manage.py createsuperuser'
```