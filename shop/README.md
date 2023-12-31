Задача:
-------

* Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
* Django Модель Item с полями (name, description, price)
* API с двумя методами:
    * GET `/buy/{id}`, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении
      этого метода c бэкенда с помощью python библиотеки stripe должен выполняться
      запрос` stripe.checkout.Session.create(...)` и полученный session.id выдаваться в результате запроса
    * GET `/item/{id}`, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о
      выбранном `Item` и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на `/buy/{id}`, получение
      session_id и далее с помощью JS библиотеки Stripe происходить редирект на Checkout
      форму `stripe.redirectToCheckout(sessionId=session_id)`

* Залить решение на Github, описать запуск в README.md

* Запуск используя `Docker`

* Просмотр Django Моделей в Django Admin панели - __доступно по адресу `127.0.0.1:8000/admin`



Запуск
------

```
git clone https://github.com/danypet2/stripe_api_django.git
Заполнить в файле .env-non-dev секретный и публичный ключи stripe
```

Запуск Docker
------

```
git clone https://github.com/vadushkin/stripe_task.git
cd shop
docker-compose build
docker-compose up
```

#### Остановка docker:
```
docker-compose stop
```

Главная страница: http://localhost:8000/

Если сервер не отдаёт информацию, подождите пару секунд и перезагрузите страницу

Сервис
------

* `/item` - Все товары 
* `admin/` - Админка
* `buy/<item_id>` - Купить товар
* `item/<item_id>` - Страница товара

Скриншоты
---------


