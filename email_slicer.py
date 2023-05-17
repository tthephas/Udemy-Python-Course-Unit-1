# get user email address
email = input('what is your email address?: ').strip()

# slice out user name
user = email[:email.index('@')]
user

# slice domain name

domain = email[email.index('@') + 1:]
domain

# format the message

output = 'Your username is {} and your domain is {}'.format(user,domain)

# display the output message

output
 