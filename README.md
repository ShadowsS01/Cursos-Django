# Cursos-Django

[![licence mit](https://img.shields.io/badge/licence-MIT-blue)](LICENSE)

> Um simples projeto Django, para hospedar cursos.

## Tecnologias e libs utilizadas:

As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)

## Como executar o projeto

Para executar o projeto você precisa ter o [Python](https://www.python.org/) e o [Git](https://git-scm.com) instalados na sua maquina. Você também precisará de um editor de código, eu utilizei o [VSCode](https://code.visualstudio.com).

### 1. Clone esse repositório

```bash
git clone https://github.com/ShadowsS01/Cursos-Django.git
```

### 2. Acesse a pasta do projeto

```bash
cd Cursos-Django
```

### 3. Ambiente virtual

Inicie um ambiente virtual e ative-o. Se não souber como, isso pode ajudar: (<https://docs.python.org/pt-br/3/tutorial/venv.html>).

### 4. instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Modificar as Constantes

Na pasta do projeto, vá na pasta `plataforma_cursos` e abra o `settings.py`.
Troque o valor da constante `SECRET_KEY` para uma senha qualquer, e do `DEBUG` para `True`. Dessa forma:

```text
SECRET_KEY = "Digite_Uma_Senha_Secreta_aqui"
DEBUG = True
```

### 6. Migações no Banco Dados

Agora precisamos fazer as migrações para o banco de dados, só rodar no terminal:

```bash
python manage.py migrate
```

### 7. Criando o Super Usuário.
- Ele vai pedir algumas informações do tipo usuário, e-mail e senha.
- Digite o que desejar, recomendo só digitar um usuário e uma senha que se lembre, só para conseguir acessar a área administrativa.

```bash
python manage.py createsuperuser
```

### 9. Executando aplicação em modo de desenvolvimento

```bash
$ python manage.py runserver
```
- A aplicação inciará localmente - acesse: (<http://127.0.0.1:8000/>)

- Na URL depois do `8000` dígite `auth/cadastro/` ou para acessar a área administrativa `admin/`.

- Na área administrativa coloque o usuário e senha criados na [etapa 7](https://github.com/ShadowsS01/Cursos-Django#7-criando-o-super-usu%C3%A1rio).

- **Agora você pode olhar tudo e descobrir como funciona a aplicação. _Lembrando_ que a URL sempre vai ser [aqui](http://127.0.0.1:8000/auth/cadastro).
Apartir daí crie um usuário e entre na home do site fazendo o login.**


## Licença

Este projeto esta sobe a licença [MIT](LICENSE)
