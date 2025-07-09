import pandas as pd
import requests
from http import HTTPStatus
import fake_useragent as fua

sites = pd.read_csv("websites.csv")
sitesList = sites['link']
ua = fua.UserAgent().firefox


for elmnt in sitesList:
    if 'http' not in elmnt:
        elmnt = 'https://' + elmnt
    
    try:
        print(elmnt,end= '--> ')
        result = requests.get(elmnt,  headers={'User-Agent': ua}).status_code # , headers={"User-Agent": ua}
        if result in HTTPStatus:
              print(result)
        else:
            print('Status code unbekannt')      

    except requests.exceptions.ConnectionError as e:
        print ('Seite konnte nicht abgerufen werden !')    


# ua = fua.UserAgent()
# print(ua.chrome)

