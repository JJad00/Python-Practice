import os
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Keep email.dat in the same folder as this script.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(SCRIPT_DIR, 'email.dat')


def main():
    """Load the emails, run the menu loop, and save after each change."""
    emails = load_emails()
    choice = get_user_choice()

    while choice != QUIT:
        if choice == LOOK_UP:
            look_up(emails)
        elif choice == ADD:
            if add(emails):
                save_emails(emails)
        elif choice == CHANGE:
            if change(emails):
                save_emails(emails)
        elif choice == DELETE:
            if delete(emails):
                save_emails(emails)

        choice = get_user_choice()


def load_emails():
    """Load the saved emails or return an empty dictionary."""
    try:
        with open(FILENAME, 'rb') as email_file:
            emails = pickle.load(email_file)
    except FileNotFoundError:
        emails = {}
    except EOFError:
        emails = {}

    return emails


def get_user_choice():
    """Display the menu and return a validated choice."""
    print()
    print('Menu')
    print('----------------------------------------')
    print('1. Look up an email address')
    print('2. Add a new name and email address')
    print('3. Change an existing email address')
    print('4. Delete a name and email address')
    print('5. Quit the program')
    print()

    choice = input('Enter your choice: ')
    valid_choices = (str(LOOK_UP), str(ADD), str(CHANGE), str(DELETE), str(QUIT))

    while choice not in valid_choices:
        print('Please enter a number from 1 to 5.')
        choice = input('Enter your choice: ')

    return int(choice)


def look_up(emails):
    """Print the email address for a name, if found."""
    name = input('Enter a name: ')

    if name in emails:
        print(emails[name])
    else:
        print('The specified name was not found.')


def add(emails):
    """Add a new entry and return whether the dictionary changed."""
    name = input('Enter name: ')

    if name in emails:
        print('That name already exists.')
        return False

    address = input('Enter email address: ')
    emails[name] = address
    print('Name and address have been added.')
    return True


def change(emails):
    """Update an existing entry and return whether it was found."""
    name = input('Enter name: ')

    if name not in emails:
        print('The specified name was not found.')
        return False

    address = input('Enter the new address: ')
    emails[name] = address
    print('Information updated.')
    return True


def delete(emails):
    """Delete an entry and return whether it was found."""
    name = input('Enter name: ')

    if name not in emails:
        print('The specified name was not found.')
        return False

    del emails[name]
    print('Name and address have been deleted.')
    return True


def save_emails(emails):
    """Pickle the emails dictionary to email.dat."""
    with open(FILENAME, 'wb') as email_file:
        pickle.dump(emails, email_file)


if __name__ == '__main__':
    main()