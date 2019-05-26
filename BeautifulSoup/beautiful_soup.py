import requests
from bs4 import BeautifulSoup

webpage_response = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

import re
# print((soup.find_all(re.compile("(div)"))))
# print(soup.find_all(attrs = {'class' : 'more-info'}))

turtle_links = soup.find_all(re.compile("\Aa\Z"))
print(turtle_links)





