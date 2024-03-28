import smtplib

my_email = "itzkumaranshuman@gmail.com"
password = "put your app password here"
receivers_email = "annylive007@gmail.com"
def email_client():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
        # connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=receivers_email, msg="Subject:Hello\n\nGood morning!")
email_client()