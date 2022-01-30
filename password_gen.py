#!/usr/bin/python
import sys
import argparse
import string
import random

def arg_check(pw_type):
	available_types = ['alpha-numeric', 'multi-char', '']
	if pw_type in available_types:
		return True
	else:
		print(f"{pw_type} is not a valid option. Please choose an available -type from the help list.")
		return False

# this is a silly way to add the various characters
# need to rewrite
def random_char(length, type):
	x = 0
	password = []
	
	while x < (length * 3):
		password.append(random.choice(string.ascii_letters))
		password.append(str(random.randint(0,9)))
		if type == 'multi-char':
			password.append(random.choice(string.punctuation))
		x += 1

	return password

def random_pass(length, type):
	long_pass = random_char(length, type)
	while len(long_pass) > length:
		long_pass.pop()
		random.shuffle(long_pass)

	return ''.join(map(str,long_pass))
	

parser = argparse.ArgumentParser()
parser.add_argument('-length', type=int, required=True, help="this is the help dialogue")
parser.add_argument('-type', type=str, required=False, default='',help="""use the following arguments 
	to build different character passwords: alpha-numeric, multi-char""")
args = parser.parse_args()

if arg_check(args.type):
	print(random_pass(args.length, args.type))
else:
	print('closing script')
