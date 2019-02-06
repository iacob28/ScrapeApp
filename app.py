import subprocess
from color_print import print_green_bold, print_yellow_bold
from scrape_to_csv import scrape_to_csv
from read_from_csv import read_from_csv
from config import BASE_URL


#CLEAR TERMINAL

command = 'clear'
subprocess.check_call(command.split())

#TERMCOLOR


print_green_bold(f'Do you want to make a new scrape to {BASE_URL} (Y/N) ?')
scrape_answer = input('-> ').lower()

if scrape_answer in ('y', 'yes', 'yeah'):
    scrape_to_csv()
else:
    read_from_csv()




