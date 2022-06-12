from datetime import datetime, timedelta


def get_birthdays_per_week(users):

    today = datetime.now()

    range_start = 5 - today.weekday()
    
    ymd_list = [[(today + timedelta(days=delta)).year,
                 (today + timedelta(days=delta)).month,
                 (today + timedelta(days=delta)).day] for delta in range(range_start, range_start+7)]

    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Monday', 'Monday']
    week_birthdays = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
    for user in users:
        for ymd in ymd_list:
            if [user['birthday'].month, user['birthday'].day] == [ymd[1], ymd[2]]:
                week_birthdays[week_days[datetime(ymd[0], ymd[1], ymd[2]).weekday()]].append(user['name'])
                break

    for key, value in week_birthdays.items():
        if value != []:
            print(f'{key}: {", ".join(value)}')


get_birthdays_per_week([{'name': 'Фунтик', 'birthday': datetime(year=2000, month=3, day=1)},
                        {'name': 'Рик', 'birthday': datetime(year=2001, month=3, day=1)},
                        {'name': 'Морти', 'birthday': datetime(year=1999, month=5, day=12)},
                        {'name': 'Пупырка', 'birthday': datetime(year=2000, month=12, day=13)},
                        {'name': 'Киборг', 'birthday': datetime(year=2003, month=2, day=8)},
                        {'name': 'Пенелопа Круз', 'birthday': datetime(year=1995, month=2, day=14)})
