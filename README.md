# Cursos-Django

[![licence mit](https://img.shields.io/badge/licence-MIT-blue)](LICENSE)

> Um simples projeto Django, para hospedar cursos.

## Tecnologias e libs utilizadas:

As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)

## Como executar o projeto

Para executar o projeto você precisa ter o [Python](https://www.python.org/) e o [Git](https://git-scm.com) instalados na sua maquina. Você também precisará de um editor de código, eu utilizei o [VSCode](https://code.visualstudio.com).

1. Clone esse repositório.

```
$ git clone https://github.com/ShadowsS01/Cursos-Django.git
```

2. Acesse a pasta do projeto.

```
$ cd Cursos-Django
```

3. Inicie um ambiente virtual e ative-o. Se não souber como, isso pode ajudar (https://docs.python.org/pt-br/3/tutorial/venv.html).

4. Depois é só instalar as dependência usando:

```
$ pip install -r requirements.txt
```

5. Então com o VsCode aberto na pasta do projeto, vá na pasta "plataforma_cursos" e abra o "settings.py". 

6. Troque o valor da constante `SECRET_KEY` para uma senha qualquer, e do `DEBUG` para `True`. Dessa forma:

```
SECRET_KEY = "Senha Qualquer"

DEBUG = True
```

7. Agora precisamos fazer as migrações para o banco de dados, só rodar no terminal:

```
$ python manage.py migrate
```

8. Criando o Super Usuário.
    - Ele vai pedir algumas informações do tipo usuário, e-mail e senha.
    - Digite o que desejar, recomendo só digitar um usuário e uma senha que se lembre, só para conseguir acessar a área administrativa.

```bash
$ python manage.py createsuperuser
```

9. Agora pode executar a aplicação em modo de desenvolvimento.

```
$ python manage.py runserver
```
   - A aplicação inciará localmente - acesse (http://127.0.0.1:8000/)

   - Na URL depois do `8000` dígite `/auth/cadastro` ou para acessar a área administrativa `/admin`.

   - Na área administrativa coloque o usuário e senha criados na parte 8.


10. **E pronto agora você pode olhar tudo e descobrir como funciona a aplicação. _Lembrando_ que a URL sempre vai ser [aqui](http://127.0.0.1:8000/auth/cadastro).
Apartir daí crie um usuário e entre na home do site fazendo o login.**


## Licença

Este projeto esta sobe a licença [MIT](LICENSE)

