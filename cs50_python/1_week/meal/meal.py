def main():
    time = input("What time is it? ")
    convert(time)

def convert(time):
    hours, minutes = time.split(":")
    if hours == '7' or hours == '8':
        print("breakfast time")
    elif hours == '12' or hours == '13':
        print("lunch time")
    elif hours == '18' or hours == '19':
        print("dinner time")

if __name__ == "__main__":
    main()