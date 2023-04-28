# From thepythoncode, article "make a password generator.", with some modifications (No Copy+Paste).
from argparse import ArgumentParser
import secrets
import random
import string

parser = ArgumentParser(
    prog='Password Generator.',
    description='Generate a password with preferences.'
)

# Logic for parser
parser.add_argument("-n", "--numbers", default=0, help="Number of digits in the password.", type=int)
parser.add_argument("-l", "--lowercase", default=0, help="Number of lowercase characters in the password.", type=int)
parser.add_argument("-u", "--uppercase", default=0, help="Number of uppercase characters in the password.", type=int)
parser.add_argument("-s", "--special-chars", default=0, help="Number of special characters in the password.", type=int)

parser.add_argument("-t", "--total-length", type=int,
                    help="Total password length. If passed, it will ignore all arguments and generate a random password with specified length.")

parser.add_argument("-a", "--amount", default=1, type=int)
parser.add_argument("-o", "--output-file")

args = parser.parse_args()

# A list with passwords
passwords = []

# Password loop-through
for _ in range(args.amount):
    if args.total_length:
        passwords.append("".join(
            [secrets.choice(string.digits + string.ascii_letters + string.punctuation) \
                for _ in range(args.total_length)]))
    else:
        password = []

# How many numbers the password should contain
        for _ in range(args.numbers):
            password.append(secrets.choice(string.digits))

        for _ in range(args.uppercase):
            password.append(secrets.choice(string.ascii_uppercase))

        for _ in range(args.lowercase):
            password.append(secrets.choice(string.ascii_lowercase))

        for _ in range(args.special_chars):
            password.append(secrets.choice(string.punctuation))
        
        # Randomizes list
        random.shuffle(password)

        # gets the letters of the string up to length argument, then joining them
        password = ''.join(password)

        # appends password to overall list
        passwords.append(password)

if args.output_file:
    with open(args.output_file, 'w') as f:
        f.write('\n'.join(passwords))

print('\n'.join(passwords))