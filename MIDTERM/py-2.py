from datetime import datetime

date_input = input("Enter the date (mm/dd/yyyy): ")
try:
    date_obj = datetime.strptime(date_input, "%m/%d/%Y")
except ValueError:
    print("Invalid date format. Please enter in mm/dd/yyyy format.")
else:
    month_name = date_obj.strftime("%B")
    day = date_obj.day
    year = date_obj.year
    print(f"Date Output: {month_name} {day}, {year}")