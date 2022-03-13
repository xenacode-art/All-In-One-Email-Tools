# Python code to auto delete mails from my gmail account.
import imaplib
import email
from email.header import decode_header

# Input account details 
username = input("Enter Your Mail Address: ")
password  = input("Input Password: ")

# Creating an IMP4 for connection via ssl

imap = imaplib.IMAP4_SSL("imap.gmail.com")
# Authentication
imap.login(username , password)
# Select mail box you want to delete
# if you want to delete Spam, use 
# imap.select("SPAM")
#imap.list()
# search for specific mails by sender
status, messages = imap.search(None, 'FROM "googlealerts-noreply@google.com"')
imap.select("INBOX")

# search for specific mails to delete
status, messages = imap.search(None, 'FROM "googlealerts-noreply@google.com"') 
status, messages = imap.search(None, 'FROM "ALL"') 
