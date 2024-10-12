#Load JSON file with pre-existing questions and answers
#Process user input and find the most relevant in JSON file
#If a suitable answer is found then return it otherwise ask the user to teach the bot

import json
import os

#Bot object that specializes in its own subject
class bot:
    def __init__(self, filename, subject, date):
        self.filename = filename
        self.subject = subject
        self.date = date
        self.data = {}

    #read from JSON file
    def read_json(self):
    #reads json file and converts the data into a python dictionary
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = {}
            
        print(self.data)

    #Write to JSON file 
    def write_json(self, new_data):

        self.filename = input("Enter filename with .json extension: ")
        
        if not os.path.exists(self.filename):

            with open(self.filename, "w") as file:
                json.dump(new_data, file, indent=4)
        
        else:
            with open(self.filename, "w") as file:
                json.dump(new_data, file, indent=4)
    
    # def revision():
    
    # def flashcards():
    

#Testing
dictionary = {
    "question": "What is my name",
    "answer": "kelly"
}

bot1 = bot("bot_response.json", "math", "08/01/2024")
bot1.read_json()

bot1.write_json(dictionary)
bot1.read_json()

    