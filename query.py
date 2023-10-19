import requests
from util import get_conv_csv_file, get_query_csv_file, get_gen_csv_file
from util import read_xlsx_file, url, url_gen, url_query


url_comp = 'http://hddevp.no-ip.org:7002/v1/completions'


conversacional = [
    'Hello, I am worried about my memory. I have noticed that sometimes I forget important things and have a hard time remembering details. Is there any exercise or technique that can help me?',
    "What's your go-to spot for a cup of joe?",
    'Sorry to hear that. Maybe try doing something that makes you happy, like hanging out with friends or doing a fun activity.',
    "I'm feeling kinda bummed out lately. Any advice?",
    'How are you today?',
    'Would you like to go out to dinner tonight?',
    'Do you want to watch a movie together tomorrow afternoon?',
    'How about we go to the park to exercise?',
]
consulta = [
    'How long does it take for this system to work?',
    'What is the cost of shipping this product?',
    'How can I solve this problem?',
    'What are the advantages of using this product?',
    'Are there any known problems with this product?',
    'How long does it take for this system to work?',
    'How can I solve this problem?',
]
generacional = [
    'I want create a text or a sentence?',
    "Please help me to create a campaign that'll make my products stand out?",
    'I need to generate a marketing campaign that showcases my unique selling proposition?',
    'I been looking for creating a marketing campaign, can you assist me?',
    'Assist me in creating a marketing campaign that targets customers based on their browser history?',
    'Are you guide me in creating a marketing campaign that analyzes customer personalities?',
]
sentencia = input('Write your answer: ')
print(sentencia)
data = {
    'temperature': 0.1,
    'max_tokens': 1024,
    'top_p': 0.9,
    'prompt': f'[INST]<<SYS>>Your are an chatbot assistant and given the following instructions: \n \n {conversacional} \n \n, \n \n  {consulta}  , \n \n {generacional} \n \n <</SYS>>: \
            tell me about this new sentence \n \n {sentencia} \n \n  what category of sentence does it correspond to (Conversation, Query, Generation) in a single word.[/INST]',
}

response = requests.post(url_comp, json=data)


def get_data():
    if response.status_code != 200:
        print('Error al realizar la solicitud:', response.status_code)
        print(response.text)
    elif response.status_code == 200:
        data = response.json()
        print(data)
    return data


def get_query_of_data(data):
    content = data.get('choices')[0].get('text')
    result = content.split('"')
    if len(result) > 2:
        return result[len(result) - 2]
    return content
    

if __name__ == '__main__':
    data = get_data()
    intention = get_query_of_data(data)
    print(intention)
