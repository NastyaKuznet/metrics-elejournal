import re
from datetime import datetime, timedelta
import plotly.graph_objects as go
from plotly.offline import plot


def draw_histogram(data, title, x_title, y_title, max_y=None):
    """
    Generates an HTML histogram from the input data.

    Args:
        data: A list of dictionaries, where each dictionary contains a single key-value pair.
              The value should be a string containing a date and a number within parentheses,
              e.g., "('2023-10-26',123)".
        title: The title of the histogram.
        x_title: The title of the x-axis.
        y_title: The title of the y-axis.
        max_y: (Optional) The maximum value for the y-axis. Must be an integer if provided.

    Returns:
        An HTML string representing the histogram.
    """

    dates = []
    values = []

    for el in data:
        for i, item in el.items():
            match = re.search(r'\((\d{4}-\d{2}-\d{2}),(\d+)\)', item)
            if match:
                dat = match.group(1)
                number = int(match.group(2))
                dates.append(dat)
                values.append(number)
            else:
                print(f"Предупреждение: Не удалось извлечь дату и число из значения: {item}")

    if not dates:  # Проверка, пуст ли список дат
        print("Предупреждение: Данные не извлечены. Возвращается пустой график.")
        # Возвращаем базовый график или сообщение об отсутствии данных
        fig = go.Figure()  # Создаем пустую фигуру
        fig.update_layout(
            title=title,
            xaxis_title=x_title,
            yaxis_title=y_title
        )
        graph_html = plot(fig, output_type='div', include_plotlyjs=False)
        return graph_html

    # Находим начальную и конечную даты
    start_date = min(dates)
    end_date = max(dates)

    # Создаем список всех дат в диапазоне
    all_dates = []
    current_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_dt = datetime.strptime(end_date, '%Y-%m-%d')
    while current_date <= end_date_dt:
        all_dates.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)

    # Создаем словарь для хранения значений для каждой даты, по умолчанию 0
    date_values = {date: 0 for date in all_dates}

    # Заполняем словарь фактическими значениями из данных
    for i in range(len(dates)):
        date_values[dates[i]] = values[i]

    # Разделяем даты и значения для построения графика
    plot_dates = list(date_values.keys())
    plot_values = list(date_values.values())

    fig = go.Figure(data=[go.Bar(x=plot_dates, y=plot_values)])

    layout = dict(
        title=title,
        xaxis_title=x_title,
        yaxis_title=y_title,
        bargap=0.2,
        xaxis=dict(
            type='category',
            dtick='D1',
            tickangle=0
        )
    )

    # Добавляем ограничение по y-оси, если оно задано
    if max_y is not None:
        if not isinstance(max_y, int):
            raise ValueError("max_y must be an integer.")
        layout['yaxis'] = dict(range=[0, max_y])

    fig.update_layout(layout)

    graph_html = plot(fig, output_type='div', include_plotlyjs=False)
    return graph_html
