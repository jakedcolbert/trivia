#!/usr/bin/env python
#
#


################ TO RUN: 'python3 trivia.py' in terminal ################


import json
import requests
import random

# ANSI codes

RED = "\033[0;31m" # RED
GREEN = "\033[0;32m" # GREEN
YELLOW = "\033[1;33m" # YELLOW
END = "\033[0m" # RESET to reqular terminal color
CR = "\x0D" # Carrige Return
CLEAR = "\033[H\033[J" # Clear the terminal window

# Global limit constant

LIMIT = 20

# Get the longest string in an array for finding the url equivelants of categories

def getLongestStrings(categories):
	dict = {}
	for subject in categories:
		dict[subject] = ""
		for category in categories[subject]:
			if (len(category) > len(dict[subject])):
				dict.update({subject: category})
	return dict
		
# Get the trivia categories from the API

def getCategories():
	url = "https://the-trivia-api.com/api/categories"
	r = requests.get(url)
	result = json.loads(r.text)
	return result
	
def getSubjects(apiCategories):
	categories = []
	for category in apiCategories:
		categories.append(category)
	return categories
		
# Get the trivia questions from the API

def getTrivia(category, difficulty):
	url = "https://the-trivia-api.com/api/questions?categories=" + category + "&limit=" + str(LIMIT) + "&difficulty=" + difficulty
	r = requests.get(url)
	result = json.loads(r.text)
	return result
	
# Main method that generates terminal UI to ask the trivia questions
	
if __name__ == "__main__":
	print(CLEAR)

	correct = 0;

	print(YELLOW + "Time for trivia!!\n" + END)
	
	categories = getCategories()
	subjects = getSubjects(categories)

	for i in range(0, len(subjects)):
		print(str(i + 1) + ") " + subjects[i])

	while(True):
		subject = int(input("\nSelect a category...\n")) - 1
		if subject in range(0, len(subjects)):
			break
		else:
			print("\n" + RED + "Please choose a number for one of the categories above" + END + "\n")

	print(CLEAR)
	
	print(YELLOW + "Time for trivia!!\n" + END)
	print("1) Easy")
	print("2) Medium")
	print("3) Hard")
	
	while(True):
		difficulty = input("\nChoose a difficulty...\n")
		
		if difficulty == "1":
			difficulty = "easy"
		if difficulty == "2":
			difficulty = "medium"
		if difficulty == "3":
			difficulty = "hard"
			
		if difficulty in ["easy", "medium", "hard"]:
			break
		else:
			print("\n" + RED + "Please choose a number for one of the difficulties above" + END + "\n")
	
	print(CLEAR)

	questions = getTrivia(getLongestStrings(categories)[subjects[subject]], difficulty)
	for question in questions:
		answers = []

		print(YELLOW + question["category"] + " on " + question["difficulty"] + " difficulty.\n" + END)
		print("Question: " + question["question"] + "\n")

		answers = question["incorrectAnswers"]
		answers.append(question["correctAnswer"])
		random.shuffle(answers)

		print("1) " + answers[0])
		print("2) " + answers[1])
		print("3) " + answers[2])
		print("4) " + answers[3])
		print("\n")

		while(True):
			choice = input("Choose one of the answers: 1, 2, 3, or 4...\n")
			if choice in ["1", "2", "3", "4"]:
				break;
			else:
				print("\n" + RED + "Please choose a number for one of the answers above" + END + "\n")

		if (answers[int(choice) - 1] == question["correctAnswer"]):
			correct += 1
			print(GREEN + "\nThat's correct! Nice job!\n" + END)
		else:
			print(RED + "\nThe correct answer was " + question["correctAnswer"] + "\n" + END)

		input("Press enter to continue...")
		print(CLEAR)
	print(CLEAR)
	print(YELLOW + "\nYou got " + str(correct) + " out of " + str(len(questions)) + " correct!\n" + END)
		
		
		
		
		
	

