
from datetime import datetime


def get_days_from_today(date):
    if not isinstance(date, str) or not date.strip():
        return "Помилка! рядок не повинен бути порожнім. Введіть дату в форматі 'PPPP-MM-ДД'."

    try:
        dt1 = datetime.strptime(date, "%Y-%m-%d").date()
        dt2 = datetime.today().date()
        td = dt2-dt1
    
        return td.days
    except ValueError:
        return "Неправельний формат дати. Використовуйте 'PPPP-MM-ДД'."

# перевірка роботи функції 
print(get_days_from_today("2025-03-9"))
print(get_days_from_today("2025-03-14"))
print(get_days_from_today(None))
print(get_days_from_today(""))
print(get_days_from_today("sf123asd"))



 