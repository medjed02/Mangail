from requests import delete, post, get, put
import datetime


# Получение всех пользователей
print(get('http://127.0.0.1:8080/api/users').json())

# Получение одного пользователя
print(get('http://127.0.0.1:8080/api/user/1').json())

# Обращение к несуществующему id пользователя
print(get('http://127.0.0.1:8080/api/user/100').json())

# Строка вместо id пользователя
print(get('http://127.0.0.1:8080/api/user/aaa').json())

# Получение всех жанров
print(get('http://127.0.0.1:8080/api/genres').json())

# Получение одного жанра
print(get('http://127.0.0.1:8080/api/genre/1').json())

# Обращение к несуществующему id жанра
print(get('http://127.0.0.1:8080/api/genre/100').json())

# Строка вместо id жанра
print(get('http://127.0.0.1:8080/api/genre/aaa').json())

# Получение всех манг
print(get('http://127.0.0.1:8080/api/mangas').json())

# Получение одной манги
print(get('http://127.0.0.1:8080/api/manga/1').json())

# Обращение к несуществующему id манги
print(get('http://127.0.0.1:8080/api/manga/100').json())

# Строка вместо id манги
print(get('http://127.0.0.1:8080/api/manga/aaa').json())

# Получение всех постов
print(get('http://127.0.0.1:8080/api/messages').json())

# Получение одного поста
print(get('http://127.0.0.1:8080/api/message/1').json())

# Обращение к несуществующему id поста
print(get('http://127.0.0.1:8080/api/message/100').json())

# Строка вместо id поста
print(get('http://127.0.0.1:8080/api/message/aaa').json())