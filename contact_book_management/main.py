# Contact Book Management System
# note : try except implemented in add_contact.py

import load_data as ld
import user_interaction as ui


print("Welcome to Contact Book Management System")
contacts = []
ld.load_data_from_database(contacts)
ui.option_selection(contacts)
