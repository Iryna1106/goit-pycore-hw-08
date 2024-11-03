from functions.functions_record import *
from addressbook.addressbook import AddressBook
from functions.functions_bday import *
from utils.utils import *
from contacts.record import *
from colorama import Fore, Style


def main():
    book=AddressBook.load_data()
    print("Welcome to an assistant bot!")

    upcoming_bdays = book.get_upcoming_birthdays()
    if upcoming_bdays:
        print("Upcoming Birthdays:\n" + upcoming_bdays)
        print_menu()
    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)
            if command in ["close", "exit"]:
                AddressBook.save_data(book)
                print("See you!")
                break
            elif command == "hello":
                print("What would you like me to do?")
            elif command == "add":
                print(add_contact(args,book))
            elif command == "change":
                print(change_contact(args,book))
            elif command == "phone":
                print(show_phone(args[0], book))
            elif command == "all":
              print(show_all(book))
            elif command == "add-birthday":                
                print(add_birthday(args,book))
            elif command == "show-birthday":
                print(show_birthday(args,book))
            elif command == "birthdays":
               print (birthdays(book))
            elif command == "delete":
                print(delete_contact(args, book)) 
            else:
                print(f"{Fore.RED}Invalid command.{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}An unexpected error occurred: {e}{Style.RESET_ALL}")




if __name__ == "__main__":
    main()