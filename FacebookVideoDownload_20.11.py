import bs4
import requests

url = input()

re = requests.get(url)

soup = bs4.BeautifulSoup(re.text,"html.parser")

find_application = soup.find_all('script',type="application/ld+json")

code_split = ((str(find_application).split('"')))

print(code_split[31].replace('\\',""))
