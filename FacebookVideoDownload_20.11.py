import bs4
import requests

url = "https://www.facebook.com/ParadiseWildlifeParkZSH/videos/black-friday-super-sale-paradise-wildlife-park/213430976864387/?__so__=permalink&__rv__=related_videos"

re = requests.get(url)

soup = bs4.BeautifulSoup(re.text,"html.parser")

re2 = soup.find_all('script',type="application/ld+json")

re3 = ((str(re2).split('"')))

print(re3[31].replace('\\',""))
