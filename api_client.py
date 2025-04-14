import json
import requests

headers = {'Content-Type': 'application/json'}
url_base = "http://185.104.249.229:3001"

# Конечные точки ключевых метрик
endpoint_get_count_subdued_headman = "/headman/subdued/count"
endpoint_get_count_registered_headman = "/headman/registered/count"
endpoint_get_count_opened_miniapp_headman = "/headman/opened-miniapp/count"
endpoint_get_count_opened_current_lesson_headman = "/headman/opened-current-lesson/count"
endpoint_get_count_saved_attendance_headman = "/headman/saved-attendance/count"

endpoint_get_count_opened_miniapp_every_day = "/headman/opened-miniapp/count/every-day"
endpoint_get_count_opened_current_lesson_headman_every_day = "/headman/opened-current-lesson/count/every-day"
endpoint_get_count_saved_attendance_headman_every_day = "/headman/saved-attendance/count/every-day"


def get_count_subdued_headman():
    """
        Получает количество приглашенных в проект старост.

        Returns:
            dict: Ответ от API в формате JSON в случае успеха, или сообщение об ошибке (str).
        """
    try:
        response = requests.get(
            url_base + endpoint_get_count_subdued_headman,
            headers=headers)
        response.raise_for_status()  # Вызывает исключение для ошибок 4xx и 5xx
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return f"Ошибка API: {e}"
    except json.JSONDecodeError as e:
        return f"Ошибка разбора JSON: {e}"


def get_count_registered_headman():
    """
        Получает количество зарегистрированных старост.

        Returns:
            dict: Ответ от API в формате JSON в случае успеха, или сообщение об ошибке (str).
    """
    try:
        response = requests.get(
            url_base + endpoint_get_count_registered_headman,
            headers=headers)
        response.raise_for_status()  # Вызывает исключение для ошибок 4xx и 5xx
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return f"Ошибка API: {e}"
    except json.JSONDecodeError as e:
        return f"Ошибка разбора JSON: {e}"


def get_count_opened_miniapp_headman(start_date, end_date):
    """
        Получает количество старост, открывших miniapp.

        Args:
        start_date (str): Начальная дата в формате 'YYYY-MM-DD'.
        end_date (str): Конечная дата в формате 'YYYY-MM-DD'.

        Returns:
            dict: Ответ от API в формате JSON в случае успеха, или сообщение об ошибке (str).
    """
    try:
        data_payload = {'startDate': start_date, 'endDate': end_date}
        response = requests.post(
            url_base + endpoint_get_count_opened_miniapp_headman,
            data=json.dumps(data_payload),
            headers=headers)
        response.raise_for_status()  # Вызывает исключение для ошибок 4xx и 5xx
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return f"Ошибка API: {e}"
    except json.JSONDecodeError as e:
        return f"Ошибка разбора JSON: {e}"


def get_count_opened_current_lesson_headman(start_date, end_date):
    """
        Получает количество старост, открывших текущую пару.

        Args:
        start_date (str): Начальная дата в формате 'YYYY-MM-DD'.
        end_date (str): Конечная дата в формате 'YYYY-MM-DD'.

        Returns:
            dict: Ответ от API в формате JSON в случае успеха, или сообщение об ошибке (str).
    """
    try:
        data_payload = {'startDate': start_date, 'endDate': end_date}
        response = requests.post(
            url_base + endpoint_get_count_opened_current_lesson_headman,
            data=json.dumps(data_payload),
            headers=headers)
        response.raise_for_status()  # Вызывает исключение для ошибок 4xx и 5xx
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return f"Ошибка API: {e}"
    except json.JSONDecodeError as e:
        return f"Ошибка разбора JSON: {e}"


def get_count_saved_attendance_headman(start_date, end_date):
    """
        Получает количество старост, открывших сохранивших посещаемость.

        Args:
        start_date (str): Начальная дата в формате 'YYYY-MM-DD'.
        end_date (str): Конечная дата в формате 'YYYY-MM-DD'.

        Returns:
            dict: Ответ от API в формате JSON в случае успеха, или сообщение об ошибке (str).
    """
    try:
        data_payload = {'startDate': start_date, 'endDate': end_date}
        response = requests.post(
            url_base + endpoint_get_count_saved_attendance_headman,
            data=json.dumps(data_payload),
            headers=headers)
        response.raise_for_status()  # Вызывает исключение для ошибок 4xx и 5xx
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return f"Ошибка API: {e}"
    except json.JSONDecodeError as e:
        return f"Ошибка разбора JSON: {e}"


def get_count_opened_miniapp_every_day(start_date, end_date):
    """
    Получает количество открытий miniapp из API за указанный период.

    Args:
        start_date (str): Начальная дата в формате 'YYYY-MM-DD'.
        end_date (str): Конечная дата в формате 'YYYY-MM-DD'.

    Returns:
        dict: Ответ от API в формате JSON в случае успеха, или сообщение об ошибке (str).
    """
    try:
        data_payload = {'startDate': start_date, 'endDate': end_date}
        response = requests.post(
            url_base + endpoint_get_count_opened_miniapp_every_day,
            data=json.dumps(data_payload),
            headers=headers)
        response.raise_for_status()  # Вызывает исключение для ошибок 4xx и 5xx
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return f"Ошибка API: {e}"
    except json.JSONDecodeError as e:
        return f"Ошибка разбора JSON: {e}"


def get_count_opened_current_lesson_headman_every_day(start_date, end_date):
    """
    Получает количество открытий текущей пары из API за указанный период.

    Args:
        start_date (str): Начальная дата в формате 'YYYY-MM-DD'.
        end_date (str): Конечная дата в формате 'YYYY-MM-DD'.

    Returns:
        dict: Ответ от API в формате JSON в случае успеха, или сообщение об ошибке (str).
    """
    try:
        data_payload = {'startDate': start_date, 'endDate': end_date}
        response = requests.post(
            url_base + endpoint_get_count_opened_current_lesson_headman_every_day,
            data=json.dumps(data_payload),
            headers=headers)
        response.raise_for_status()  # Вызывает исключение для ошибок 4xx и 5xx
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return f"Ошибка API: {e}"
    except json.JSONDecodeError as e:
        return f"Ошибка разбора JSON: {e}"


def get_count_saved_attendance_headman_every_day(start_date, end_date):
    """
    Получает количество сохранений посещаемости из API за указанный период.

    Args:
        start_date (str): Начальная дата в формате 'YYYY-MM-DD'.
        end_date (str): Конечная дата в формате 'YYYY-MM-DD'.

    Returns:
        dict: Ответ от API в формате JSON в случае успеха, или сообщение об ошибке (str).
    """
    try:
        data_payload = {'startDate': start_date, 'endDate': end_date}
        response = requests.post(
            url_base + endpoint_get_count_saved_attendance_headman_every_day,
            data=json.dumps(data_payload),
            headers=headers)
        response.raise_for_status()  # Вызывает исключение для ошибок 4xx и 5xx
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return f"Ошибка API: {e}"
    except json.JSONDecodeError as e:
        return f"Ошибка разбора JSON: {e}"
