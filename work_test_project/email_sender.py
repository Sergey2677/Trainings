import smtplib
import os
from email.mime.text import MIMEText
import csv


def transform_template(html_file, csv_row):
    """
    csv_row is a list with split values from csv file
    html_file is template html
    """
    # Open file with html template
    try:
        with open(html_file) as file:
            html_file = file.read()
    except IOError:
        raise EOFError("The template file doesn't exist!")

    # Loop through list of csv_row and split each element into with separate sign '|'
    for i in csv_row:
        try:
            # You can choose any separate sign, this is up to you, but don`t forget check with csv file
            var = i.split("|")  # type: list
            # Replace template with value
            if var[0] in html_file and len(var) == 2:
                html_file = html_file.replace(var[0], var[1])
        except:
            pass

    # return finished html template
    return html_file


def establish_connection(account):
    # First two elements from tuple is address of SMTP server and its port
    server = smtplib.SMTP(*account[:2])
    server.starttls()
    try:
        # Remaining elements of tuple is password and login
        server.login(*account[2:])
        print "Connection has been established!"
    except Exception as _ex:
        raise ValueError("Incorrect account! Check your login or password please!")
    # return server with established connection
    return server


def send_email(account, html_template, followers):
    print "Sending ...."
    # Establish connection with a server
    server = establish_connection(account)
    # Open a csv file with followers, loop through and send a message
    try:
        with open(followers) as f:
            # Each row is a data of each follower
            reader = csv.reader(f)
            for row in reader:
                message = MIMEText(transform_template(html_template, row[1:]), "html")
                message["From"] = account[2]
                message["To"] = row[0]
                message["Subject"] = "TEST"
                server.sendmail(account[2], row[0], message.as_string())
                return "Sending is finished"
    except:
        raise EOFError("Sending has been stopped with an error!")


def main():
    account = ('smtp.gmail.com', 587, 'sergeyasdf2677@gmail.com',
               os.getenv("EMAIL_PASSWORD"))  # Using a variable from the virtual environment
    html_template = 'email_template.html'
    followers = 'followers.csv'
    print(send_email(account, html_template, followers))


if __name__ == "__main__":
    main()
