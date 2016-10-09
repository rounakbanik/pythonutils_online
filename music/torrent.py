#! python3
import os, sys, twilio, smtplib, imapclient, pyzmail

bot_email = "botrony@gmail.com"
bot_password = "playmistyforme"

my_email = "rounakbanik@gmail.com"

smtp_server = "smtp.gmail.com"
imap_server = "imap.gmail.com"

#Check Bot E-Mail for any new instructions.
imapObj = imapclient.IMAPClient(imap_server, ssl=True)
imapObj.login(bot_email, bot_password)