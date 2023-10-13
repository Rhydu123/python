import re

url = "https://www.example.com/page"
pattern = r'https?://(www\.)?([^/]+)'
match = re.search(pattern, url)

if match:
    domain = match.group(2)
    print(domain)
	
