import re

def find_urls(text):
    url_pattern = r'https?://\S+|www\.\S+'
    urls = re.findall(url_pattern, text)
    return urls


text = "Here are some URLs: https://www.example.com and http://www.openai.com, also, check www.google.com"

urls = find_urls(text)

for url in urls:
    print(url)

