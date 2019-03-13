# Django rest-framework API - (CRUD)
Tutorial de como criar uma api REST com python e django rest-framework, com manipulações básicas de um objeto, CRUD (create, read, update, delete).

### Contexto
Criação de uma aplicação server-side que permita algumas operações básicas de uma API, tomando como exemplo a criação e manipulação de palestras e palestrantes. Além de um CRUD básico, também será adicionado um filtro de listagem de palestra pela data do acontecimento.

### Preparando o ambiente
Vamos isolar nosso ambiente de desenvolvimento criando uma variável de ambiente:
```
$ virtualenv -p python3 env
$ source env/bin/activate
```
Instalando os requisitos:
```
$ pip install django
$ pip install djangorestframework
```
Vamos iniciar nosso projeto, criando a aplicação dentro de uma pasta desejada:
```
django-admin startproject meu_projeto .
```
O django irá criar para você dentro da pasta meu_projeto alguns arquivos, os quais vamos trabalhar:

```
diretorio_atual/
    manage.py
    meu_projeto/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```
### Criando banco de dados
Neste caso, utilizei o postgresql para aplicação rodando localmente. Em _settings.py_ vamos adicionar as credenciais do banco de dados e remover a configuração padrão do sqlite:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'rijgzlqt',
        'USER': 'rijgzlqt',
        'PASSWORD': 'my_password',
        'HOST': ''my_host',
        'PORT': '5432'
    }
}
```
### Criando nossa aplicação
Agora precisamos de uma app que irá rodar juntamente com nosso projeto, criaremos dentro do diretório principal:
```
$ python manage.py startapp app
```
Teremos dentro de nossa app, os sequintes arquivos:
```
app/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```
Em _settings.py_ devemos registras as seguintes APPs em INSTALLED_APPS:
```
    'rest_framework',
    'app',
```
Vamos começar editando o arquivo _models.py_, este será o arquivo que irá receber as informações para criar o banco de dados e será gerenciado pela aplicação. Neste caso, criaremos duas classes: Palestras e Palestrantes, e suas variávels para criação de tabelas:
```
from django.db import models


class Palestrante(models.Model):
    nome = models.CharField(max_length=50)
    bio = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.nome


