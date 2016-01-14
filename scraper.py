import requests
from bs4 import BeautifulSoup as bs
import scraperwiki
from datetime import datetime
import re


start_url = 'http://www.amazon.com/gp/offer-listing/{}/ref%3Dolp_f_used?ie=UTF8&f_primeEligible=true&f_used=true&f_usedAcceptable=true&f_usedGood=true&f_usedLikeNew=true&f_usedVeryGood=true'
ua = {'User-agent': 'Mozilla/5.0'}


def connect(start_url, search_term):
    search_page = requests.get(start_url.format(search_term), headers=ua)
    soup = bs(search_page.text, 'lxml')
    title = ''
    try:
        title = soup.title.text
    except:
        pass
    while 'Robot Check' in title:
        search_page = requests.get(start_url.format(search_term), headers=ua)
        soup = bs(search_page.text, 'lxml')
        title = ''
        try:
            title = soup.title.text
        except:
            pass
    if soup:
        pass
    else:
        connect(start_url, search_term)
    return soup


def parse(search_term, search_tag, p):
    search_tag = '='+'"'+search_tag+'"'
    print p
    soup = connect(start_url, search_term)
    if 'used=true' in start_url:
            search_rows = []
            try:
                search_rows = soup.find_all('div', 'a-row a-spacing-mini olpOffer')
            except:
                pass
            if not search_rows:
                used_price_absent = 1
            else:
                used_price_absent = 0
            searchstring = search_term.strip()
            search_tag = search_tag
            used_price_lowest = used_price_0 = used_price_1 = used_price_2 = used_price_3 = used_price_4 = used_price_5 = used_price_6 = used_price_7 = used_price_8 = used_price_9 = used_cond_0 = used_cond_1 = used_cond_2 =\
                        used_cond_3 = used_cond_4 = used_cond_5 = used_cond_6 = used_cond_7 = used_cond_8 =  used_cond_9 = ''
            if used_price_absent == 0:
                for i, search_row in enumerate(search_rows):
                    try:
                        back_ordered = search_row.find('div', 'a-column a-span3 olpDeliveryColumn').find('ul', 'a-vertical').find('span', 'a-list-item').text.strip()
                        if i == 0:
                            used_price_lowest = search_row.find('span', 'a-size-large a-color-price olpOfferPrice a-text-bold').text.strip().split('$')[1].strip()
                            used_price_0 = search_row.find('span', 'a-size-large a-color-price olpOfferPrice a-text-bold').text.strip().split('$')[1].strip()
                            status_check = search_row.find('span', 'a-size-medium olpCondition a-text-bold').text.strip()
                            if '- Acceptable' in status_check:
                                used_cond_0 = 4
                            elif '- Good' in status_check:
                                used_cond_0 = 3
                            elif '- Very Good' in status_check:
                                used_cond_0 = 2
                            elif '- Like New' in status_check:
                                used_cond_0 = 1
                            if 'Back-ordered' in back_ordered:
                                used_cond_0 = used_price_0 = ''
                        elif i == 1:
                            used_price_1 = search_row.find('span', 'a-size-large a-color-price olpOfferPrice a-text-bold').text.strip().split('$')[1].strip()
                            status_check = search_row.find('span', 'a-size-medium olpCondition a-text-bold').text.strip()
                            if '- Acceptable' in status_check:
                                used_cond_1 = 4
                            if '- Good' in status_check:
                               used_cond_1 = 3
                            if '- Very Good' in status_check:
                                used_cond_1 = 2
                            if '- Like New' in status_check:
                                used_cond_1 = 1
                            if 'Back-ordered' in back_ordered:
                                used_cond_1 = used_price_0 = ''
                        elif i == 2:
                            used_price_2 = search_row.find('span', 'a-size-large a-color-price olpOfferPrice a-text-bold').text.strip().split('$')[1].strip()
                            status_check = search_row.find('span', 'a-size-medium olpCondition a-text-bold').text.strip()
                            if '- Acceptable' in status_check:
                                used_cond_2 = 4
                            if '- Good' in status_check:
                                used_cond_2 = 3
                            if '- Very Good' in status_check:
                                used_cond_2 = 2
                            if '- Like New' in status_check:
                                used_cond_2 = 1
                            if 'Back-ordered' in back_ordered:
                                used_cond_2 = used_price_2 = ''
                        elif i == 3:
                            used_price_3 = search_row.find('span', 'a-size-large a-color-price olpOfferPrice a-text-bold').text.strip().split('$')[1].strip()
                            status_check = search_row.find('span', 'a-size-medium olpCondition a-text-bold').text.strip()
                            if '- Acceptable' in status_check:
                                used_cond_3 = 4
                            if '- Good' in status_check:
                                used_cond_3 = 3
                            if '- Very Good' in status_check:
                                used_cond_3 = 2
                            if '- Like New' in status_check:
                                used_cond_3 = 1
                            if 'Back-ordered' in back_ordered:
                                used_cond_3 = used_price_3 = ''
                        if i == 4:
                            used_price_4 = search_row.find('span', 'a-size-large a-color-price olpOfferPrice a-text-bold').text.strip().split('$')[1].strip()
                            status_check = search_row.find('span', 'a-size-medium olpCondition a-text-bold').text.strip()
                            if '- Acceptable' in status_check:
                                used_cond_4 = 4
                            if '- Good' in status_check:
                                used_cond_4 = 3
                            if '- Very Good' in status_check:
                                used_cond_4 = 2
                            if '- Like New' in status_check:
                                used_cond_4 = 1
                            if 'Back-ordered' in back_ordered:
                                used_cond_4 = used_price_4 = ''
                        elif i == 5:
                            used_price_5 = search_row.find('span', 'a-size-large a-color-price olpOfferPrice a-text-bold').text.strip().split('$')[1].strip()
                            status_check = search_row.find('span', 'a-size-medium olpCondition a-text-bold').text.strip()
                            if '- Acceptable' in status_check:
                                used_cond_5 = 4
                            if '- Good' in status_check:
                                used_cond_5 = 3
                            if '- Very Good' in status_check:
                                used_cond_5 = 2
                            if '- Like New' in status_check:
                                used_cond_5 = 1
                            if 'Back-ordered' in back_ordered:
                                used_cond_5 = used_price_5 = ''
                        if i == 6:
                            used_price_6 = search_row.find('span', 'a-size-large a-color-price olpOfferPrice a-text-bold').text.strip().split('$')[1].strip()
                            status_check = search_row.find('span', 'a-size-medium olpCondition a-text-bold').text.strip()
                            if '- Acceptable' in status_check:
                                used_cond_6 = 4
                            if '- Good' in status_check:
                                used_cond_6 = 3
                            if '- Very Good' in status_check:
                                used_cond_6 = 2
                            if '- Like New' in status_check:
                                used_cond_6 = 1
                            if 'Back-ordered' in back_ordered:
                                used_cond_6 = used_price_6 = ''
                        elif i == 7:
                            used_price_7 = search_row.find('span', 'a-size-large a-color-price olpOfferPrice a-text-bold').text.strip().split('$')[1].strip()
                            status_check = search_row.find('span', 'a-size-medium olpCondition a-text-bold').text.strip()
                            if '- Acceptable' in status_check:
                                used_cond_7 = 4
                            if '- Good' in status_check:
                                used_cond_7 = 3
                            if '- Very Good' in status_check:
                                used_cond_7 = 2
                            if '- Like New' in status_check:
                                used_cond_7 = 1
                            if 'Back-ordered' in back_ordered:
                                used_cond_7 = used_price_7 = ''
                        if i == 8:
                            used_price_8 = search_row.find('span', 'a-size-large a-color-price olpOfferPrice a-text-bold').text.strip().split('$')[1].strip()
                            status_check = search_row.find('span', 'a-size-medium olpCondition a-text-bold').text.strip()
                            if '- Acceptable' in status_check:
                                used_cond_8 = 4
                            if '- Good' in status_check:
                               used_cond_8 = 3
                            if '- Very Good' in status_check:
                                used_cond_8 = 2
                            if '- Like New' in status_check:
                                used_cond_8 = 1
                            if 'Back-ordered' in back_ordered:
                                used_cond_8 = used_price_8 = ''
                        elif i == 9:
                            used_price_9 = search_row.find('span', 'a-size-large a-color-price olpOfferPrice a-text-bold').text.strip().split('$')[1].strip()
                            status_check = search_row.find('span', 'a-size-medium olpCondition a-text-bold').text.strip()
                            if '- Acceptable' in status_check:
                                used_cond_9 = 4
                            if '- Good' in status_check:
                                used_cond_9 = 3
                            if '- Very Good' in status_check:
                                used_cond_9 = 2
                            if '- Like New' in status_check:
                                used_cond_9 = 1
                            if 'Back-ordered' in back_ordered:
                                used_cond_9 = used_price_9 = ''

                    except:pass
            else:
                used_price_lowest = used_price_0 = used_price_1 = used_price_2 = used_price_3 = used_price_4 = used_price_5 = used_price_6 = used_price_7 = used_price_8 = used_price_9 = used_cond_0 = used_cond_1 = used_cond_2 =\
                        used_cond_3 = used_cond_4 = used_cond_5 = used_cond_6 = used_cond_7 = used_cond_8 =  used_cond_9 = ''

            today_date = str(datetime.now())
            scraperwiki.sqlite.save(unique_keys=['Date'], data={'SearchString': unicode(searchstring), 'Search Tag': search_tag, 'used_price_lowest': used_price_lowest,'used_price_0': used_price_0, 'used_price_1': used_price_1, 'used_price_2': used_price_2,
                                                                    'used_price_3': used_price_3, 'used_price_4': used_price_4, 'used_price_5': used_price_5, 'used_price_6': used_price_6, 'used_price_7': used_price_7, 'used_price_8': used_price_8
                    , 'used_price_9': used_price_9, 'used_cond_0': used_cond_0, 'used_cond_1': used_cond_1, 'used_cond_2': used_cond_2, 'used_cond_3': used_cond_3, 'used_cond_4': used_cond_4, 'used_cond_5': used_cond_5, 'used_cond_6': used_cond_6,
                      'used_cond_7': used_cond_7, 'used_cond_8': used_cond_8, 'used_cond_9': used_cond_9, 'used_price_absent': used_price_absent, 'Date': today_date})

if __name__ == '__main__':
        file1 = open('amazon.txt', 'r')
        p = 1
        for line in file1:
            search_term = line.split('%')[-1].replace('&', '%26')
            search_tag = line.split('%')[0]
            search_term = '+'.join(search_term.split(' '))
            parse(search_term.strip(), search_tag, p)
            p +=1
