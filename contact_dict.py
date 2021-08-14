

contacts = {
    "contact1" : {
        "name" : "Derek",
"phone number" : "7608452921",
         "age" : "29"
    },
    "contact2" : {
        "name" : "Bob",
"phone number" : None,
         "age" : "42"
    },
    "contact3" : {
        "name" : "Joe",
"phone number" : "4206980085",
         "age" : "69"
    },
}

#print("You have " + str(len(contacts)) + " contacts.")

#manually add a new contact
contacts["contact4"] = {
    "name" : "Ron",
    "phone number": "8008556969",
    "age": "21"
}


#create a function to print each contact out one by one
def contact_printer():
    for contact_num, contact_info in contacts.items():
        print(contact_num, contact_info)

#creates a new dictionary of inputs (name, phone, age)
#updates old nested dictionary with new contact
def add_contact():
    contact_num = "contact" + str(len(contacts) + 1)
    contacts[str(contact_num)] = {
        "name" : input("name? "),
        "phone number" : input("phone number? "),
        "age" : input("age? ") 
    }
    print("Now you have " + str(len(contacts)) + " contacts.")

def main():
    contact_printer()
    add_contact()

main()