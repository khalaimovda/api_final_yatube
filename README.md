# API Final YaTube

### Описание
Проект реализует REST API для социальной сети YaTube. API позволяет:
- Просматривать, создавать, редактировать и удалять посты
- Просматривать, создавать, редактировать и удалять комментарии к постам
- Добавлять посты в группы
- Просматривать все посты, относящиеся к конкретной группе
- Оформлять подписки на различных авторов

### Запуск проекта в dev-режиме (Windows)

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/khalaimovda/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Перейти в директорию основного приложения:

```
cd yatube_api
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Аутентификация
Аутентификация на ресурсе происходит посредством JWT-токена. Для его получения необходимо выполнить запрос:
```
GET /api/v1/jwt/create/

{
    "username": "my_username",
    "password": "mypassword"
}
```
Ответ будет выглядеть примерно так:
```
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzMjE1OTU2OSwianRpIjoiNWZlNjUxNjEyMDFmNDIwYjg3Y2YxMTIwYjliNzNkMzUiLCJ1c2VyX2lkIjoxfQ.Ugsfl2RUAsIYSnErd4ubDaOLhmCm3yQ3paik90OvQFI",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMTU5NTY5LCJqdGkiOiIwYzdhOTY0NDgzNGY0NDk1OThmZDJjNzc4NWI1YzhkOCIsInVzZXJfaWQiOjF9.Igd-9ApQ-wNPo3-tQM_t3ppX6wJ_DNL_C0QP7hR1-PU"
}
```
Все последующие запросы к ресурсу отправлять с заголовком
```
Authorization: Bearer access_токен
```



### Примеры запросов к API
Получить список всех постов (поддерживаются параметры limit и offset)
```
GET /api/v1/posts/
```

Получить пост с id = 1
```
GET /api/v1/posts/1/
```

Создать пост
```
POST /api/v1/posts/

{
  "text": "Текст поста"
}
```

Обновить содержимое поста с id = 1
```
PUT/PATCH /api/v1/posts/1/

{
  "text": "Текст поста"
}
```

Удалить пост с id = 1
```
DELETE /api/v1/posts/1/
```

Получить список всех комментариев поста с id = 1
```
GET api/v1/posts/1/comments/
```

Добавить комментарий для поста с id = 1
```
POST api/v1/posts/1/comments/

{
  "text": "Текст комментария ",
}
```

Получить комментарий с id = 2 поста с id = 1
```
GET api/v1/posts/1/comments/2/
```

Отредактировать комментарий с id = 2 поста с id = 1
```
PUT/PATCH  api/v1/posts/1/comments/2/

{
  "text": "Текст комментария ",
}
```

Удалить комментарий с id = 2 поста с id = 1
```
DELETE api/v1/posts/1/comments/2/
```

Получить информацию обо всех группах
```
GET api/v1/groups/
```

Получить информацию о группе с id = 3
```
GET api/v1/groups/3/
```

Получить список всех ваших подписок
```
GET /api/v1/follow/
```

Оформить подписку на автора с username = author_username
```
POST /api/v1/follow/

{
"following": author_username
}
```

**Более подробную документацию API смотрите на**

```
/swagger/
```

### Авторы

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Дмитрий Халаимов
