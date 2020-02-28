#!/usr/bin/env python3.8	

def endsPy(input):
	input = input[len(input)-2:]
	input = input.lower()
	
	if input ==  'py':
		print('True')
		return True
	else:
		print('False')
		return False
	
