import smtplib as smtp, ssl, os

def send_email(message):
    PORT: int = 465
    SMTP_SERVER: str = "smtp.gmail.com"
    TO: str = "alexander.levinson.70@gmail.com" 
    PASSWORD: str = os.getenv("DAY22_PWD")

    context = ssl.create_default_context()
    with smtp.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
        server.login(TO, PASSWORD)
        
        server.sendmail(TO, TO, message)
        
if __name__ == "__main__":
    send_email("Hello, this is a test email from Python!")