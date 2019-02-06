import requests
from bs4 import BeautifulSoup
from csv import DictReader
from random import choice
from config import BASE_URL
from color_print import print_green_bold, print_yellow_bold


def read_from_csv():
    with open('quotes.csv', 'r') as file:
            reader = list(DictReader(file))
            quote_choice = choice(reader)
            print(quote_choice['text'])
            print(quote_choice['author'])
            
    reamaning_guesses = 4
    guess = ''
    while guess.lower() != quote_choice['author'].lower() and reamaning_guesses > 0:
        guess = input(f"What author said this? Reamaning guessses: {reamaning_guesses}, -> ") 
        reamaning_guesses  -= 1
        if guess.lower() == quote_choice['author'].lower():
            print_green_bold('Your answer is CORRECT !!')
            break
        if reamaning_guesses == 3:
            req = requests.get(f"{BASE_URL}{quote_choice['author_bio_link']}")
            soup = BeautifulSoup(req.text, 'html.parser')
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_location = soup.find(class_="author-born-location").get_text()
            print(f"Author Birth Date is: {birth_date} and was born {birth_location}")
        elif reamaning_guesses == 2:
            print(f"First initial is: {quote_choice['author'][0]}")
        elif reamaning_guesses == 1:
            last_initials = quote_choice['author'].split(" ")[1][0]
            print(f"Last initials of the author is {last_initials}")
        else:
            print("Sorry, you ran out of guesses !")

    print_yellow_bold('Do you want to play again (Y/N) ?')
    play_again = ''
    while play_again not in ('y', 'yes', 'n', 'no'):
        play_again = input('-> ').lower()
    if play_again in ('y', 'yes', 'yeah', 'sure'):
        return read_from_csv()
    else:
        print_yellow_bold('Ok, bye !!')


if __name__ == '__main__':
    read_from_csv()