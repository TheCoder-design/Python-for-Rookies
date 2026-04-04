import csv
# Creation of functions that will let users access the contact book


def add_contact(name, email, phone):
    with open("contacts.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, email, phone])

    print(f"Contact for {name} added Successfully")


def view_contacts():
    with open("contacts.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def search_contact():
    with open("contacts.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if name.lower() in row[0].lower():
                print(row)
                return
        print("Contact not found")


# Let's Build the Interface menu for the user
while True:
    print("=== Contact Book ===")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your Choice: ")

    if choice == "1":
        name = input("Enter the name: ")
        email = input("Enter the email address: ")
        phone = input("Enter the phone number: ")
        add_contact(name, email, phone)

    elif choice == "2":
        view_contacts()
    elif choice == "3":
        name = input("Enter the name to search: ")
        search_contact()
    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("Invalid Choice. Try again")
