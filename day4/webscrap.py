from bs4 import BeautifulSoup
import requests
response=requests.get(" https://news.ycombinator.com/")
contents=response.text
soup=BeautifulSoup(contents,"html.parser")
print("Headings:")
headings=soup.find_all(class_="athing")
all=headings[0:]
for h1 in all:
    print(h1.text)
print("Score:")
score=soup.find_all(class_="score")
all=score[0:]
for points in all:
    print(points.text)
print("Links of the headings:")
link=soup.find_all(class_="sitestr")
all=link[0:]
for anchor in all:
    print(anchor.text)