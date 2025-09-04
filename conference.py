"""
    This is for assignment: OOP 2.3 Extended Function Argument Syntax
"""

def conference_signup(*participant_names, **contact_details):
    """
        This function takes the contacts name, email, and phone number and neatly lists it out
    """
    i = 0 # starts a counter to organize the list
    print("Here is the people who have signed-up: ")

    for names in participant_names: # Start Loop
            
            contacts = sorted(contact_details.items()) # Keeps the contact_details list organized
            phone, email = contacts[i] # Helps itterate through contact_details in orderly fashion

            print(f"\nName: {names}")
    # for phone, email in contact_details.items():
            print(f"Email: {email}\nPhone Number: {phone}")
            i+1 # Allows for movement to next list item

participant_names = ("Will", "Camren", "Ben")
contact_details = {"815-575-5909": "wstandley@students.mchenry.edu", "815-575-5900": "camren@students.mchenry.edu", "815-575-5908": "ben@students.mchenry.edu"}

conference_signup(*participant_names, **contact_details)