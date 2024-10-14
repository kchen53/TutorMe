#Load JSON file with pre-existing questions and answers
#Process user input and find the most relevant in JSON file
#If a suitable answer is found then return it otherwise ask the user to teach the bot

import json
import os
from difflib import get_close_matches

#Bot object that specializes in its own subject
class bot:
    def __init__(self, filename, subject, date):
        self.filename = filename
        self.subject = subject
        self.date = date

    #read from JSON file
    def read_json(self):

        with open(self.filename, 'r') as file:
           data:dict = json.load(file)

        print(data)
        
        return data

    #Write to JSON file 
    def write_json(self, bot_knowledge):
        
        with open(self.filename, "w") as file:
            json.dump(bot_knowledge, file, indent=2)
    
    def find_best_answer(user_question, questions):
        matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)

        if matches:
            return matches[0]
        else:
            None

    def get_answer(question, bot_knowledge):
        for quest in bot_knowledge["questions"]:
            if quest["question"] == question:
                return quest["answer"]
        
        return None

    # def revision():
    
    # def flashcards():
    
