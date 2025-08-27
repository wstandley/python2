# This is for OOp 2.1 Core Syntax

class AddressBook:
    """
        Class to represent an address book entry.

        Attributes:
            The class attributes include the users first name, last name, birthday, email, address, city, state, zip code, and phone number

        Methods:
            __eq__ Method is used on line 96 to compare two addresses
            __dir__ Method is used on Line 100 to show the letters in my first name
            __str__ Method is used on Line 68 to help lines 91 - 94 print the addresses in an orderly fashion
    """

    def __init__(self, first_name, last_name, birthday, email, street_address, city, state, zip, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.email = email
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone

    # Getters and Setters
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_birthday(self):
        return self.birthday
    def get_email(self):
        return self.email
    def get_street_address(self):
        return self.street_address
    def get_city(self):
        return self.city
    def get_state(self):
        return self.state
    def get_zip(self):
        return self.zip
    def get_phone(self):
        return self.phone
    

    def set_first_name(self, value):
        self.first_name = value
    def set_last_name(self, value):
        self.last_name = value
    def set_birthday(self, value):
        self.birthday = value
    def set_email(self, value):
        self.email = value
    def set_street_address(self, value):
        self.street_address = value
    def set_city(self, value):
        self.city = value
    def set_state(self, value):
        self.state = value
    def set_zip(self, value):
        self.zip = value
    def set_phone(self, value):
        self.phone = value

    # Magic Methods 
    def __str__(self):
        return ("First Name: " + self.first_name + "\nLast Name: " + self.last_name + "\nBirthday: " + self.birthday + "\nEmail: " + self.email + "\nAddress: " + self.street_address + "\nCity: " + self.city + "\nState: " + self.state + f"\nZip Code: {self.zip}" + "\nPhone #: " + self.phone + "\n")
    
    def __eq__(self, other):
        print("Does Will and Jared's zip codes match?")
        return self.zip == other.zip
    
    def __dir__(self):
        return self.first_name
    
# Instances
address1 = AddressBook(first_name = "Will", last_name = "Standley", birthday = "March 13, 2003", email = "wstandley@students.mchenry.edu", street_address = "905 Abbington Dr.", city = "Crystal Lake", state = "Illinois", zip = 60014, phone = "815-575-5909")

address2 = AddressBook(first_name = "Bob", last_name = "Johnson", birthday = "March 18, 2003", email = "bjohnson@students.mchenry.edu", street_address = "111 Street St.", city = "Woodstock", state = "Illinois", zip = 60098, phone = "815-575-5999")

address3 = AddressBook(first_name = "Jared", last_name = "Smith", birthday = "April 15, 2002", email = "jsmith@students.mchenry.edu", street_address = "123 Sesame St.", city = "Crystal Lake", state = "Illinois", zip = 60014, phone = "888-888-8888")

address4 = AddressBook(first_name = "Will", last_name = "Johnson", birthday = "December 2, 2005", email = "wjohnson@students.mchenry.edu", street_address = "11515 US 14", city = "Woodstock", state = "Illinois", zip = 60098, phone = "000-000-0000")

# Printing each address
print(address1)
print(address2)
print(address3)
print(address4)

# __eq__ Method in use
print(address1.__eq__(address3))

#__dir__ Method in use
print("What is Address 1's first name? " + address1.__dir__())