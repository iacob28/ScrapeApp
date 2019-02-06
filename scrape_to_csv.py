import requests
from bs4 import BeautifulSoup
from time import sleep
from csv import DictWriter
from color_print import print_yellow_bold, print_purple_bold
from read_from_csv import read_from_csv
from config import BASE_URL



def scrape_to_csv():
    with open('quotes.csv', 'w') as file:
                fields_name = ['text', 'author', 'author_bio_link']
                writer = DictWriter(file, fieldnames=fields_name)
                writer.writeheader()
    page_number = '/page/1'
    while page_number:
        print_yellow_bold(f'Now scrapping {BASE_URL}{page_number}')
        res = requests.get(f'{BASE_URL}{page_number}')
        parser = BeautifulSoup(res.text, 'html.parser')
        quotes = parser.find_all(class_="quote")
        for quote in quotes:
            text = quote.find(class_="text").get_text()
            author = quote.find(class_="author").get_text()
            author_link = quote.find("a")['href']
            with open('quotes.csv', 'a') as file:
                fields_name = ['text', 'author', 'author_bio_link']
                writer = DictWriter(file, fieldnames=fields_name)
                writer.writerow({'text': text, 'author': author, 'author_bio_link': author_link})
        next_btn = parser.find(class_="next")
        page_number = next_btn.find("a")['href'] if next_btn else None
        sleep(1)
    print_purple_bold('Do you want to play the guessing game (Y/N)?')
    play_game_answer = input('-> ').lower()

    if play_game_answer in ('y', 'yes', 'yeah'):
        read_from_csv()
    else:
        print_yellow_bold('Ok, bye !')


if __name__ == '__main__':
    scrape_to_csv()