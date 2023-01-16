import os
from datetime import datetime


def get_day_week(val):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[val]


def create_salutation(salutation):
    def salute(user):
        now = datetime.now()
        date_now = now.date().strftime("%Y/%m/%d")
        day_now = now.date().weekday()
        day_week = get_day_week(day_now)

        return f"> {salutation}, {user}. Today is {day_week}, {date_now}"

    return salute


user = os.environ["USERNAME"]
hour_system = datetime.now().hour

good_morning = create_salutation("Good Morning")
good_afternoon = create_salutation("Good Afternoon")
good_night = create_salutation("Good Night")


if hour_system < 12:
    print(good_morning(user))
elif hour_system < 18:
    print(good_afternoon(user))
elif hour_system < 23:
    print(good_night(user))
