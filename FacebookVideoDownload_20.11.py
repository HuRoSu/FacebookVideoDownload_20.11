import bs4
import requests

url = input()

re = requests.get(url)

soup = bs4.BeautifulSoup(re.text,"html.parser")

re2 = soup.find_all('script',type="application/ld+json")

re3 = ((str(re2).split('"')))

print(re3[31].replace('\\',""))
