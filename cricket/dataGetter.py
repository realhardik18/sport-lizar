from bs4 import BeautifulSoup
import requests
import time
#from classes import class_score, class_commentary, class_overs, class_for_toss
from matchinfo import match_url


def get_commentary(url, class_for_commentary_cards):
    pageResponse = requests.get(url).text
    soup = BeautifulSoup(pageResponse, "html.parser")
    entry = soup.find(
        class_=class_for_commentary_cards)
    return entry.text.strip('\n')[5:]


def get_score(url, class_for_score):
    pageResponse = requests.get(url).text
    soup = BeautifulSoup(pageResponse, "html.parser")
    entries = soup.find(
        class_=class_for_score)
    for entry in entries:
        return entry.text.split(' ')[-1]


def get_overs(url, class_for_overs):
    pageResponse = requests.get(url).text
    soup = BeautifulSoup(pageResponse, "html.parser")
    entry = soup.find(
        class_=class_for_overs)
    return entry.text


def get_toss_result(url, class_for_toss):
    pageResponse = requests.get(url).text
    soup = BeautifulSoup(pageResponse, "html.parser")
    entry = soup.find(
        class_=class_for_toss)
    return entry.text


def get_score_from_title_of_site(url):
    pageResponse = requests.get(url)
    soup = BeautifulSoup(pageResponse.text, 'html.parser')
    for title in soup.find_all('title'):
        return title.get_text().split(' ')[1]


#print(get_toss_result(match_url, class_for_toss))
# print(get_score_from_title_of_site(match_url))
