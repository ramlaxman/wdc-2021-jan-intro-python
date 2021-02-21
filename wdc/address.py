people = []
filename = 'people.data'

while True:
    print(people)
    user_choice = input('Enter command: ').strip()

    if user_choice == 'q':
        break

    elif user_choice == 'a':
        # first_name = input('Enter first name: ').strip()
        # last_name = input('Enter last name: ').strip()
        # phone = input('Enter phone: ').strip()
        # email = input('Enter email: ').strip()
        #
        # new_person = {'first_name': first_name,
        #               'last_name': last_name,
        #               'email': email,
        #               'phone': phone}

        new_person = {}
        for field in ['first_name', 'last_name', 'email', 'phone']:
            new_person[field] = input(f'Enter {field}: ').strip()

        people.append(new_person)

    elif user_choice == 'w':
        with open(filename, 'w') as f:
            for one_person in people:
                f.write('\t'.join(one_person.values()) + '\n')

    elif user_choice == 'r':
        people = []
        with open(filename) as f:
            for one_line in f:
                first_name, last_name, email, phone = one_line.strip().split('\t')
                people.append({'first_name':first_name,
                               'last_name':last_name,
                               'email':email,
                               'phone':phone})

    elif user_choice == 'l':
        for one_person in people:
            print(f'{one_person["last_name"]}, {one_person["first_name"]}')
            print(f'\temail: {one_person["email"]}')
            print(f'\tphone: {one_person["phone"]}')

    elif user_choice == 'f':
        look_for = input('Enter search string: ').strip()
        for one_person in people:
            if (look_for in one_person['first_name'] or
                look_for in one_person['last_name'] or
                look_for in one_person['email']):

                print(f'{one_person["last_name"]}, {one_person["first_name"]}')
                print(f'\temail: {one_person["email"]}')
                print(f'\tphone: {one_person["phone"]}')

    else:
        print(f'{user_choice} is not a valid command.')

# save: first name, last name, email, phone
# list of dicts

# q -- quit.  Exit from the program

# a -- add.  the system asks 4 questions (first name, last name, email, and phone)
#      and adds a new dict with that data to the global list

# l -- list.  show all people in the address book

# f -- find.  ask the user to enter a search string.  Show all entries in which
#      that string is INSIDE of either the first name, or the last name, or
#      email address.

# w -- write.  write to a file, with each person on one line and each field
#      separated with tab characters.

# r -- read.  erase people in our current database, then read from the file.
