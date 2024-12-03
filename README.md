# Basic Django application: Specification

We’d like you to build a REST API for us - a basic currency exchange database.
Interacting with external API just to load initial data to the database. Here’s the full
specification of endpoints that we’d like it to have:

● GET /currency/

    ○ It should fetch a list of all currencies already present in the local
    application database. List of currencies not currency pairs. Result should
    be [{“code”: “USD”}, {“code”: “SGD”}, {“code”: “PLN”}]

    ○ Additional filtering sorting is entirely optional - but some implementation is
    a bonus.

● GET /currency/EUR/USD/(required)

    ○ It should fetch latest exchange rate for EUR/USD present in the local
    application database. Result should be like {“currency_pair”: “EURUSD”,
    “exchange_rate”:1.034}

Admin interface is not optional. It should allow us to list historical rates for specific
currency pairs.

### Rules

● Load data from an external database. Currency and rates should be stored in
the local database. We recommend Yahoo and
https://github.com/ranaroussi/yfinance, but you can change. You should load at
least EURUSD, USDJPY, PLNUSD.

● The goal is to implement the REST API in Django. You're free to use any third-
party libraries - sharing your reasoning behind choosing them is welcome!

● Database selection is limited to MySQL or SqlLite.

● Endpoint must use a local database.

● Basic tests of endpoints are obligatory. Their exact scope is left up to you.

● We do not require any authorization/authentication system(s).

● The application's code should be in a public repository!

---

## How to run (commands for linux)

1. Install venv `python3 -m venv venv`

2. Run venv `source venv/bin/activate`

3. Install requirements.txt `pip install -r requirements`

4. Create migrations `python3 manage.py makemigrations`

5. Migrate `python3 manage.py migrate`

6. Run command `python3 manage.py load_currencies`

7. Run server `python manage.py runserver`

8. Run tests `pytest`

9. Enjoy!

## Screens

![general screen of Swagger](https://i.imgur.com/HzyqhCM.png "Swagger General")

![specyfic endpoint from Swagger](https://i.imgur.com/LK13W8F.png "Swagger specyfic")