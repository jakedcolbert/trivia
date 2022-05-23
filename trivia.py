#!/usr/bin/env python
#
#


################ TO RUN: 'python3 test.py' in terminal ################


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

# Get the trivia questions from the API

def getTrivia():
	url = "https://the-trivia-api.com/api/questions?limit=" + str(LIMIT)
	r = requests.get(url)
	result = json.loads(r.text)
	return result
	
# Main method that generates terminal UI to ask the trivia questions
	
if __name__ == "__main__":
	print(CLEAR)
	
	correct = 0;
	
	print(YELLOW + "Time for trivia!!\n" + END)
	for question in getTrivia():
		answers = []
		
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
	print(YELLOW + "\nYou got " + str(correct) + " out of " + str(LIMIT) + " correct!\n" + END)
		
		
		
		
		
	

