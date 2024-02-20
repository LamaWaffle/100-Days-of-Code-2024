weekdays = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7,
}

print(weekdays["Wednesday"])

weekdays["Sunday"] = 0
print(weekdays)

weekdays.pop("Sunday")
print(weekdays)

for day in weekdays:
    print(day)

for day in weekdays:
    print(f"The day of the week is {day}, and the number of days is {weekdays[day]}")


for day in weekdays:
    if day == weekdays:
        print("This day is correct.")
    else:
        print("This day is not correct.")

print(len(weekdays))

suspect_number_one = {
    "Name": "Jimmy",
    "Age": 17,
    "Address": {
        "Street": "Evergreen Terrace",
        "City": "Springfield",
        "Country": "United States of America",
    },
    "Criminal": False,
}

print(suspect_number_one["Address"]["Country"])




usernames = {
    "Username": {
        "First Name": "Matthew",
        "Last Name": "Eberhard",
        "Number": '0401188306',
    },
    "Enabled": True          
}


