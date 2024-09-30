from datetime import datetime, timedelta, date

def display_current_datetime():
    current_date = datetime.now()
    formatted = current_date.strftime('%Y-%m-%d %H:%M:%S')
    print(f"Current date and time: {formatted}")

def calculate_future_date (number_of_days):
    current_date = date.today()
    future_date=current_date + timedelta(days=number_of_days)
    future_date = future_date.strftime('%Y-%m-%d')
    print("Future date:", str(future_date))
display_current_datetime()
calculate_future_date(int(input("Enter the number of days to add to the current date: ")))
