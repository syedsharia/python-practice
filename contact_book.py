def main():
    contact_book = {}
    
    while True:
        print("\n=== Contact Book ===")
        print("1. Add contact")
        print("2. Search contact")
        print("3. List all contacts")
        print("4. Delete contact")
        print("5. Exit")

        
        choice = input("Choose option: ")
        
        if choice == "1":
            name = input("Enter name: ").strip().title()
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_book[name] = {"phone": phone, "email": email}
            print(f"Contact '{name}' added.")
        
        elif choice == "2":
            name = input("Enter name: ").strip().title()
            if name in contact_book:
                details = contact_book[name]
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
            else:
                print(f"Contact '{name}' not found.")
        
        elif choice == "3":
            if not contact_book:
                print("No contacts found.")
            else:
                for name, details in contact_book.items():
                    print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
        
        elif choice == "4":
            name = input("Enter name to delete: ").strip().title()
            if name in contact_book:
                del contact_book[name]
                print(f"Contact '{name}' deleted.")
            else:
                print(f"Contact '{name}' not found.")
        
        elif choice == "5":
            print("Exiting Contact Book. Goodbye!")
            break
        
        else:
            print("Invalid option. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()  

