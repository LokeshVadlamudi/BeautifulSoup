import requests

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

#for getting the status code
# print(page.status_code)

#for getting the content from the page
# print(page.content)

#importing beautiful Soup library
from bs4 import BeautifulSoup

#creating instance of the beautiful soup class
# soup = BeautifulSoup(page.content,'html.parser')

#lets print the formatted html content
# print(soup.prettify())

#lets call children property of the soup

# print(list(soup.children))


#lets get type of each element

# print([type(item) for item in list(soup.children)])

#now let us deal with the html tags and its children
# html = list(soup.children)[2]

#let us call children method on html object

# print(list(html.children))

#going into body tag to extract p tag

# body = list(html.children)[3]

# p = list(body.children)[1]

#.get_text() isolates the tag and extracts all the text
# print(p.get_text())


#thus we have figured out how to navigate the html
#lets use even more easier method


#finding all instances of a tag at once

# soup = BeautifulSoup(page.content,'html.parser')
# print(soup.find_all('p'))

# print(soup.find_all('p')[0].get_text())

#if we only want to find the first instance of a tag,
#we can just use find method

# print(soup.find('p'))



# now lets search for tags by class and id

page1 = requests.get('http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html')

soup = BeautifulSoup(page1.content,'html.parser')
# print(soup)

# print(soup.find_all('p', class_='outer-text'))

# print(soup.find_all(class_='outer-text'))

# print(soup.find_all(id='first'))


# we can also use css selectors
# select returns a list of BeautifulSoup objects
# print(soup.select('div p'))






