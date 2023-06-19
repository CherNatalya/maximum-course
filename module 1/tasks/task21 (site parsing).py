import requests
from bs4 import BeautifulSoup
titles = []
response = requests.get('http://www.columbia.edu/~fdc/sample.html')
response = response.content
html = BeautifulSoup(response, 'lxml')
contents = html.find_all("h3")
for content in contents:
    titles.append(content.get_text())
print(titles)
a = ()
