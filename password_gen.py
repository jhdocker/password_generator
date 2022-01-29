#!/usr/bin/python
import sys
import argparse
import string
import random

def random_char(length):
	x = 0
	password = []
	while x < (length * 3):
		password.append(random.choice(string.ascii_letters))
		password.append(random.choice(string.ascii_letters).upper())
		password.append(str(random.randint(0,9)))
		x += 1

	return password


def random_pass(length):
	long_pass = random_char(length)
	while len(long_pass) > length:
		long_pass.pop()
		random.shuffle(long_pass)

	return ''.join(map(str,long_pass))
	

parser = argparse.ArgumentParser()
parser.add_argument('-length', type=int, required=True, help="this is the help dialogue")
args = parser.parse_args()

if args.length:
	pass_len = args.length

print(random_pass(args.length))

