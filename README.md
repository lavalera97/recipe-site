<h1 align="center">Сайт для рецептов</h1>
<img src="https://img.shields.io/github/languages/top/lavalera97/recipe-site">
<img src="https://img.shields.io/tokei/lines/github.com/lavalera97/recipe-site">

## Превью сайта
<p align="center">
<img src="https://media.giphy.com/media/L568DgyPMyLyFwMLeq/giphy.gif" width="80%" style="border-radius: 2%; max-width:100%;"></p>

### Инструкция по использованию
1. Установить <strong> [Docker](https://www.docker.com/) </strong>
2. Скачать репозиторий и разархивировать или использовать git clone
```
git clone https://github.com/lavalera97/recipe-site.git
```
3. Перейти в папку проекта и выполнить команду( при первом запуске это займет некоторое время ):
```
docker-compose up --build
```
4. Зайти в bash контейнера
```
docker-compose exec web bash
```
> При использовании git bash перед командой написать winpty

5. Выполнить команду по сбору static файлов
```
python manage.py collectstatic
```

6. Создать superuser для дальнейшего использования admin панели.
```
python manage.py createsuperuser
```
> Вход в админ панель производится с помощью email 

> http://127.0.0.1:8000/admin

7. Загружаем наши первоначальные данные из фикстур
```
python manage.py loaddata account ingredient category recipe
```

8. Заходим на сайт по url:
> http://127.0.0.1:8000/

###Возможности сайта

* <strong>Авторизация пользователя</strong>
<img src="https://media.giphy.com/media/XO2OIrxGK7fxwLSJOk/giphy.gif" width="80%" style="border-radius: 2%; max-width:100%; padding-top:30px; padding-bottom: 20px"></p>
  
* <strong>Поиск по названию рецепта и ингредиентам</strong>
<img src="https://media.giphy.com/media/iWpxjbSYhGi692PSWF/giphy.gif" width="80%" style="border-radius: 2%; max-width:100%; padding-top:30px; padding-bottom: 20px"></p>

* <strong>Создание рецепта</strong> 
<img src="https://media.giphy.com/media/imL7HdWRJLmj8LMme0/giphy.gif" width="80%" style="border-radius: 2%; max-width:100%; padding-top:30px; padding-bottom: 20px"></p>

* Изменение уже существующего рецепта
<img src="https://media.giphy.com/media/mDVsqn5w3XdLiqzE8Q/giphy.gif" width="80%" style="border-radius: 2%; max-width:100%; padding-top:30px; padding-bottom: 20px"></p>


