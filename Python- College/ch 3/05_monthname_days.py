month = input("Enter a month name: ").lower()
days_in_month = {"january": 31, "february": 28, "march": 31, "april": 30, "may": 31,
    "june": 30, "july": 31, "august": 31, "september": 30,
    "october": 31, "november": 30, "december": 31}
print(f"{month.capitalize()} has {days_in_month.get(month, 'Invalid month')} days.")
