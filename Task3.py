import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):

    phone_number = phone_number.strip() # видаляє пробіли 
    phone_number = re.sub(r'[^\d+]','', phone_number) # Видаляємо всі символи крім + і цифр 

    if re.match(r'\+380', phone_number):
        return phone_number
    elif re.match(r'380', phone_number):
        return f'+{phone_number}'
    elif re.match(r'0', phone_number):
        return f'+38{phone_number}'
    



    



sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)