class Palestra(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    data = models.DateField()
    hora = models.TimeField()
    palestrante = models.ForeignKey(
        'Palestrante', related_name='palestras', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

```
A _ForeignKey_ irá permitir que o usuário crie uma palestra selecionando um palestrante já existente em nosso banco de dados.

Agora vamos serializar nossos dados utilizando o arquivo serializers.py, este permite a tradução dos dados em um formato que pode ser transformado em outro ambiente computacional.
```
from rest_framework import serializers

from .models import Palestra, Palestrante


class PalestraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palestra
        fields = ('id', 'titulo', 'descricao', 'data','hora', 'palestrante')


class PalestranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palestrante
        fields = ('id', 'nome', 'bio', 'link')

```
Conforme dito anteriormente, queremos listar palestras de determinado dia, para isso, vamos criar dentro da nossa pasta app, um arquivo chamado _filters.py_, e vamos adicionar o seguinte código a ele:

```
from .models import Palestra
import django_filters

class PalestraFilter(django_filters.FilterSet):
    class Meta:
        model = Palestra
        fields = ['data',]
```

Nota:
> Devemos adicionar o _django_filters_ em INSTALLED_APPS e declarar as configurações de data e hora:
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DATE_FORMAT': "%m/%d/%Y",
    'TIME_FORMAT': "%H:%M"


Agora criaremos nossas Views em views.py, estas serão responsáveis por receber requisições web e retornar uma resposta a ela. Dentro dela iremos escrever as classes para a criação do nosso CRUD.
Há várias formas de criar métodos com a função de criar, listar, atualizar e deletar, mas algumas funcionalidades do rest-framework traz algumas facilidades, como o **Generics** **Views**, que torna o código mais curto de algumas operações rotineramente efetuadas.
```
from rest_framework.views import APIView
from .filters import PalestraFilter
from rest_framework import generics

from .models import Palestra, Palestrante
from .serializers import PalestraSerializer, PalestranteSerializer



class PalestraListCreate(generics.ListCreateAPIView):
    queryset = Palestra.objects.all()
    serializer_class = PalestraSerializer
    filter_class = PalestraFilter

class PalestraEditDel(generics.RetrieveUpdateDestroyAPIView):
    queryset = Palestra.objects.all()
    serializer_class = PalestraSerializer

(...)
```
Utilizaremos o _ListCreateAPIView_ para listar e criar palestras e palestrantes, e o _RetrieveUpdateDestroyAPIView_ para atualizar e deletar.
Note que _filter_class = PalestraFilter_ irá adicionar um botão na UI backend da nossa aplicação para fazer a filtragem por data.

Observação: aqui abordamos as principais alterações feitas nos arquivos do django, mas outros arquivos deverão ser atualizados para o funcionamento completo da aplicação, como _urls.py_, _admin.py_ e _app/urls.py_  que se encontram neste repositório.

### Rodando nossa aplicação:
Executamos os seguintes comandos para a atualização e migração das configurações do banco de dados:
```
$ python manage.py makemigrations
$ python mange.py migrate
```
Finalmente rodamos localmente nossa aplicação:
```
$ python manage.py runserver
```
## Deploy no Heroku
Para a disponibilidade da aplicação com uma url, utilizamos o Heroku.
### Instalação e inicialização
Utilizaremos o Heroku CLI, que pode ser instalado facilmente seguindo o tutorial oficial do [Heroku](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).
Também utilizaremos o Git, para versionamento e integração do deploy com o Heroku.
Após a instalação e login seguinto o tutorial oficial, vamos fazer push da nossa aplicação, com os seguintes passos:
```
$ git init
$ git add .
$ git commit -m 'First commit'
```
Feito isso, vamos esconder nossos arquivos sensíveis com o módulo _decouple_ e ignorar com .gitignore o que não queremos enviar para o repositório:
```
pip install python-decouple
```
_settings.py_:
```
from decouple import config
SECRET_KEY = config('SECRET_KEY')
```
A SECRET_KEY contida por padrão no arquivo settings será armazenada em um arquivo chamado .env em nosso diretório.
Coloque .env no arquivo .gitignore, juntamente com a virtualenv env, e db_sqlite.
### Banco de dados no Heroku.
o Heroku cria automaticamente uma url para um banco de dados postgresql na amazon, portanto, podemos remover as configurações do banco que criamos e inserir uma configuração padrão do db.sqlite:
```
pip install dj-database-url
```
_setting.py_
```
from dj_database_url import parse as dburl

default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = { 'default': config('DATABASE_URL', default=default_dburl, cast=dburl), }
```
### Configurando a URL
Crie um arquivo chamado Procfile no diretório raíz do projeto e armazene a seguinte configuração:
web: gunicorn website.wsgi --log-file -
"website" deverá ser substituido pelo nome do seu projeto.
Configurando host para direcionamento da aplicação:
_settings.py_:
```
ALLOWED_HOSTS = ['meu-projeto.herokuapp.com','127.0.0.1']
```
### Fazendo o Deploy
Antes de enviar seu projeto para o Heroku, precisamos enviar a variável de ambiente que criamos em .env através do plugin config:
```
$ heroku plugins:install heroku-config
$ heroku config:push -a
```
Para verificar:
```
$ heroku config
```
> Observação:
Talvez seja necessário adicionar ao config do heroku as seguintes variáveis:
$ heroku config:set DISABLE_COLLECTSTATIC=1
$ heroku config:set DEBUG=True


Para a exibição correta da nossa aplicação rest-framework na UI do backend, é necessário alterar a seguinte configuração em settings.py:
Comentar a primeira linha, em _SecurityMiddleware_ e adicionar a última: _'whitenoise.middleware.WhiteNoiseMiddleware'_.
```
MIDDLEWARE = [
    #'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
```
E finalmente enviamos nosso projeto para o repositório do Heroku e fazemos o deployment:
```
git add .
git commit -m 'Configuring the app'
git push heroku master --force
```
