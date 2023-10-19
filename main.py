import csv
import requests
from pathlib import Path
from util import (
    get_conv_csv_file,
    get_query_csv_file,
    get_gen_csv_file,
    read_xlsx_file,
    url,
    url_gen,
    url_query,
)


class Categorization:

    def __init__(self):
        """
        Initializes the class instance with the necessary attributes.
        """
        self.url_comp = ""
        # self.conversacional = get_conv_csv_file(url)
        self.conversacional = [
            "Hello, I am worried about my memory. I have noticed that sometimes I forget important things and have a hard time remembering details. Is there any exercise or technique that can help me?",
            "What's your go-to spot for a cup of joe?",
            "Sorry to hear that. Maybe try doing something that makes you happy, like hanging out with friends or doing a fun activity.",
            "I'm feeling kinda bummed out lately. Any advice?",
            "How are you today?",
            "Would you like to go out to dinner tonight?",
            "Do you want to watch a movie together tomorrow afternoon?",
            "How about we go to the park to exercise?",
        ]
        # self.consulta = read_xlsx_file()
        self.consulta = [
            "How long does it take for this system to work?",
            "What is the cost of shipping this product?",
            "How can I solve this problem?",
            "What are the advantages of using this product?",
            "Are there any known problems with this product?",
            "How long does it take for this system to work?",
            "How can I solve this problem?",
        ]
        # self.generacional = get_gen_csv_file(url_gen)
        self.generacional = [
            "I want create a text or a sentence?",
            "Please help me to create a campaign that'll make my products stand out?",
            "I need to generate a marketing campaign that showcases my unique selling proposition?",
            "I been looking for creating a marketing campaign, can you assist me?",
            "Assist me in creating a marketing campaign that targets customers based on their browser history?",
            "Are you guide me in creating a marketing campaign that analyzes customer personalities?",
        ]
        self.sentence = []
        self.data = {}
        self.current_sentence = None
        self.response = None
        self.context = {}
        self.filename = "save_int_query.csv"


    def set_data(self):
        self.data = {
            "temperature": 0.1,
            "max_tokens": 1024,
            "top_p": 0.9,
            "prompt": f"[INST]<<SYS>>Your are an chatbot assistant and given the following instructions: \n \n {self.conversacional} \n \n, \n \n  {self.consulta}  , \n \n {self.generacional} \n \n <</SYS>>: \
                    tell me about this new sentence \n \n {self.current_sentence} \n \n  what category of sentence does it correspond to (Conversation, Query, Generation) in a single word.[/INST]",
        }


    def get_data(self):
        """
        Get the data stored in the object.

        Returns:
            The data stored in the object.
        """
        return self.data


    def set_current_sentence(self,sentence):
        """
        Set the current sentence to the given sentence.

        Parameters:
            sentence (str): The sentence to set as the current sentence.

        Returns:
            None
        """
        self.current_sentence = sentence


    def get_current_sentence(self):
        """
        Get the current sentence.

        Returns:
            str: The current sentence.
        """
        return self.current_sentence


    def get_response(self):
        """
        Retrieves a response from the API.

        Returns:
            dict: A dictionary containing the response data.

        Raises:
            None
        """
        self.context = {}
        if self.current_sentence != None and self.current_sentence != "":
            self.set_data()
            self.response = requests.post(self.url_comp, json=self.data)
            self.context = self.response.json()
            if self.response.status_code != 200:
                print("Error al realizar la solicitud:", self.response.status_code)
                print(self.response.text)
        else:
            print("The current sentence is empty.")


    def get_query_of_data(self):
        """
        Extracts the query from the given data dictionary.
        Args:
            data: The input data dictionary.
        Returns:
            str: The extracted query.
        """
        content = self.context.get("choices")[0].get("text")
        result = content.split('"')
        if len(result) > 2:
            return result[len(result) - 2]
        return content
    

    def save_intention(self):
        """
        Saves the query in a csv file.
        Args:
            sentencia: The query to save.
            content: The data dictionary.
            existing_file: A boolean indicating whether the file already exists.
        """
        content = self.get_query_of_data()
        with open(self.filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([self.current_sentence, content])
            print(self.current_sentence)
            print(f"The '{self.current_sentence}' and the '{content}' are saved successfully.")


    def get_sentence(self):
        """
        Returns the value of the sentence attribute.

        :return: The value of the sentence attribute.
        """
        return self.sentence


    def set_sentence(self,filename='generacional.txt'):
        """
        Sets the `sentence` attribute of the class.

        Parameters:
            filename (str): The name of the file to read.

        Returns:
            None
        """
        self.sentence = []
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip('"",')   
                self.sentence.append(line)


    def generate_sentence(self):
        """
        Generates and returns a sentence based on the current state of the object.

        Parameters:
            self (object): The instance of the class.

        Returns:
            list: A list of sentences generated.
        """
        self.set_sentence()
        for sentence in self.sentence:
            self.set_current_sentence(sentence)
            self.set_data()
            self.get_response()
            self.save_intention()
        return self.sentence


    def set_filename(self, filename):
        """
        Set the filename attribute of the object.

        :param filename: The name of the file to be set.
        :type filename: str
        """
        self.filename = filename


# for i in range(20):
#     print("Working in  ",i)
#     cat = Categorization()
#     sleept = 5
#     cat.set_filename(f"queries_pocasm/save_in_query_{i}.csv")
#     cat.generate_sentence()
