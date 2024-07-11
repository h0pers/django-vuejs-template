
# Django + Vue js Template

This template will help you descrease your developing time instead of thinking structure.
To handle easy API Endpoints in VUE was added swagger support with **drf-yasg**.


![Logo](https://miro.medium.com/v2/resize:fit:640/1*n9MSMu6_-0cODbeItES0wQ.png)
## 🛠 Installing
Clone the project in folder where your project would be locate.

```
git clone link
```

Super, project mostly ready. Now you shuold choose what you would like to develop first, front or back.
For example i will choose frontend first.

Your VUE project will locate in frontend folder
```
cd frontend
```
Develope frontend and back when it will be ready
```
npm run dev
```
Super, it`s ready and we can go next, build your vue project using command.
```
npm run build
```

Now we can check is vue project susscessfuly displays in django backend.
Create .env file in backend folder with specials variables, here is example of it.

```
SECRET_KEY=hello-world-key
DEBUG=True
ALLOWED_HOSTS=*
CORS_ALLOWED_ORIGINS=http://*
CSRF_TRUSTED_ORIGINS=http://*
LANGUAGE_CODE=en-us
TIME_ZONE=Europe/Kyiv
USE_I18N=True
USE_TZ=True

DB_NAME=django_db
DB_USERNAME=postgres
DB_HOST=127.0.0.1
DB_PORT=5433
DB_PASSWORD=root
```

Please make sure you have changed this variables in deploy.
```
python manage.py migrate
```
```
python manage.py runserver
```

Greate, connect your Frontend with backend and deploy the project using [official django documentation](https://docs.djangoproject.com/en/4.2/howto/deployment/)

![Logo](https://miro.medium.com/v2/resize:fit:1400/1*94DMaC239Dq_UTI_S4-qrg.png)
## Author Links 🖇️

- [Github](https://github.com/h0pers)
- [Telegram](https://t.me/dhryshchenkowork)

