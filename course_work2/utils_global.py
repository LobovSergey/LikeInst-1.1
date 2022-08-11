import json
import logging

from flask import render_template


def get_posts_all():
    try:
        with open('static/data/data.json', 'r', encoding='utf-8') as f:
            return json.load(f)

    except FileNotFoundError:
        return abort_500()


def logger():
    my_logger = logging.getLogger()
    my_logger.setLevel('INFO')

    format_for_file = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler("logs/api.log", 'w')
    file_handler.setFormatter(format_for_file)

    my_logger.addHandler(console_handler)
    my_logger.addHandler(file_handler)


def abort_404():
    return render_template('404.html'), 404


def abort_500():
    return render_template('500.html'), 500
