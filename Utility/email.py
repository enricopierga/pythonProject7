import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class email():
    def __init__(self):
        pass


    def emailScadenzaAbbonamento(self, email, nome, cognome):
        self.senderEmail = "centrosportivofake@gmail.com"
        self.server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        self.server.login(self.senderEmail, "Centro123")
        recEmail = email
        message = MIMEMultipart("alternative")
        message["Subject"] = "Prenotazione avvenuta con successo"
        message["From"] = self.senderEmail
        message["To"] = recEmail

        text = f"""\
           Caro {nome} {cognome},
           Il suo abbonamento sta per scadere, si ricordi di rinnovarlo!
           """
        part = MIMEText(text, "plain")
        message.attach(part)
        self.server.sendmail(self.senderEmail, recEmail, message.as_string())

    def emailPrenotazioneAvvenuta(self, email, nome, cognome, data, ora, campo):
        self.senderEmail = "centrosportivofake@gmail.com"
        self.server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        self.server.login(self.senderEmail, "Centro123")
        recEmail = email
        message = MIMEMultipart("alternative")
        message["Subject"] = "Prenotazione avvenuta con successo"
        message["From"] = self.senderEmail
        message["To"] = recEmail

        text = f"""\
Caro {nome} {cognome},
La sua prenotazione per il campo: {campo} in data: {data} alle ore: {ora} è avvenuta 
con successo!
Buona giornata da tutto lo staff del Centro Sportivo!
                """
        part = MIMEText(text, "plain")
        message.attach(part)
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(self.senderEmail, "Centro123")
        server.sendmail(self.senderEmail, recEmail, message.as_string())


    def emailPrenotazioneCancellata(self, email, nome, cognome, data, ora, campo):
        self.senderEmail = "centrosportivofake@gmail.com"
        self.server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        self.server.login(self.senderEmail, "Centro123")
        recEmail = email
        message = MIMEMultipart("alternative")
        message["Subject"] = "Prenotazione eliminata con successo"
        message["From"] = self.senderEmail
        message["To"] = recEmail

        text = f"""\
Caro {nome} {cognome},
La sua prenotazione per il campo: {campo} in data: {data} 
alle ore: {ora} è stata cancellata.
Buona giornata da tutto lo staff del Centro Sportivo!
                """
        part = MIMEText(text, "plain")
        message.attach(part)
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(self.senderEmail, "Centro123")
        server.sendmail(self.senderEmail, recEmail, message.as_string())



