vocabulary words = {
	'apple': 'fruit',
	'steak': 'meat',
	'celery': 'vegetable',
	'cat': 'pet'
}

def count_name():
	letter_count = {} # here you are setting an empty dictionary
	name = 'Natasha' # setting the variable
	for char in name: # using the for loop toiterate through each letter in the string. Checking for repeated characters
		if char in letter_count:
			letter_count[char] += 1 # for each repeated character aincrement by 1 to the count
		else:
			letter_count[char] = 1 # else count the character once if letter is mentioned once.

	return letter_count # stores the information

print count_name () # calling the function and displaying data


prices = {'banana': 4, 'apple': 2, 'orange': 1.5, 'pear': 3}
	for item, price in price.items():
		print item
		print price
			if # find the conditional statement to check for the greatest number value.