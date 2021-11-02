<h1 align="center">Сайт для рецептов</h1>
<img src="https://img.shields.io/github/languages/top/lavalera97/recipe-site">
<img src="https://img.shields.io/tokei/lines/github.com/lavalera97/recipe-site">

## Превью сайта
<p align="center">
<img src="https://media.giphy.com/media/ev6gjk7aF5z0eQbQiD/giphy.gif" width="85%" style="border-radius: 2%"></p>

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


