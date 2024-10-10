#Load JSON file with pre-existing questions and answers
#Process user input and find the most relevant in JSON file
#If a suitable answer is found then return it otherwise ask the user to teach the bot

import json

class bot:
    def __init__(self, filename, new):
        self.filename = filename
        self.new = new

    #read from JSON file
    def read_json(self):
    #reads json file and converts the data into a python dictionary
        with open(self.filename) as file:
            data = json.load(file)

        print(data)

    #Write to JSON file 
    #
    def write_file(self, data):
        
        if self.new:
            filename = input("Enter filename with .json extension: ")

            with open(filename, "w") as file:
                json.dump(data, file, indent=4)

        else:
            with open(self.filename, "w") as file:
                json.dump(data, indent=4)



    