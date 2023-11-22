import requests
import re

url = 'https://rozetka.com.ua/apple-iphone-15-pro-256gb-blue-titanium/p395460921//'

response = requests.get(url)
html_content = response.text

price_pattern = r'"price":"(\d+)","priceCurrency"'
matches = re.search(price_pattern, html_content)

if matches:
    actual_price = matches.group(1)
    print('Актуальна ціна:', actual_price, 'UAH')
else:
    print('Ціна не знайдена')


# import requests
# import re

# Вказуємо URL-адресу сторінки, з якої хочемо отримати ціну товару
# url = 'https://rozetka.com.ua/apple-iphone-15-pro-256gb-blue-titanium/p395460921//'

# Відправляємо HTTP-запит до вказаної URL-адреси і отримуємо відповідь
# response = requests.get(url)

# Отримуємо HTML-зміст сторінки з відповіді на запит
# html_content = response.text

# Визначаємо регулярний вираз для пошуку ціни на товар в HTML-змісті сторінки
# price_pattern = r'"price":"(\d+)","priceCurrency"'

# Шукаємо співпадіння за заданим регулярним виразом в HTML-змісті сторінки
# matches = re.search(price_pattern, html_content)

# Перевіряємо, чи знайдені співпадіння за заданим регулярним виразом
# if matches:
    # Якщо співпадіння знайдені, отримуємо фактичну ціну товару з першої групи регулярного виразу
# actual_price = matches.group(1)
    # Виводимо фактичну ціну товару разом з повідомленням на екран
# print('Актуальна ціна:', actual_price, 'UAH')
# else:
# Якщо співпадіння не знайдені, виводимо повідомлення про те, що ціну не вдалося знайти
# print('Ціна не знайдена')
