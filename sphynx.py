#!/usr/bin/python3

import random
import os

print('\nWelcome to the SPHYNX v0.2\n')
print("Cypher a text file with some seed (AKA password) and uncypher it later using the same seed. If the seeds don't coincide, the file would not be decoded correctly.\n")
answer = input('What do you want to do, cypher[c] or decode[d]? ')



# CYPHER:

if answer == 'c':
	# open the file and save the text as a string:
	while True:
		try:
			filename = input('Enter filename (with file extension): ')
			with open(filename, 'r') as file:
				text = file.read()
			break
		except FileNotFoundError:
			print("Sorry, the filename you entered couldn't be found.")
	text = list(text)
	print('Text obtained succesfully.')
	length = len(text)

	# generate an array of positions not used:
	unused_positions = [i for i in range(len(text))]

	# generate empty scrambled array, to join it later:
	scrambled = []

	# set the seed:
	seed = input('Enter seed//password: ')
	random.seed(seed)
	print('Seed//password set to {}'.format(seed))

	print('Cyphering...')
	for i in range(length):
		# get a position from the unused positions list:
		position = random.choice(unused_positions)
		# and remove it to not get it repeated:
		unused_positions.remove(position)
		# add it to the scrambled text:
		scrambled.append(text[position])

	# save content as a .scr file:
	with open(filename + '.sph', 'w') as file:
		file.write(''.join(scrambled))
	print('Scrambled text saved succesfully.')

	delete_ans = input('Would you like to delete the original file? [Y/n] ')
	if delete_ans == 'Y':
		os.remove(filename)
		print('File removed succesfully.')

# DECODE:

if answer == 'd': 
	# open the file and save the text as a string:
	while True:
		try:
			filename = input('Enter filename (with file extension): ')
			with open(filename, 'r') as file:
				text = file.read()
			break
		except FileNotFoundError:
			print("Sorry, the filename you entered couldn't be found.")
	text = list(text)
	print('Cyphered text obtained succesfully.')
	length = len(text)

	# generate an array of positions not used:
	unused_positions = [i for i in range(len(text))]

	# generate empty scrambled array, to join it later:
	unscrambled = ['' for i in range(length)]

	# set the seed:
	seed = input('Enter seed//password: ')
	random.seed(seed)
	print('Seed//password set to {}'.format(seed))

	print('Decoding...')
	for i in range(length):
		# get a position from the unused positions list:
		position = random.choice(unused_positions)
		# and remove it to not get it repeated:
		unused_positions.remove(position)
		# insert in position the text from the scrambled one:
		unscrambled[position] = text[i]
	print('File decoded succesfully.')

	save_decoded_ans = input('Would you like to save the decoded text as a file? [Y/n] ')
	if save_decoded_ans == 'Y':
		filename_decoded = filename[:-4]
		with open(filename_decoded, 'w') as file:
			file.write(''.join(unscrambled))
		print('File saved succesfully.')
		delete_decoded_ans = input('Would you like to delete the cyphered file? [Y/n] ')
		if delete_decoded_ans == 'Y':
			os.remove(filename)
			print('Cyphered file removed succesfully.')
	else:
		print('The uncyphered text reads as follows:')
		print(''.join(unscrambled))

print('Thank you for using SPHYNX v0.2')

##############
# references #
##############

# empty_array = ['' for i in range(5)]

# random.randint(int1, int2) returns a number between 

# separate the text in paragraphs:
# blocks = text.split('\n')
# # and delete empty elements:
# blocks = [block for block in blocks if block] # list comprehension

'''
# generate empty array same length as text
scrambled = ['' for i in range(length)]
# and an array to save used positions and check to not repeat
used_positions = []

for i in range(length):
	repeat = True
	while repeat == True:
		position = random.randint(0, length)
		print('')
		if position not in used_positions: # check if it's used
			repeat == False # if not, break the loop
	used_positions.append(position) # add the position to our list
	scrambled[i] = text[position]
'''
'''
# generate an empty dictionary with keys as positions:
scrambled_dict = {i:'' for i in range(length)}

for i in range(length):
	position = random.randint(0, len(scrambled_dict.keys()))
	scrambled_dict[position] = text[i]
'''