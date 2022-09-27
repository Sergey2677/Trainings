
# Declare list with months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# The loop until input will be right
while True:
    date = input("Date: ")
    # Only works if input has got sign ',' or '/'
    if (('/' in date) or (',' in date)):
        try:
            # Delete all whitespaces
            date = date.strip()
            # Try split with separate sign '/'
            month, day, year = date.split('/')
            # Check value of month and day
            if (int(month) <= 12 and int(month) >= 1) and (int(day) <= 31 and int(day) >= 1):
                break
        except:
            try:
                # Split with separate whitespace
                month, day, year = date.split()
                # Check is month inside months
                for i in range(len(months)):
                    if month == months[i]:
                        month = i + 1
                # Replace comma sign
                day = day.replace(',', '')
                # Check value of month and day
                if (int(month) <= 12 and int(month) >= 1) and (int(day) <= 31 and int(day) >= 1):
                    break
            except:
                print()
                pass
    # Loop again if inside input no sign '/' or ','
    else:
        continue

# Print out result if all good
print(f"{year}-{int(month):02}-{int(day):02}")
