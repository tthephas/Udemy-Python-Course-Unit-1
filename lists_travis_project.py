# travis project
# working with lists 
# travis is a security robot, checking if names are authorized or not

known_users = ['Josh', 'Lesley', 'Ryan', 'Mya', 'Shari', 'Craig', 'Steve', 'Jackie']


while True:
    print('Hi! My name is Travis')
    name = input('What is your name?: ').strip().capitalize()
    # use the in keyword , check if name is in list of known users

    if name in known_users:
        print('Hello, {}!'.format(name))
        remove = input('Would you like to be removed from the system (y/n)?: ').strip().lower()
        
        if remove == 'y':
            known_users.remove(name)
        elif remove == 'n':
            print('No problem. I didnt want you to leave anyway.')

    else:
        print('{} NOT recognized. Sorry!'.format(name))
        add_me = input('Would you like to be added to the system (y/n)?: ').strip().lower()

        if add_me == 'y':
            known_users.append(name)
        elif add_me == 'n':
            print('No worries, see you around town.')
