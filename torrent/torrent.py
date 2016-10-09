#!/usr/bin/env python3
import os, sys, smtplib, imapclient, pyzmail, subprocess
from twilio.rest import TwilioRestClient

bot_email = "************"
bot_password = "***********"

smtp_server = "***********"
imap_server = "***********"

#Check Bot E-Mail for any new instructions.
imapObj = imapclient.IMAPClient(imap_server, ssl=True)
imapObj.login(bot_email, bot_password)
imapObj.select_folder('INBOX', readonly=False)

UIDs = imapObj.search([u'FROM', u'*************'])
print(UIDs)

rawMessages = imapObj.fetch(UIDs, ['BODY[]', 'FLAGS'])

links = []
torrent_uids = []
for UID in UIDs:
	message = pyzmail.PyzMessage.factory(rawMessages[UID][b'BODY[]'])
	if message.get_subject().lower() == "torrent":
		#print(message.get_subject())
		link = message.text_part.get_payload().decode(message.text_part.charset)
		links.append(link)
		torrent_uids.append(UID)

if len(links) == 0:
	sys.exit()

imapObj.delete_messages(torrent_uids)
imapObj.expunge()

imapObj.logout()

subprocess.Popen(['/usr/bin/deluge'] + links)

smtpObj = smtplib.SMTP(smtp_server, 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(bot_email, bot_password)

smtpObj.sendmail(bot_email, '************', 
	'Subject: Instruction Received. \nI have received the magnet link.\n Deluge has been opened and is currently downloading.\nHave a nice day!')
smtpObj.quit()

accountSID = '******************************'
authToken = '*******************************'

twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = '**********'
myCellPhone = '**********'

message = twilioCli.messages.create(body='Your Instruction has been received. Torrent is downloading. Have a nice day!', 
	from_=myTwilioNumber, to=myCellPhone)
