# Фреймворк Django (семинары)

Установка и запуск

- Создать и инициализировать виртуальное окружение

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

- Установить нужные библиотеки

    ```bash
    pip install -r requirements.txt
    ```

- Запустить сервер

    ```bash
    cd homeproject
    python manage.py runserver
    ```

- Создать миграции и заполнить фейковыми данными для магазина (shop app)

  ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py fill_fake_orders --products=20 --customers=10 --orders=40
    ```

## Урок 3. Шаблоны, классы и формы

**shop** - добавлены шаблоны для отображения заказов клиента и заказанных им товаров за последние недею, месяц, год

По адресу ```http://127.0.0.1:8000/shop``` - список клиентов. 

По адресам

- ```http://127.0.0.1:8000/shop/customers/<cust_id>/orders/``` - все заказы клиента с ```<cust_id>```

- ```http://127.0.0.1:8000/shop/customers/<cust_id>/products/<period>/``` - все заказанные клиентом с ```<cust_id>``` товары за последний период ```<period>```

## Урок 2. Django ORM и связи

  **blog**: Модели - "Автор", "Статья" и "Комментарий" и CRUD операции на ними
  
  **shop**:

- Модели "Клиент", "Товар" и "Заказ"
- CRUD операции:
  - fill_fake_orders - заполнить БД тестовыми данными (по умолчанию создается: 10 товаров, 10 клиентов и 10 заказов)
  - create_cuctomer - добавить клиента
  - update_cuctomer - изменить информацию о клиенте
  - delete_customer_by_id - удалить информацию о клиенте
  - get_customers - получить список \<n> клиентов отсортированных по имени (по умолчанию 10)
  - get_customer_by_email - найти клиента по email
  - get_customer_by_name - найти клиента по части имени беp учета регистра
  - create_product - добавить новый товар
  - update_product - изменить информацию о товаре
  - delete_product_by_id - удалить товар
  - get_products - получить список \<n> товаров отсортированных по имени (по умолчанию всех)
  - get_product_by_title - найти товар по части названия беp учета регистра
  - create_order_for_customer - создать заказ для клиента
  - get_orders_by_customer_id - получить список \<n> последних заказов по клиента по id (по умолчанию всех)
  - get_orders_by_customer_name - получить список \<n> последних заказов по клиента по имени (по умолчанию всех)
  - get_orders - получить список \<n> последних заказов всех клинтов (по умолчанию - всех)
  - delete_order_by_id - удалить заказ

## Урок 1. Первое Знакомство с Django

По адресу <http://127.0.0.1:8000> - главная

По адресу <http://127.0.0.1:8000/about> - о себе
