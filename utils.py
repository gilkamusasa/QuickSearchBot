from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import requests
from bs4 import BeautifulSoup


QuickSearchBot = ChatBot('Bot')

trainer = ListTrainer(QuickSearchBot)


def fetch_reply(message):
    if message.upper().strip() != 'QUIT':
        if message.upper()[:4] == 'IFRS':
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
                    if message.upper() == title:
                        get_single_link_data(href)
                    else:
                        return 'Sorry your required IFRS is not available.'

            def get_single_link_data(href):
                source_code = requests.get(href)
                plain_text = source_code.text
                soup = BeautifulSoup(plain_text, 'html.parser')
                for link_content in soup.findAll('p'):
                    return str(link_content.string)

            search_spider()

        else:
            response = QuickSearchBot.get_response(message)
            return response

    else:
        return 'Bye!'




