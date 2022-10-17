# Import modules
from sys import argv
from sys import exit
import requests

# Check for argv value
if len(argv) == 2:
    try:
        btc = float(argv[1])
    except:
        print("Command-line argument is not a number")
        exit(1)
else:
    print("Missing command-line argument")
    exit(1)

# Try convert argv value to float
while True:
    try:
        btc = float(argv[1])
        break
    except:
        print("Command-line argument is not a number")
        exit(1)

# Try calculate result and print out it
try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data_btc = r.json()
    result = data_btc["bpi"]["USD"]["rate_float"] * btc
    print(f"${result:,.4f}")

except requests.RequestException:
    print("RequestException")
    sys.exit(1)