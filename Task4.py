from datetime import datetime, timedelta 

users = [
    {"name": "John Doe", "birthday": "1985.03.14"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Smit Krak", "birthday": "1985.03.15"},
    {"name": "Angela Bim", "birthday": "1985.03.16"}
]

def get_upcoming_birthdays(users):

    
    today = datetime.today().date() #Визначаємо поточну дату системи
    upcoming_birthdays = []


    for user in users:
        name = user['name']
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date() #Конвертуємо дату народження із рядка в обєкти 
        birthday_this_year = birthday.replace(year=today.year)            #Визначаємо день народження у поточному році 

        # Якщо день народження був цього року, переносимо на наступний рік 
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year = today.year + 1)

        #Перевіряємо чи входить день народження в найблищі 7 днів 
        delta_days = (birthday_this_year - today).days
        if 0<= delta_days <=7:

            # Переносим на понеділок якщо день народження випадає на вихідний  
            while birthday_this_year.weekday() in [5,6]:                        #5- субота, 6- неділля 
                birthday_this_year = birthday_this_year + timedelta(days=1)

            # зберігаємо імя і дату того кого потрібно привітати    
            upcoming_birthdays.append({"name": name, "congratulation_date":birthday_this_year.strftime("%Y.%m.%d")})

    
    
    
    return upcoming_birthdays
    
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)