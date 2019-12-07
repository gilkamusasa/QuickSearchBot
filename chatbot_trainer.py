from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import requests
from bs4 import BeautifulSoup


QuickSearchBot = ChatBot('Bot')
conversation = [
    "Hello",
    "Hello my name is QuickSearchBot. \n Please enter your required IFRS (eg IFRS 1) \n Type QUIT to stop chat",
    "Hi",
    "Hello my name is QuickSearchBot. \n Please enter your required IFRS (eg IFRS 1) \n Type QUIT to stop chat",
    "Good day",
    "Good day my name is QuickSearchBot. \n Please enter your required IFRS (eg IFRS 1) \n Type QUIT to stop chat",
    "Good morning",
    "Good morning my name is QuickSearchBot. \n Please enter your required IFRS (eg IFRS 1) \n Type QUIT to stop chat",
    "Good afternoon",
    "Good afternoon my name is QuickSearchBot. \n Please enter your required IFRS (eg IFRS 1) \n Type QUIT to stop chat",
    "Good evening",
    "Good evening my name is QuickSearchBot. \n Please enter your required IFRS (eg IFRS 1) \n Type QUIT to stop chat",
    "Ndeipi",
    "Ndeipi my name is QuickSearchBot. \n Please enter your required IFRS (eg IFRS 1) \n Type QUIT to stop chat",
    "Whats up",
    "Whats up my name is QuickSearchBot. \n Please enter your required IFRS (eg IFRS 1) \n Type QUIT to stop chat",
]

trainer = ListTrainer(QuickSearchBot)

trainer.train(conversation)


while True:
    message = input('You:')
    if message.upper().strip() != 'QUIT':
        formated_message = message.upper()
        if formated_message[:4] == 'IFRS':
            def search_spider():
                title_list = {}
                url = 'https://www.iasplus.com/en/standards'
                source_code = requests.get(url)
                plain_text = source_code.text
                soup = BeautifulSoup(plain_text, 'html.parser')
                for link in soup.findAll('a', {'class': 'internal-link'}):
                    href = link.get('href')
                    title = link.string
                    title_list[title] = href

                for title, href in title_list.items():
                    if formated_message == title:
                        print(href)
                        get_single_link_data(href)
                        break
                else:
                    print('Sorry your required IFRS is not available.')


            def get_single_link_data(href):
                source_code = requests.get(href)
                plain_text = source_code.text
                soup = BeautifulSoup(plain_text, 'html.parser')
                for link_content in soup.findAll('p'):
                    print(link_content.string)
            search_spider()
        else:
            response = QuickSearchBot.get_response(message)
            print('QuickSearchBot:', response)

    else:
        print('QuickSearchBot: Bye!')
        break
