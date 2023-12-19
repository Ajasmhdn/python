from datetime import datetime

def is_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def calculate_days(age):
    num_age = int(age)
    current_year = int(datetime.now().year)
    year_left = 90 - num_age
    total_days_left = 0

    for year in range(current_year, current_year + year_left):
        if is_leap(year):
            total_days_left += 366
        else:
            total_days_left += 365

    return total_days_left

age = input("Enter your age : ")
num_age = int(age)
days_left = calculate_days(age)
year_left = 90 - num_age
months_left = year_left * 12
weeks_left = year_left * 53

print(f"The days left{days_left}. The weeks left {weeks_left}. the months left {months_left}")