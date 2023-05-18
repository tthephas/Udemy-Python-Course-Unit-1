# travis project
# working with lists 
# travis is a security robot, checking if names are authorized or not

known_users = ['Josh', 'Lesley', 'Ryan', 'Mya', 'Shari', 'Craig', 'Steve', 'Jackie']

print(len(known_users))

while True:
    print('Hi! My name is Travis')
    name = input('What is your name?: ').strip().capitalize()
    # use the in keyword , check if name is in list of known users

    if name in known_users:
        print('Hello, {}!'.format(name))
        remove = input('Would you like to be removed from the system (y/n)?: ').lower()
        
        if remove == 'y':
            known_users.remove(name)

    else:
        print('{} NOT recognized. Sorry!')
