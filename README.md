
# Online Store QA Tests

Демонстрационный проект автоматизации тестирования для интернет-магазина [demoblaze.com].

## Стек:
- Python 3
- Selenium
- Pytest
- Page Object Model
- GitHub Actions (CI/CD)
- SQL и API тесты

## Запустить
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
pytest -v
```
## Структура 
online-store-qa-tests/
│
├── tests/  
│   ├── test_login.py       # UI-тест авторизации  
│   ├── test_add_to_cart.py  # UI-тест добавления товара в корзину  
│   └── test_api.py          # API-тест проверки статуса  
├── sql/
│   └── check_order.sql      # SQL-запрос проверки заказа
├── requirements.txt         # Зависимости проекта
└── README.md                # Документация проекта
