from datetime import datetime

current_date = datetime.now()


def display_current_datetime():
    print('Current date and time:', current_date)

future_days = int(prompt("Enter the number of days to add to the current date:"))

def calculate_future_date():
    number_of_days = int(prompt("Enter the number of days to add to the current date:"))
    future_date = current_date + timedelta(days=number_of_days)
    print("Future date:",future_date)