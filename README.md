# drfsite
## Описание проекта
REST API сервис для работы с списком задач на Django Rest Framework.
Цель проекта - получить практический опыт разработки.

## Основной функционал:
1. Регистрация и аутентификация пользователей:  
      для аутентификации реализованы: session based authentication, token based authentication и 
      JSON Web Token authentication (организовано с помощью библиотеки Djoser). 
      Декодировать токен можно по [ссылке](https://jwt.io) для подробной информации.  
2. CRUD операции с задачами (с помощью permission):  
      чтение статей (всем пользователям);  
      добавление, изменение статьи (только авторизованным пользователем);   
      удаление статей (только администратор).  
3. Постраничная навигация для удобства просмотра.

## Установка
1.Склонируйте репозиторий на свой локальный компьютер и перейдите в директорию проекта:
```python
git clone https://github.com/alenaVSk/drf_project.git

cd drf_project
```
3. Создайте и активируйте виртуальное окружение:
```python
python -m venv venv

source venv/bin/activate   # для Windows: venv\Scripts\activate
```
4. Установите зависимости из файла requirements.txt:    
```python
pip install -r requirements.txt
```
5. Настройте базу данных:
```python
python manage.py makemigrations
python manage.py migrate
```
6. Запустите проект:
```python
python manage.py runserver
```
7. После этого приложение будет доступно по адресу http://localhost:8000.
## Использование  
'api/v1/delisious_way/': получить все объекты    
'api/v1/delisious_way/<int:pk>/': получить объект по id для чтения и изменения    
'api/v1/delisious_waydelete/<int:pk>/': удалить объект по id  

аутентификация по сессиям:  

'api/v1/drf-auth/login/'  
'api/v1/drf-auth/logout/'  
'api/v1/auth/': ссылка на список пользователей

аутентификация по JWT токенам:  

'api/v1/token/': получить refrsh и access токены  
'api/v1/token/refresh/': получить access токен   
'api/v1/token/verify/': проверка на действительность токена
  
## Пагинация  
Результаты запросов разделены на страницы для удобства навигации.  
Используйте параметр page_size для контроля отображаемых результатов.  
Пример:  
'api/v1/delisious_way/?page_size=3'  
## Тестирование  
Для тестирования API вы можете использовать Postman.  


