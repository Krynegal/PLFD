from datetime import date, timedelta

today = date(1900, 1, 1)

while today.year != 2000:
    today += timedelta(days=1)
    if today.day * today.month == today.year % 100:
        print(today, " is magic date")
