**Тестовое задание «Электронный магазин»**

Создайте виртуальное окружение poetry командой:

    poetry init

Установите зависимости командой:
   
    poetry install

Создайте миграции командами:
python manage.py makemigrations

    python manage.py migrate

Хапустите сервер:

    python manage.py runserver

Создайте Базу Данных (в данном проекте используется PostgreSQL).

Перейдите в файл '.env.sample'. Заполните в этом файле все необходимые поля, создайте в директории проекта файл '.env' и перенесите туда заполненный в '.env.sample' шаблон.

Ниже приведен пример заполнения:



    POSTGRES_NAME= *название базы данных*
    POSTGRES_PASSWORD= *пароль от базы данных*
    POSTGRES_HOST= *хост базы данных*
    POSTGRES_USER= *имя пользователя базы данных*
    HOST_DOMEN=http://127.0.0.1:8000/

С помощью декоратора action реализуется очищения объекта сети от долгов, если пользователь является админом. 
Следует отправить GET запрос по адресу, подставляя вместо pk айди нужного объекта сети.

    http://localhost:8000/provider/{pk}/clean_debt/

Ссылка на поставщика реализована через магический метод str, так как только админ сможет видеть отображение ссылки и не придется создавать отдельное поле в модели.

Иерархия автоматически соблюдается при создании и изменении объекта сети.

Для регистрации используется система токенов, следует отправить POST запрос с данными зарегистрированного пользователя и получить токен для доступа к урлам

Создать тестового админ пользователя можно базовой командой:
    
    python manage.py createsuperuser
