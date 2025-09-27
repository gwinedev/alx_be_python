def display_current_datetime() :
    import datetime
    current_date = datetime.datetime.now()

    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_date)

def calculate_future_datetime():
    from datetime import timedelta, datetime

    number_of_days = int(input("Enter your number of days: "))
    current_date = datetime.now()

    future_date  = current_date + timedelta(days=number_of_days)
    formatted_date = future_date.strftime("%Y-%m-%d")

    print(formatted_date)

display_current_datetime()
calculate_future_datetime()