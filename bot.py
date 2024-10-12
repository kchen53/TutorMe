#Load JSON file with pre-existing questions and answers
#Process user input and find the most relevant in JSON file
#If a suitable answer is found then return it otherwise ask the user to teach the bot

import json
import os

class bot:
    def __init__(self, filename):
        self.filename = filename

    #read from JSON file
    def read_json(self):
    #reads json file and converts the data into a python dictionary
        with open(self.filename) as file:
            data = json.load(file)

        print(data)

    #Write to JSON file 
    def write_json(self, new_data):

        self.filename = input("Enter filename with .json extension: ")
        
        if not os.path.exists(self.filename):

            with open(self.filename, "w") as file:
                json.dump(new_data, file, indent=4)
        
        else:
            with open(self.filename, "w") as file:
                json.dump(new_data, file, indent=4)
       

#Testing
dictionary = {
    "question": "What is my name",
    "answer": "kelly"
}

bot1 = bot("bot_response.json")

bot1.read_json()

bot1.write_json(dictionary)
bot1.read_json()

    