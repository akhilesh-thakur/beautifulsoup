from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup, Comment

# # Read the HTML content from the file
# with open('chatGpt.html', 'r', encoding='utf-8') as file:
#     htmlContent = file.read()
# # Get all the linsk please put the above code after "allLinks = set()"
# for link in anchors:
#     href = link.get('href')
#     if href and href != '#':  # Exclude empty or '#' links
#         allLinks.add(href)  # Store the link as is
# # Print only unique links
# for link in allLinks:
#     print(link)


url = "https://thehindu.com"
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')

# # Get the title of the page
# title = soup.title 
# print(title)


# # Get all the paras
# paras = soup.find_all('p')
# print(paras)


# Get all the anchors
anchors = soup.find_all('a')
allLinks = set()
for link in anchors:
     href = link.get('href')
     if href and href != '#':  # Exclude empty or '#' links
        # Combine the base URL with the relative URL if needed
        full_link = urljoin(url, href)
        allLinks.add(full_link)
# print only unique links
for link in allLinks:
    print(link)


