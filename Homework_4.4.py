def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if args[0] in contacts.keys():
        add_contact(args, contacts)
    else:
        print (f"Not changet, no user {args[0]}")

def show_phone(args, contacts):
        name = args[0]
        return contacts[name] if name in contacts.keys() else "No such user"
  
def show_all(args, contacts):
    s=''
    for key in contacts:
        s+=(f"{key:10} : {contacts[key]:10}\n")
    return s

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "show":
            print(show_phone(args,contacts))
        elif command == "all":
            print(show_all(args,contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()