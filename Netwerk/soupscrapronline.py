from bs4 import BeautifulSoup
import requests

source = requests.get('https://en.wikipedia.org/wiki/Trafigura').text 

soup = BeautifulSoup(source, 'lxml')

article = soup.find('td')




print(article.prettify())

# headline = article.h2.a.text
# print(headline)

# summary = article.find('div',class_='entry-content').p.text
# print(summary)
# vid_source = article.find('iframe',class_='youtube-player')
# vid_source = article.find('iframe',class_='youtube-player')['src']
# print(vid_source)

# vid_id = vid_source.split('/')[4]
# vid_id = vid_id.split('?')[0]
# #print(vid_id)

# yt_link = f'https://youtube.com/watch?v={vid_id}'
# print(yt_link)