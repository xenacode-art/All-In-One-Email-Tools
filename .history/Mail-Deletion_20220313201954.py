# Python code to auto delete mails from my gmail account.
import imaplib
import email
from email.header import decode_header

# Input account details 
username = input("Enter Your Mail Address: ")
password  = input("Input Password")

# Creating an IMP4 for connection via ssl

imp4 = imaplib.IMAP4_SSL()