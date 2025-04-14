from flask import Flask, render_template, request
from datetime import date

from api_client import *
from plotting import draw_histogram

app = Flask(__name__)


def write_count_subdued_headman():
    return get_count_subdued_headman()[0]['get_count_subdued_headman']


def write_count_registered_headman():
    return get_count_registered_headman()[0]['get_count_registered_headman']


def write_count_opened_miniapp_headman(start_date, end_date):
    return get_count_opened_miniapp_headman(start_date, end_date)[0]['get_count_opened_miniapp_headman']


def write_count_opened_current_lesson_headman(start_date, end_date):
    return get_count_opened_current_lesson_headman(start_date, end_date)[0]['get_count_opened_current_lesson_headman']


def write_count_saved_attendance_headman(start_date, end_date):
    return get_count_saved_attendance_headman(start_date, end_date)[0]['get_count_saved_attendance_headman']


def draw_count_opened_miniapp_every_day(start_date, end_date):
    data = get_count_opened_miniapp_every_day(start_date, end_date)
    graph_html = draw_histogram(
        data,
        'Гистограмма количества старост, открывших miniapp',
        'Дата',
        'Количество открытий',
        5)
    return graph_html


def draw_count_opened_current_lesson_headman_every_day(start_date, end_date):
    data = get_count_opened_current_lesson_headman_every_day(start_date, end_date)
    graph_html = draw_histogram(
        data,
        'Гистограмма количества старост, открывших текущую пару',
        'Дата',
        'Количество открытий',
        5)
    return graph_html


def draw_count_saved_attendance_headman_every_day(start_date, end_date):
    data = get_count_saved_attendance_headman_every_day(start_date, end_date)
    graph_html = draw_histogram(
        data,
        'Гистограмма количества старост, сохранивших посещаемость',
        'Дата',
        'Количество сохранений',
        5)
    return graph_html


@app.route('/', methods=['GET', 'POST'])
def index():
    default_start_date = date(date.today().year, 1, 1).strftime('%Y-%m-%d')
    default_end_date = date.today().strftime('%Y-%m-%d')

    start_date = request.form.get('start_date', default_start_date)
    end_date = request.form.get('end_date', default_end_date)

    text_count_subdued_headman = write_count_subdued_headman()
    text_count_registered_headman = write_count_registered_headman()
    text_count_opened_miniapp_headman = write_count_opened_miniapp_headman(start_date, end_date)
    text_count_opened_current_lesson_headman = write_count_opened_current_lesson_headman(start_date, end_date)
    text_count_saved_attendance_headman = write_count_saved_attendance_headman(start_date, end_date)

    graph_count_opened_miniapp_every_day = draw_count_opened_miniapp_every_day(start_date, end_date)
    graph_count_opened_current_lesson_headman_every_day = draw_count_opened_current_lesson_headman_every_day(
        start_date, end_date)
    graph_count_saved_attendance_headman_every_day = draw_count_saved_attendance_headman_every_day(
        start_date, end_date)

    return render_template(
        'index.html',
        text_count_subdued_headman=text_count_subdued_headman,
        text_count_registered_headman=text_count_registered_headman,
        text_count_opened_miniapp_headman=text_count_opened_miniapp_headman,
        text_count_opened_current_lesson_headman=text_count_opened_current_lesson_headman,
        text_count_saved_attendance_headman=text_count_saved_attendance_headman,
        graph_count_opened_miniapp_every_day=graph_count_opened_miniapp_every_day,
        graph_count_opened_current_lesson_headman_every_day=graph_count_opened_current_lesson_headman_every_day,
        graph_count_saved_attendance_headman_every_day=graph_count_saved_attendance_headman_every_day,
        start_date=start_date,
        end_date=end_date)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
