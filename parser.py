import sys
from datetime import datetime, timedelta

import requests
import dateutil.tz
from icalendar import Calendar, Event
from requests.utils import dict_from_cookiejar


def parse(url: str, sheet_id: str) -> list:
    session = requests.session()
    token_response = session.get(url)

    if token_response.status_code != 200:
        print('Ошибка при получении файла')
        exit()

    url_parts = url.split('/')
    base_url = "/".join(url_parts[:4])
    account_id = url_parts[6]
    file_id = url_parts[7]

    cookies = dict_from_cookiejar(session.cookies)
    token = cookies.get('drive-sharing-' + file_id)

    if not token:
        print('Ошибка при получении токена')
        exit()

    object_id = api_call(base_url + "/oo/r/webapi/entry.cgi/SYNO.Office.Node", {
        "api": "SYNO.Office.Node",
        "method": "get",
        "version": "1",
        "basic": "true",
        "path": f"%22link:{account_id}%22",
        "sharing_token": f"%22{token}%22"
    })['data']['object_id']

    table_data = api_call(base_url + "/d/s/" + account_id + "/webapi/entry.cgi/SYNO.Office.Sheet.Snapshot", {
        "api": "SYNO.Office.Sheet.Snapshot",
        "method": "get",
        "version": "1",
        "password": "%22%22",
        "object_id": f"%22{object_id}%22",
        "sharing_token": f"%22{token}%22"
    })['data'][sheet_id]['cells']

    return dict_to_list(table_data)


def api_call(url: str, params: dict) -> dict:
    payload = "&".join([f"{key}={value}" for key, value in params.items()])
    api_response = requests.post(url, data=payload)

    if api_response.status_code != 200:
        print('Ошибка при вызове API')
        exit()

    return api_response.json()


def dict_to_list(d):
    if isinstance(d, dict):
        # Получаем все числовые ключи
        numeric_keys = [int(key) for key in d.keys() if key.isdigit()]
        if numeric_keys:
            max_index = max(numeric_keys)
            result = [None] * (max_index + 1)
            for key, value in d.items():
                if key.isdigit():
                    result[int(key)] = dict_to_list(value)
        else:
            result = d  # Если нет числовых ключей, возвращаем словарь как есть
        return result
    elif isinstance(d, list):
        return [dict_to_list(element) for element in d]
    else:
        return d


def save_ical(timetable: list, filename='timetable.ics'):
    cal = Calendar()

    for w in range(3, len(timetable), 1):
        for h in range(1, 14):  # колонки B-N
            add_event(cal, timetable, w, h)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(cal.to_ical().decode('utf-8').replace('\r\n', '\n').strip())


def add_event(cal, timetable, week, hour):
    lesson = timetable[week][hour]

    if lesson is None or 'v' not in lesson or not lesson['v'] or not isinstance(lesson['v'], str):
        return

    if any(word in lesson['v'].lower() for word in ['праздник', 'выходной', 'каникулы', 'сессия']):
        return

    t = get_hours(hour)
    i = get_date_cell_for_hour(hour)

    week -= 1

    for _ in range(3):
        if is_date_value(timetable[week][i]):
            break
        week -= 1
    else:
        return

    start_date = datetime(1900, 1, 1, tzinfo=dateutil.tz.tzstr("Europe/Moscow"))
    date = start_date + timedelta(days=int(timetable[week][i]['v']) - 2)

    event = Event()
    event.add('summary', lesson['v'])
    event.add('dtstart', date.replace(hour=t[0][0], minute=t[0][1]))
    event.add('dtend', date.replace(hour=t[1][0], minute=t[1][1]))
    cal.add_component(event)


def get_date_cell_for_hour(h):
    saturday = 11
    return saturday if h >= saturday else h if h % 2 != 0 else h - 1


def is_date_value(lesson):
    return 'v' in lesson and isinstance(lesson['v'], int)


def get_hours(index):
    times = [
        [[19, 00], [20, 30]], [[20, 40], [22, 10]],  # Monday
        [[19, 00], [20, 30]], [[20, 40], [22, 10]],  # Tuesday
        [[19, 00], [20, 30]], [[20, 40], [22, 10]],  # Wednesday
        [[19, 00], [20, 30]], [[20, 40], [22, 10]],  # Thursday
        [[19, 00], [20, 30]], [[20, 40], [22, 10]],  # Friday
        [[11, 00], [12, 30]], [[12, 40], [14, 10]], [[14, 20], [15, 50]]  # Saturday
    ]
    return times[index-1]


def run(file_url, sheet_id, file_name):
    timetable = parse(file_url, sheet_id)
    save_ical(timetable, file_name)

    print('Расписание сохранено')


if __name__ == '__main__':
    run(file_url=sys.argv[1], sheet_id=sys.argv[2], file_name=sys.argv[3])
