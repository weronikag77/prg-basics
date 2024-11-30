#The file email.txt contains a raw email. Write a program that uses regular expressions to fetch and print:

#For each of the above commands, define a separate function (see below) 
# that returns the value read from the email. Place the functions in a separate module called emails.

#email_sender()
#email_recipient()
#email_subject()
#email_body()

def email_sender(email_file):
    with open(email_file) as file:
        for line in file:
            if "From:" in line:
                return line
            
def email_recipient(email_file):
    with open(email_file) as file:
        for line in file:
            if "To:" in line:
                return line
email = "email.txt"
print(email_sender(email))
print(email_recipient(email))