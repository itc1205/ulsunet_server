from flask import Flask

from data import db_session
from data.users import User
from data.schedules import Schedule
from data.group import Group

def parse(parsed_string: str) -> list:
    return parsed_string.split(';')

def first_use():
    
    group = Group()
    group.course = 1
    group.group_name = "ПРИ"
    group.year = 2022
    
    user = User()
    user.name = "Иван"
    user.surname = "Иванов"
    user.profile_image = "assets/image.png"
    user.group = group # Многие к одному

    schedule = Schedule()
    schedule.lections = "ЭВМ;Мат анализ"
    schedule.places = "303;203"
    schedule.group = group # Одно к одному


app = Flask(__name__)


def main():
    db_session.global_init("main.db")
    app.run()


if __name__ == "__main__":
    main()



