import contact

class Contact_List():
    def __init__(self):
        self.contacts = []
        self.contact = []
    def new_contact(self, name, email, phone):
        new = contact.Contact()
        new.new_name(name)
        self.contact.append(new.name)
        new.new_email(email)
        self.contact.append(new.email)
        new.new_telephone(phone)
        self.contact.append(new.telephone)
        self.contacts.append(self.contact)

    def display_contacts(self):
        print(self.contacts)

def main():
    abc = Contact_List()
    abc.new_contact('John Brown', 'brown@onet.pl', '555234000')
    abc.new_contact('Anna May', 'am@o2.pl', '232000199')
    abc.display_contacts()

if __name__ =="__main__":
   main()