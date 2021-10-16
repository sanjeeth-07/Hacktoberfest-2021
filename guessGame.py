import random
name = input("What is your name? ")
print("Good Luck ! ", name)
words = ['rainbow', 'computer', 'science', 'programming',
		'python', 'mathematics', 'player', 'condition',
		'reverse', 'water', 'board', 'geeks']
word = random.choice(words)
print("Guess the characters in the words...>>>>>>")
guesses = ''
turns = 5
while turns > 0:
	failed = 0
	for char in word:
		if char in guesses:
			print(char)	
		else:
			print("_")
			failed += 1
			

	if failed == 0:
	
		print("You always Win....>>>>>")
		print("The word is this >>>>>> ", word)
		break
	
	guess = input("guess a character:")
	
	guesses += guess
	if guess not in word:
		
		turns -= 1
	
		print("Wrong Guess dude...")
		print("You have....", + turns, 'more guesses mate!')
		
		if turns == 0:
			print("You Loose")
