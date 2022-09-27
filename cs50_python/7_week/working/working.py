import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if matches:
        # Separate groups into a list
        parts = matches.groups()
        if int(parts[1]) > 12 or int(parts[5]) > 12:
            raise ValueError
        # Convert first half of time in correct 24-hours format
        first_part = convert_time(parts[1], parts[2], parts[3])

        # Convert second half of time in correct 24-hours format
        second_part = convert_time(parts[5], parts[6], parts[7])

        # Return result
        return first_part + " to " + second_part
    else:
        raise ValueError

# Funct for convert time to 24-hours format
def convert_time(hour, minutes, AM_PM):
    if AM_PM == 'PM':
        if int(hour) == 12:
            hour = 12
        else:
            hour = int(hour) + 12
    else:
        if int(hour) == 12:
            hour = 0
        else:
            hour = int(hour)
    if minutes == None:
        time = f"{hour:02}" + ":00"
    else:
        time = f"{hour:02}" + ":" + minutes
    return time


if __name__ == "__main__":
    main()